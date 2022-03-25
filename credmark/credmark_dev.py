#! /usr/bin/env python3
import sys
import argparse
import logging
import json
from typing import (
    List,
    Union,
)

from dotenv import load_dotenv, find_dotenv

from credmark.dto.dto_error_schema import extract_error_codes_and_descriptions
sys.path.append('.')
from .model.engine.context import EngineModelContext
from .model.engine.model_loader import ModelLoader
from .model.web3 import Web3Registry
from .model.engine.model_api import ModelApi
from .dto import (
    json_dump,
    print_example,
    print_tree,
    dto_schema_viz,
)

logger = logging.getLogger(__name__)

EngineModelContext.dev_mode = True


def add_api_url_arg(parser):
    parser.add_argument('--api_url', required=False, default=None,
                        help='Credmark API url. '
                        'Defaults to the standard API gateway. '
                        'You do not normally need to set this.')


def main():
    load_dotenv(find_dotenv(usecwd=True))

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Credmark developer tool')
    parser.add_argument('--log_level', default=None, required=False,
                        help='Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL')
    parser.add_argument('--model_path', default="models", required=False,
                        help='Semicolon separated paths to the model folders \
                            (or parent) or model python file. Defaults to models folder.')
    parser.add_argument('--manifest_file', type=str, default='models.json',
                        help='Name of the built manifest file. Defaults to models.json. '
                        '[Not required during development]')

    subparsers = parser.add_subparsers(title='Commands',
                                       description='Supported commands',
                                       help='additional help')

    parser_list = subparsers.add_parser(
        'list', help='List models in this repo', aliases=['list-models'])
    parser_list.add_argument('--manifests', action='store_true', default=False,
                             help="Show full manifests")
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

    parser_list = subparsers.add_parser(
        'describe', help='Show documentation for local and deployed models', aliases=['describe-models', 'man'])
    parser_list.add_argument('model-slug', nargs='?', default=None, type=str,
                             help='Slug or partial slug to describe.')
    add_api_url_arg(parser_list)
    parser_list.set_defaults(func=describe_models)

    parser_run = subparsers.add_parser('run', help='Run a model', aliases=['run-model'])
    parser_run.add_argument('-b', '--block_number', type=int, required=False, default=None,
                            help='Block number used for the context of the model run.'
                            ' If not specified, it is set to the latest block of the chain.')
    parser_run.add_argument('-c', '--chain_id', type=int, default=1, required=False,
                            help='Chain ID. Defaults to 1.')
    parser_run.add_argument('-i', '--input', required=False, default='{}',
                            help='Input JSON or '
                            'if value is "-" it will read input JSON from stdin.')
    parser_run.add_argument('-v', '--model_version', default=None, required=False,
                            help='Version of the model to run. Defaults to latest.')
    parser_run.add_argument('--provider_url_map', required=False, default=None,
                            help='JSON object of chain id to Web3 provider HTTP URL. '
                            'Overrides settings in env vars.')
    add_api_url_arg(parser_run)
    parser_run.add_argument('--run_id', help=argparse.SUPPRESS, required=False, default=None)
    parser_run.add_argument('--depth', help=argparse.SUPPRESS, type=int, required=False, default=0)
    parser_run.add_argument('model-slug', default='(missing model-slug arg)',
                            help='Slug for the model to run.')
    parser_run.set_defaults(func=run_model, depth=0)

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
    args.func(vars(args))


def config_logging(args, default_level='WARNING'):
    level = args['log_level']
    if not level:
        level = default_level
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=level)


def load_models(args, load_dev_models=False):
    manifest_file = args.get('manifest_file')
    model_path = args['model_path']
    model_paths = [model_path] if model_path is not None else None
    model_loader = ModelLoader(model_paths, manifest_file, load_dev_models)
    model_loader.log_errors()
    return model_loader


def describe_models(args, ):
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
    else:
        print_no_models_found(model_slug)


