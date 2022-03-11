#! /usr/bin/env python3
import sys
import argparse
import logging
import json
from typing import (
    Union,
)

from dotenv import load_dotenv, find_dotenv
sys.path.append('.')
from .model.engine.context import EngineModelContext
from .model.engine.model_loader import ModelLoader
from .model.errors import MaxModelRunDepthError, MissingModelError, \
    ModelRunError, ModelRunRequestError
from .model.web3 import Web3Registry
from .model.encoder import json_dump
from .types.dto import cross_examples

logger = logging.getLogger(__name__)

EngineModelContext.dev_mode = True


def main():
    load_dotenv(find_dotenv(usecwd=True))

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
        'describe', help='describe models', aliases=['describe-models'])
    parser_list.add_argument('model-slug', nargs='?', default=None, type=str,
                             help='Slug to describe.')
    parser_list.set_defaults(func=describe_models)

    parser_list = subparsers.add_parser(
        'build', help='Build model manifest', aliases=['build-manifest'])
    parser_list.set_defaults(func=write_manifest_file)

    parser_list = subparsers.add_parser(
        'clean', help='Clean model manifest', aliases=['remove-manifest'])
    parser_list.set_defaults(func=remove_manifest_file)

    parser_run = subparsers.add_parser('run', help='Run a model', aliases=['run-model'])
    parser_run.add_argument('-b', '--block_number', type=int, required=False, default=None,
                            help='Block number used for the context of the model run.'
                            ' If not specified, it is set to the latest block of the chain.')
    parser_run.add_argument('-c', '--chain_id', type=int, default=1, required=False,
                            help='[OPTIONAL] The chain ID. Defaults to 1.')
    parser_run.add_argument('-i', '--input', required=False, default='{}',
                            help='[OPTIONAL] Input JSON or '
                            'if value is "-" it will read input JSON from stdin.')
    parser_run.add_argument('-v', '--model_version', default=None, required=False,
                            help='[OPTIONAL] Version of the model to run. Defaults to latest.')
    parser_run.add_argument('--provider_url_map', required=False, default=None,
                            help='[OPTIONAL] JSON object of chain id to Web3 provider HTTP URL. '
                            'Overrides settings in env vars.')
    parser_run.add_argument('--api_url', required=False, default=None,
                            help='[OPTIONAL] Credmark API url. '
                            'Defaults to the standard API gateway. '
                            'You do not normally need to set this.')
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
    load_dev_models = not args.get('run_id')  # we assume developer will not pass a run_id
    model_loader = ModelLoader(
        [model_path] if model_path is not None else None, manifest_file, load_dev_models)
    model_loader.log_errors()
    return model_loader


