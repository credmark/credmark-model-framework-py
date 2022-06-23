#! /usr/bin/env python3
import os
import sys
import argparse
import logging
import json
import unittest
import inspect
from typing import List, Union
from dotenv import load_dotenv, find_dotenv

from .engine.context import EngineModelContext
from .engine.model_loader import ModelLoader
from .engine.mocks import MockGenerator, ModelMockRunner
from .engine.web3_registry import Web3Registry
from .engine.model_api import ModelApi
from credmark.dto import json_dump, json_dumps
from credmark.cmf.engine.model_unittest import ModelTestContextFactory
from credmark.cmf.model.print import print_manifest, print_manifest_description


logger = logging.getLogger(__name__)

EngineModelContext.dev_mode = True


def add_api_url_arg(parser):
    parser.add_argument('--api_url', required=False, default=None,
                        help='Credmark API url. '
                        'Defaults to the standard API gateway. '
                        'You do not normally need to set this.')


def main():  # pylint: disable=too-many-statements
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Credmark developer tool')
    parser.add_argument('--log_level', default=None, required=False,
                        help='Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL')
    parser.add_argument('--log_file', default=None, required=False,
                        help='log file to write')
    parser.add_argument('--model_path', default="models", required=False,
                        help='Semicolon separated paths to the model folders \
                            (or parent) or model python file. Defaults to models folder.')
    parser.add_argument('--manifest_file', type=str, default='models.json',
                        help='Name of the built manifest file. Defaults to models.json. '
                        '[Not required during development]')

    subparsers = parser.add_subparsers(title='Commands',
                                       description='Supported commands',
                                       help='additional help')

    parser_version = subparsers.add_parser(
        'version', help='Show version of the framework', aliases=[])
    parser_version.set_defaults(func=show_version)

    parser_list = subparsers.add_parser(
        'list', help='List models in this repo', aliases=['list-models'])
    parser_list.add_argument('--manifests', action='store_true', default=False,
                             help="Show full manifests")
    parser_list.add_argument('--include_dev_models', action='store_true',
                             default=False, help=argparse.SUPPRESS)
    parser_list.add_argument('--json', action='store_true',
                             default=False, help="Output as json")
    parser_list.add_argument('model-slug', nargs='?', default=None, type=str,
                             help='[OPTIONAL] Slug for the model to show.')
    parser_list.set_defaults(func=list_models)

    parser_models = subparsers.add_parser(
        'models', help='List models deployed on server', aliases=['deployed-models'])
    parser_models.add_argument('--manifests', action='store_true', default=False,
                               help="Show full manifests")
    parser_models.add_argument('--json', action='store_true',
                               default=False, help="Output as json")
    parser_models.add_argument('model-slug', nargs='?', default=None, type=str,
                               help='[OPTIONAL] Slug for the model to show.')
    add_api_url_arg(parser_models)
    parser_models.set_defaults(func=list_deployed_models)

    parser_desc = subparsers.add_parser(
        'describe', help='Show documentation for local and deployed models',
        aliases=['describe-models', 'man'])
    parser_desc.add_argument('model-slug', nargs='?', default=None, type=str,
                             help='Slug or partial slug to describe.')
    add_api_url_arg(parser_desc)
    parser_desc.set_defaults(func=describe_models)

    parser_create = subparsers.add_parser(
        'create', help='Create a new model skeleton file',
        aliases=['create-model'])
    parser_create.add_argument(
        'model_folder', default='(missing model_folder arg)',
        help='The name of the folder under "models/contrib" in which to put the new model file. '
        'Ex. "my_models"')
    parser_create.add_argument(
        'filename', default='(missing filename arg)',
        help='The name of the new model file. Ex. "model.py"')
    parser_create.set_defaults(func=create_model)

    parser_run = subparsers.add_parser('run', help='Run a model', aliases=['run-model'])
    parser_run.add_argument('-b', '--block_number', type=int, required=False, default=None,
                            help='Block number used for the context of the model run.'
                            ' If not specified, it is set to the latest block of the chain.')
    parser_run.add_argument('-c', '--chain_id', type=int, default=1, required=False,
                            help='Chain ID. Defaults to 1.')
    parser_run.add_argument('-i', '--input', required=False, default='{}',
                            help='Input JSON or '
                            'if value is "-" it will read input JSON from stdin.')
    parser_run.add_argument('-o', '--output', required=False, default=None,
                            help='Output path to save model results as JSON file.')
    parser_run.add_argument('-v', '--model_version', default=None, required=False,
                            help='Version of the model to run. Defaults to latest.')
    parser_run.add_argument('-j', '--format_json', action='store_true', default=False,
                            help='Format output json to be more readable')
    parser_run.add_argument('-d', '--debug', action='store_true', default=False,
                            help='Log debug info for model run input and output')
    parser_run.add_argument(
        '-l', '--use_local_models', default=None,
        help='Comma-separated list of model slugs for models that should '
        'favor use of the local version. This is only required when a model is '
        'calling another model. Use "*" to favor the use of local versions of all models.'
        ' Use "-" to use no local models.')
    parser_run.add_argument(
        '-m', '--model_mocks', default=None,
        help='Module path and symbol of model mocks config to use. '
        'For example, models.contrib.mymodels.mymocks.mock_config')
    parser_run.add_argument(
        '--generate_mocks', default=None,
        help='Generate model mocks and write them to the specified file. '
        'The generated python file can be used with --model_mocks on another run or in unit tests.')
    parser_run.add_argument('--provider_url_map', required=False, default=None,
                            help='JSON object of chain id to Web3 provider HTTP URL. '
                            'Overrides settings in env var or .env file.')
    add_api_url_arg(parser_run)
    parser_run.add_argument('--run_id', help=argparse.SUPPRESS, required=False, default=None)
    parser_run.add_argument('--depth', help=argparse.SUPPRESS, type=int, required=False, default=0)
    parser_run.add_argument(
        'model-slug', default='(missing model-slug arg)',
        help='Slug for the model to run or "console" for the interactive console.')
    parser_run.set_defaults(func=run_model, depth=0)

    parser_test = subparsers.add_parser('test', help='Run model tests', aliases=['run-tests'])
    parser_test.add_argument('-p', '--pattern', required=False, default='test*.py',
                             help='Pattern to match test files (test*.py default).')
    add_api_url_arg(parser_test)
    parser_test.add_argument('--provider_url_map', required=False, default=None,
                             help='JSON object of chain id to Web3 provider HTTP URL. '
                             'Overrides settings in env var or .env.test file.')
    parser_test.add_argument('tests_folder', nargs='?', default='models',
                             help='Folder to start discovery for tests. Defaults to "models".')
    parser_test.set_defaults(func=run_tests)

    parser_build = subparsers.add_parser(
        'build', help='Build model manifest [Not required during development]',
        aliases=['build-manifest'])
    parser_build.set_defaults(func=write_manifest_file)

    parser_clean = subparsers.add_parser(
        'clean', help='Clean model manifest', aliases=['remove-manifest'])
    parser_clean.set_defaults(func=remove_manifest_file)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    if args.func == run_tests:  # pylint: disable=comparison-with-callable
        load_dotenv(find_dotenv('.env.test', usecwd=True))
    else:
        load_dotenv(find_dotenv(usecwd=True))

    args.func(vars(args))


