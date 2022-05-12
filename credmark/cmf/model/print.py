
from credmark.dto.dto_error_schema import extract_error_codes_and_descriptions
from credmark.dto.dto_schema import dto_schema_viz, print_example, print_tree


def print_manifest(manifest, stream):
    for i, v in manifest.items():
        if i == 'slug':
            stream.write(f'{v}\n')
            stream.write(f' - {i}: {v}\n')
        else:
            stream.write(f' - {i}: {v}\n')


def print_manifest_description(manifest, stream):
    for i, v in manifest.items():
        if i == 'slug':
            stream.write(f'{v}\n')
            stream.write(f' - {i}: {v}\n')
        elif i == 'input':
            input_tree = dto_schema_viz(
                v, v.get('title', 'Object'), v, 0, 'tree',
                only_required=False, tag='top', limit=10)
            input_examples = dto_schema_viz(
                v, v.get('title', 'Object'), v, 0, 'example',
                only_required=False, tag='top', limit=10)

            print(' - input schema (* for required field):')
            print_tree(input_tree, '   ', stream.write)

            print(' - input example:')
            print_example(input_examples, '   ', stream.write)

        elif i == 'output':
            output_tree = dto_schema_viz(
                v, v.get('title', 'Object'), v, 0, 'tree',
                only_required=False, tag='top', limit=1)
            output_examples = dto_schema_viz(
                v, v.get('title', 'Object'), v, 0, 'example',
                only_required=True, tag='top', limit=1)

            print(' - output schema (* for required field):')
            print_tree(output_tree, '   ', stream.write)

            print(' - output example:')
            print_example(output_examples, '   ', stream.write)

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
                print_tree(output_tree, '   ', stream.write)
            else:
                print('   No defined errors')

        else:
            stream.write(f' - {i}: {v}\n')