def drill_definition(head_node, var_name, node, n_iter, ret_type):
    assert ret_type in ['tree', 'example']
    try:
        # 1. DTO/dict
        # 1.1 DTO with example
        # 1.2 DTO without example
        # 1.3 dict
        # 2. Array
        # 2.1 DTO
        # 2.2 other
        # 3. Union
        # 4. DTO Reference

        if 'type' in node:
            if node['type'] == 'object':
                # DTO with example
                if ret_type == 'example' and 'examples' in node:
                    return node["examples"]
                # DTO without example
                if 'properties' in node:
                    props = node['properties']
                    required = node['required'] if 'required' in node else list(props.keys())
                    ret = []
                    for prop_name, prop_item in props.items():
                        if prop_name in required:
                            if ret_type == 'tree':
                                ret.extend(drill_definition(
                                    head_node, prop_name, prop_item, n_iter + 1, ret_type))
                            elif ret_type == 'example':
                                drill_ret = drill_definition(
                                    head_node, prop_name, prop_item, n_iter + 1, ret_type)
                                if len(ret) == 0:
                                    ret = drill_ret
                                else:
                                    ret = cross_examples(ret, drill_ret, limit=10)
                    return ret

                # dict
                if ret_type == 'tree':
                    return [(n_iter, 'dict()')]
                return [{var_name: {}}]

            if node['type'] == 'array':
                # array of object
                if '$ref' in node['items']:
                    ref = node['items']['$ref'].split('/')
                    definition_node = head_node[ref[1]][ref[2]]
                    ret = drill_definition(head_node, var_name,
                                           definition_node, n_iter + 1, ret_type)
                    if ret_type == 'tree':
                        return [(n_iter, f'List[{var_name}]')] + ret
                    return [{var_name: [ret]}]

                # array of other type
                if 'type' in node['items']:
                    if ret_type == 'tree':
                        return [(n_iter, f'List[{node["items"]["type"]}]')]
                    return [{var_name: node["items"]['type']}]
                else:
                    raise ValueError(f'Unhandled {node}')
            else:  # ['type'] != 'array'
                # ordinary type
                if ret_type == 'tree':
                    return [(n_iter, node["type"])]
                return [{var_name: node["type"]}]

        # Various Union type
        elif 'anyOf' in node or 'allOf' in node or 'oneOf' in node:
            ret = []
            of_node = node.get('anyOf', node.get('allOf', node.get('oneOf')))
            for item in of_node:
                if ret_type == 'tree':
                    ret.extend(drill_definition(
                        head_node, var_name, item, n_iter + 1, ret_type))
                elif ret_type == 'example':
                    drill_ret = drill_definition(
                        head_node, var_name, item, n_iter + 1, ret_type)
                    if len(ret) == 0:
                        ret = drill_ret
                    else:
                        ret = cross_examples(ret, drill_ret, limit=10)
            return ret

        # Object reference
        elif '$ref' in node:
            ref = node['$ref'].split('/')
            definition_node = head_node[ref[1]][ref[2]]
            breakpoint()
            return drill_definition(head_node, var_name, definition_node, n_iter + 1, ret_type)
        else:
            raise ValueError(f'Unhandled {node}')
    except Exception as err:
        raise ValueError(f'Unknown schema node {var_name, node, err}')


def print_tree(v):
    if isinstance(v, tuple):
        nn, cc = v
        print(f'{" "*4*nn}{cc}')
    elif isinstance(v, list):
        for x in v:
            print_tree(x)
    elif isinstance(v, dict):
        for kk, vv in v.items():
            print(f'{kk}: {print_tree(vv)}')
        raise ValueError(v)


def describe_models(args, ):
    args['manifests'] = True
    args['json'] = False
    list_models(args)


def list_models(args):
    config_logging(args)

    model_loader = load_models(args)
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
            # add more tree-descriptive
            for m in manifests:
                # breakpoint()
                try:
                    print(m['slug'], ":")
                    print(m['input'], ":")
                    print()

                    head_node = m['input']
                    tree_schema = drill_definition(
                        head_node, head_node['title'], head_node, 0, 'tree')
                    examples = drill_definition(
                        head_node, head_node['title'], head_node, 0, 'example')

                    print('example:')
                    if len(examples) > 0:
                        for n, l in enumerate(examples):
                            print(f'#{n+1:02d}: {l}')
                    else:
                        print('Nil')

                    print('tree_schema:')
                    if len(tree_schema) > 0:
                        print_tree(tree_schema)
                    else:
                        print('Nil')
                    print(tree_schema)

                except Exception as err:
                    raise err

                # for i, v in m.items():
                #    sys.stdout.write(f' {i}: {v}\n')
                sys.stdout.write('\n')
    else:
        models = model_loader.loaded_model_version_lists()
        if model_slug is not None:
            models = {k: v for k, v in models.items() if model_slug in k}

        if json_output:
            json.dump(models, sys.stdout)
        else:
            slugs = list(models.keys())
            slugs.sort()
            for s in slugs:
                sys.stdout.write(f' - {s}: {models[s]}\n')

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

        model_loader = load_models(args)

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

        json_dump(result, sys.stdout)

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