def config_logging(args, default_level='WARNING'):
    level = args['log_level']
    log_file = args['log_file']
    if not level:
        level = default_level
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=level,
        filename=log_file,
        filemode='w')


def load_models(args, load_dev_models=False):
    manifest_file = args.get('manifest_file')
    model_path: str = args['model_path']
    if model_path is not None:
        model_paths = model_path.split(';')
    else:
        model_paths = None

    # We add the tests folder (if set)
    # to the models paths if not present
    tests_folder = args.get('tests_folder')
    if tests_folder:
        if model_paths is None:
            model_paths = [tests_folder]
        else:
            if tests_folder not in model_paths:
                model_paths.append(tests_folder)

    model_loader = ModelLoader(model_paths, manifest_file, load_dev_models)
    model_loader.log_errors()
    return model_loader


def show_version(_args):
    import credmark.cmf  # pylint: disable=import-outside-toplevel
    ver = credmark.cmf.__version__
    print(f'credmark-model-framework version {ver}')
    sys.exit(0)


def describe_models(args):
    config_logging(args)
    model_api = create_model_api(args)
    model_loader = load_models(args, True)

    manifests = model_loader.loaded_model_manifests()
    try:
        deployed_manifests = model_api.get_models()
    except Exception:
        # Error will have been logged but we continue
        # so things work offline
        deployed_manifests = []

    manifests = merge_manifests(manifests, deployed_manifests)

    model_slug = args.get('model-slug')
    if model_slug is not None:
        manifests = [m for m in manifests if model_slug in m['slug']]

    print('')
    if len(manifests) > 0:
        print_manifests(manifests, True)
        exit_code = 0
    else:
        print_no_models_found(model_slug)
        exit_code = 1
    sys.exit(exit_code)


