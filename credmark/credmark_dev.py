#! /usr/bin/env python3
import sys
import argparse
import logging
import json
import os
from typing import Union

from dotenv import load_dotenv
sys.path.append('.')
from .model.engine.context import EngineModelContext
from .model.engine.model_loader import ModelLoader
from .model.errors import MaxModelRunDepthError, MissingModelError, \
    ModelRunError, ModelRunRequestError

logger = logging.getLogger(__name__)

EngineModelContext.dev_mode = True


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Credmark developer tool')
    parser.add_argument('--log_level', default='INFO', required=False,
                        help='[OPTIONAL] Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL')
    parser.add_argument('--model_path', default="models", required=False,
                        help='[OPTIONAL] Semicolon separated paths to the model folders \
                            (or parent) or model python file. Defaults to models folder.')
    parser.add_argument('--manifest_file', type=str, default='models.yaml',
                        help='[OPTIONAL] Name of the built manifest file. Defaults to models.yaml. '
                        '(Not required during development.)')

    subparsers = parser.add_subparsers(title='Commands',
                                       description='Supported commands',
                                       help='additional help')

    parser_list = subparsers.add_parser('list', help='List models', aliases=['list-models'])
    parser_list.add_argument('--manifests', action='store_true', default=False)
    parser_list.add_argument('--json', action='store_true', default=False)
    parser_list.set_defaults(func=list_models)

    parser_list = subparsers.add_parser(
        'build', help='Build model manifest', aliases=['build-manifest'])
    parser_list.set_defaults(func=write_manifest_file)

    parser_list = subparsers.add_parser(
        'clean', help='Clean model manifest', aliases=['remove-manifest'])
    parser_list.set_defaults(func=remove_manifest_file)

    parser_run = subparsers.add_parser('run', help='Run a model', aliases=['run-model'])
    parser_run.add_argument('-b', '--block_number', type=int, required=True,
                            help='Default block number.')
    parser_run.add_argument('-c', '--chain_id', type=int, default=1, required=False,
                            help='[OPTIONAL] The chain ID. Defaults to 1.')
    parser_run.add_argument('-i', '--input', required=False, default=None,
                            help='[OPTIONAL] Input JSON. If missing, will read from stdin.')
    parser_run.add_argument('--provider_url_map', required=False, default=None,
                            help='[OPTIONAL] JSON object of chain id to Web3 provider HTTP URL')
    parser_run.add_argument('-v', '--model_version', default=None, required=False,
                            help='[OPTIONAL] Version of the model to run. Defaults to latest.')
    parser_run.add_argument('--api_url', required=False, default=None,
                            help='[OPTIONAL] Credmark API url')
    parser_run.add_argument('--run_id', help=argparse.SUPPRESS, required=False, default=None)
    parser_run.add_argument('--depth', help=argparse.SUPPRESS, type=int, required=False, default=0)
    parser_run.add_argument('model-slug', default='(missing model-slug arg)',
                            help='Slug for the model to run.')
    parser_run.set_defaults(func=run_model, depth=0)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    args.func(vars(args))


def config_logging(args):
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=args['log_level'])


def load_models(args):
    manifest_file = args.get('manifest_file')
    model_path = args['model_path']
    model_loader = ModelLoader([model_path] if model_path is not None else None, manifest_file)
    model_loader.log_errors()
    return model_loader


def list_models(args):
    config_logging(args)

    model_loader = load_models(args)
    json_output = args.get('json')

    if not json_output:
        sys.stdout.write('\nLoaded models:\n\n')

    if args.get('manifests'):
        manifests = model_loader.loaded_model_manifests()
        if json_output:
            json.dump({'models': manifests}, sys.stdout)
        else:
            for m in manifests:
                for i, v in m.items():
                    sys.stdout.write(f' {i}: {v}\n')
                sys.stdout.write('\n')
    else:
        models = model_loader.loaded_model_version_lists()
        if json_output:
            json.dump(models, sys.stdout)
        else:
            for m, v in models.items():
                sys.stdout.write(f' - {m}: {v}\n')

    if not json_output:
        sys.stdout.write('\n')
        sys.stdout.write(
            f'{len(model_loader.errors)} errors, {len(model_loader.warnings)} warnings\n\n')
    sys.exit(0)


def write_manifest_file(args):
    config_logging(args)
    model_loader = load_models(args)
    model_loader.write_manifest_file()
    sys.exit(0)


def remove_manifest_file(args):
    config_logging(args)
    manifest_file = args.get('manifest_file')
    model_loader = load_models({'model_path': None, 'manifest_file': manifest_file})
    model_loader.remove_manifest_file()
    sys.exit(0)


def run_model(args):
    exit_code = 0

    try:
        config_logging(args)

        chain_to_provider_url = None
        providers_json = args['provider_url_map']

        breakpoint()

        if providers_json is None:
            providers_json = os.environ.get('CREDMARK_WEB3_PROVIDERS')
        if providers_json:
            try:
                chain_to_provider_url = json.loads(providers_json)
            except Exception as err:
                logger.error(f'Error parsing JSON in env var CREDMARK_WEB3_PROVIDERS: {err}')

        model_loader = load_models(args)

        chain_id: int = args['chain_id']
        block_number: int = args['block_number']
        model_slug: str = args['model-slug']
        model_version: Union[str, None] = args['model_version']
        api_url: Union[str, None] = args['api_url']
        run_id: Union[str, None] = args['run_id']
        depth: int = args['depth']

        if args['input']:
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
        json.dump(result, sys.stdout)

    except (MaxModelRunDepthError, MissingModelError, ModelRunError) as e:
        msg = {
            "statusCode": 500,
            "error": "Model run error",
            "message": str(e)
        }
        json.dump(msg, sys.stdout)
        exit_code = 1
    except ModelRunRequestError as e:
        sys.stdout.write(str(e))
        exit_code = 1
    except Exception as e:
        logger.exception('Run error')
        msg = {
            "statusCode": 500,
            "error": "Model run error",
            "message": str(e)
        }
        json.dump(msg, sys.stdout)
        exit_code = 1
    finally:
        sys.stdout.write('\n')
        sys.stdout.flush()

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