def print_no_models_found(model_slug):
    if model_slug:
        print(f'No models matching slug {model_slug}')
    else:
        print('No models found')


def list_models(args):
    config_logging(args)

    model_loader = load_models(args, True)
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


def list_deployed_models(args):
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
    for m in manifests:
        for i, v in m.items():
            if i == 'slug':
                sys.stdout.write(f'{v}\n')
                sys.stdout.write(f' - {i}: {v}\n')
            else:
                if not describe_schemas:
                    sys.stdout.write(f' - {i}: {v}\n')
                else:
                    if i == 'input':
                        input_tree = dto_schema_viz(
                            v, v.get('title', 'Object'), v, 0, 'tree', only_required=False, tag='top', limit=10)
                        input_examples = dto_schema_viz(
                            v, v.get('title', 'Object'), v, 0, 'example', only_required=False, tag='top', limit=10)

                        print(' - input schema (* for required field):')
                        print_tree(input_tree, '   ', sys.stdout.write)

                        print(' - input example:')
                        print_example(input_examples, '   ', sys.stdout.write)

                    elif i == 'output':
                        output_tree = dto_schema_viz(
                            v, v.get('title', 'Object'), v, 0, 'tree', only_required=False, tag='top', limit=1)
                        output_examples = dto_schema_viz(
                            v, v.get('title', 'Object'), v, 0, 'example', only_required=True, tag='top', limit=1)

                        print(' - output schema (* for required field):')
                        print_tree(output_tree, '   ', sys.stdout.write)

                        print(' - output example:')
                        print_example(output_examples, '   ', sys.stdout.write)

                    elif i == 'error':
                        codes = extract_error_codes_and_descriptions(v)
                        print(' - errors:')
                        if len(codes) > 0:
                            for ct in codes:
                                print(f'   {ct[0]}')
                                print(f'     codes={ct[1]}')
                                print(f'     {ct[2]}')
                            title = v.get('title', 'Error')
                            output_tree = dto_schema_viz(
                                v, title, v, 0, 'tree', only_required=False, tag='top', limit=1)
                            output_examples = dto_schema_viz(
                                v, title, v, 0, 'example', only_required=False, tag='top', limit=1)
                            print(' - error schema:')
                            print_tree(output_tree, '   ', sys.stdout.write)
                        else:
                            print('   No defined errors')

                    else:
                        sys.stdout.write(f' - {i}: {v}\n')

        sys.stdout.write('\n')


def write_manifest_file(args):
    config_logging(args, 'INFO')
    model_loader = load_models(args)
    model_loader.write_manifest_file()
    sys.exit(0)


def remove_manifest_file(args):
    config_logging(args)
    manifest_file = args.get('manifest_file')
    ModelLoader.remove_manifest_file(manifest_file)
    sys.exit(0)


def run_model(args):
    exit_code = 0

    try:
        config_logging(args, 'INFO')

        chain_to_provider_url = None
        providers_json = args['provider_url_map']

        # if arg is provided, it overrides any providers env vars
        if providers_json is not None:
            try:
                chain_to_provider_url = json.loads(providers_json)
            except Exception as err:
                logger.error(f'Error parsing JSON in arg provider_url_map: {err}')
        else:
            try:
                chain_to_provider_url = Web3Registry.load_providers_from_env()
            except Exception as err:
                logger.error(f'{err}')

        model_loader = load_models(args, load_dev_models=not args.get(
            'run_id'))  # we assume developer will not pass a run_id

        chain_id: int = args['chain_id']
        block_number: Union[int, None] = args['block_number']
        model_slug: str = args['model-slug']
        model_version: Union[str, None] = args['model_version']
        api_url: Union[str, None] = args['api_url']
        run_id: Union[str, None] = args['run_id']
        depth: int = args['depth']

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
            depth=depth)

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
        json.dump(msg, sys.stdout)
        exit_code = 1
    finally:
        sys.stdout.write('\n')
        sys.stdout.flush()

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