def print_no_models_found(model_slug):
    if model_slug:
        print(f'No models matching slug {model_slug}')
    else:
        print('No models found')


def list_models(args):  # pylint: disable=too-many-branches
    config_logging(args)

    model_loader = load_models(args, args.get('include_dev_models', False))
    json_output = args.get('json')
    model_slug = args.get('model-slug')

    if not json_output:
        sys.stdout.write('\nLoaded models:\n\n')

    if args.get('manifests'):
        manifests = model_loader.loaded_model_manifests()
        if model_slug is not None:
            manifests = [m for m in manifests if model_slug in m['slug']]
        if json_output:
            json.dump({'models': manifests}, sys.stdout)
        else:
            if len(manifests) > 0:
                print_manifests(manifests)
            else:
                print_no_models_found(model_slug)
    else:
        models = model_loader.loaded_model_version_lists()
        if model_slug is not None:
            models = {k: v for k, v in models.items() if model_slug in k}

        if json_output:
            json.dump(models, sys.stdout)
        else:
            slugs = list(models.keys())
            slugs.sort()
            if len(slugs) > 0:
                for s in slugs:
                    sys.stdout.write(f' - {s}: {models[s]}\n')
            else:
                print_no_models_found(model_slug)

    error_count = len(model_loader.errors)
    warning_count = len(model_loader.warnings)
    if not json_output:
        sys.stdout.write('\n')
        sys.stdout.write(
            f'{error_count} errors, {warning_count} warnings\n\n')
    sys.exit(0 if error_count == 0 else 1)


def create_model_api(args):
    api_url = args.get('api_url')
    return ModelApi.api_for_url(api_url)


def merge_manifests(manifests: List[dict], extra_manifests: List[dict]):
    """
    We copy the list because it may be owned by the model_loader.
    """
    merged = manifests.copy()
    slugs = {m['slug'] for m in merged}
    for m in extra_manifests:
        if not m['slug'] in slugs:
            merged.append(m)
    merged.sort(key=lambda m: m['slug'])
    return merged


def list_deployed_models(args):  # pylint: disable=too-many-branches
    config_logging(args)
    json_output = args.get('json')
    model_slug = args.get('model-slug')
    show_manifests = args.get('manifests') or model_slug
    model_api = create_model_api(args)

    if model_slug:
        model = model_api.get_model(model_slug)
        if model is not None:
            deployments = model_api.get_model_deployments(model_slug)
            if deployments:
                model['versions'] = {
                    dep["version"]: dep.get("location", "") for dep in deployments}
            manifests = [model]
        else:
            manifests = []
    else:
        manifests = model_api.get_models()

    if not json_output:
        if model_slug:
            sys.stdout.write('\n')
            if len(manifests) == 0:
                sys.stdout.write(f'Model slug {model_slug} not found on server.\n\n')
        else:
            sys.stdout.write('\nDeployed Models:\n\n')

        if show_manifests:
            print_manifests(manifests)
        else:
            for model in manifests:
                print(f'{model["slug"]} : {model.get("displayName", "")}')
            print('')
    else:
        json.dump(manifests, sys.stdout)


def print_manifests(manifests: List[dict], describe_schemas=False):
    for m in manifests:  # pylint: disable=too-many-nested-blocks
        if describe_schemas:
            print_manifest_description(m, sys.stdout)
        else:
            print_manifest(m, sys.stdout)
        sys.stdout.write('\n')


def create_model(args):
    import credmark.cmf.model.template  # pylint: disable=import-outside-toplevel

    model_folder = args['model_folder'].replace('-', '_')

    filename = args['filename'].replace('-', '_')
    if not filename.endswith('.py'):
        filename += '.py'

    folder_path = os.path.join('models', 'contrib', model_folder)
    file_path = os.path.join(folder_path, filename)

    if not os.path.isdir(folder_path):
        try:
            print(f'Creating folder {folder_path}')
            os.mkdir(folder_path)
        except Exception as exc:
            logger.error(f'Error creating model folder {folder_path}: {exc}')
            sys.exit(1)

    if os.path.isfile(file_path):
        res = input(f'File {file_path} exists, overwrite [Y/n]? ')
        if res not in ['', 'Y', 'y']:
            print('Exiting...')
            sys.exit(1)
    try:
        print(f'Creating file {file_path}')
        with open(file_path, 'w') as file:
            file.write(inspect.getsource(credmark.cmf.model.template))
    except Exception as exc:
        logger.error(f'Error writing model template to path {file_path}: {exc}')

    sys.exit(0)


def write_manifest_file(args):
    config_logging(args, 'INFO')
    manifest_file = args.get('manifest_file')
    ModelLoader.remove_manifest_file(manifest_file)

    model_loader = load_models(args)

    models = model_loader.loaded_model_version_lists()
    sys.stdout.write(f'\nLoaded {len(models)} models:\n')

    slugs = list(models.keys())
    slugs.sort()
    if len(slugs) > 0:
        for s in slugs:
            sys.stdout.write(f' - {s}: {models[s]}\n')
    sys.stdout.write('\n')

    error_count = len(model_loader.errors)
    warning_count = len(model_loader.warnings)
    sys.stdout.write(f'{error_count} errors, {warning_count} warnings\n\n')

    if error_count == 0:
        model_loader.write_manifest_file()
    else:
        sys.stdout.write('** Not writing manifest due to errors.\n')

    sys.exit(0 if error_count == 0 else 1)


def remove_manifest_file(args):
    config_logging(args)
    manifest_file = args.get('manifest_file')
    ModelLoader.remove_manifest_file(manifest_file)
    sys.exit(0)


def create_chain_to_provider_url(providers_json):
    # if arg is provided, it overrides any providers env vars
    if providers_json is not None:
        try:
            chain_to_provider_url = json.loads(providers_json)
        except Exception as err:
            logger.error(f'Error parsing JSON in arg provider_url_map: {err}')
            raise
    else:
        try:
            chain_to_provider_url = Web3Registry.load_providers_from_env()
        except Exception as err:
            logger.error(f'{err}')
            raise
    return chain_to_provider_url


def run_tests(args):
    config_logging(args, 'INFO')

    api_url: Union[str, None] = args['api_url']
    providers_json = args['provider_url_map']
    chain_to_provider_url = create_chain_to_provider_url(providers_json)
    model_loader = load_models(args, load_dev_models=True)

    factory = ModelTestContextFactory(model_loader, chain_to_provider_url, api_url)
    ModelTestContextFactory.use_factory(factory)

    pattern = args['pattern']
    tests_folder = args['tests_folder']
    test_argv = [sys.argv[0], 'discover',
                 '-s', tests_folder, '-p', pattern]
    unittest.main(module=None, argv=test_argv, verbosity=2)


def run_model(args):  # pylint: disable=too-many-statements,too-many-branches,too-many-locals
    exit_code = 0

    try:
        config_logging(args, 'INFO')

        chain_to_provider_url = None
        providers_json = args['provider_url_map']

        chain_to_provider_url = create_chain_to_provider_url(providers_json)

        model_loader = load_models(args, load_dev_models=not args.get(
            'run_id'))  # we assume developer will not pass a run_id

        chain_id: int = args['chain_id']
        block_number: Union[int, None] = args['block_number']
        model_slug: str = args['model-slug']
        model_version: Union[str, None] = args['model_version']
        api_url: Union[str, None] = args['api_url']
        run_id: Union[str, None] = args['run_id']
        depth: int = args['depth']
        format_json: bool = args['format_json']
        debug_log: bool = args['debug']
        use_local_models: Union[str, None] = args['use_local_models']
        model_mocks_config: Union[str, None] = args['model_mocks']
        generate_mocks: Union[str, None] = args.get('generate_mocks')

        if model_mocks_config:
            model_mock_runner = ModelMockRunner(model_mocks_config)
            EngineModelContext.use_model_mock_runner(model_mock_runner)

        if generate_mocks is not None:
            if not generate_mocks.endswith('.py'):
                generate_mocks += '.py'
            mock_gen = MockGenerator()
            EngineModelContext.add_model_run_listener(mock_gen.model_run)
        else:
            mock_gen = None

        if debug_log:
            dbg_logger = logging.getLogger('credmark.cmf.engine.context.debug')
            handler = logging.StreamHandler(sys.stderr)
            handler.setFormatter(logging.Formatter('%(message)s\n'))
            dbg_logger.propagate = False
            dbg_logger.addHandler(handler)
            dbg_logger.setLevel(logging.DEBUG)

        if args['input'] != '-':
            input = json.loads(args['input'])
        else:
            sys.stderr.write('Reading input JSON on stdin\n')
            input = json.load(sys.stdin)

        result = EngineModelContext.create_context_and_run_model(
            chain_id=chain_id,
            block_number=block_number,
            model_slug=model_slug,
            model_version=model_version,
            input=input,
            model_loader=model_loader,
            chain_to_provider_url=chain_to_provider_url,
            api_url=api_url,
            run_id=run_id,
            depth=depth,
            use_local_models=use_local_models)

        if generate_mocks is not None and mock_gen is not None:
            logger.info(f'Writing mocks to file "{generate_mocks}"')
            mock_gen.write(generate_mocks, model_slug)

        if 'error' in result:
            etype = result.get('error', {}).get('type')
            if etype == 'ModelInputError':
                exit_code = 2
            elif etype == 'ModelNotFoundError':
                exit_code = 126
            elif etype == 'ModelDataError':
                exit_code = 3
            else:
                exit_code = 1

        if model_slug != 'console':
            if format_json:
                print(json_dumps(result, indent=4).replace('\\n', '\n').replace('\\"', '\''))
            elif args['output']:
                logger.info(f"Saving model results to {args['output']}")
                with open(args['output'], 'w') as fp:
                    json.dump(result, fp, indent=4)
            else:
                json_dump(result, sys.stdout)

    except Exception as e:
        # this exception would only happen have been raised
        # within this file itself
        logger.exception('Run processing error')
        msg = {
            "error": {
                "type": "ModelEngineError",
                "message": f'Error in credmark-dev: {str(e)}'
            }
        }
        if args.get('model-slug') != 'console':
            json.dump(msg, sys.stdout)
        exit_code = 1
    finally:
        sys.stdout.write('\n')
        sys.stdout.flush()

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
