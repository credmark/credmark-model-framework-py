from itertools import product


def combine_dict(dicts):
    dd = {}
    for d in dicts:
        dd |= d
    return dd


def cross_examples(*x, limit=10):
    return [combine_dict(ds) for ds in product(*x)][:limit]


#  -> Union[Iterable[Tuple[Any, Any, Any]], Iterable[Dict[str, str]]]
def dto_schema_viz(head_node,  # pylint: disable=too-many-arguments,too-many-locals,too-many-return-statements,too-many-branches,too-many-statements
                   var_name, node, n_iter, ret_type,
                   only_required, tag, limit=10):
    assert ret_type in ['tree', 'example']
    # print(var_name, tag, ret_type, only_required)

    try:  # pylint: disable=too-many-nested-blocks
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
                if ret_type == 'example' and ('examples' in node or 'example' in node):
                    # return [{var_name: v} for v in node.get('examples', node.get('example'))]
                    return node.get('examples', node.get('example'))[:limit]

                # DTO without example
                if ret_type == 'tree':
                    ret = [(n_iter, var_name, node['type'])]
                else:
                    ret = [{}]

                if 'properties' in node and len(node['properties']) > 0:
                    props = node['properties']
                    required = node['required'] if 'required' in node else list(props.keys())
                    for prop_name, prop_item in props.items():
                        if only_required:
                            if prop_name not in required:
                                break

                        drill_ret = dto_schema_viz(
                            head_node, prop_name, prop_item,
                            n_iter + 1, ret_type, only_required, 'prop', limit)

                        if ret_type == 'tree':
                            if len(ret) == 1:
                                # For generic dict, return node['type'] which is "object".
                                # For non-generic object type, return the object name.
                                title_or_object = node['title'] if 'title' in node else node['type']
                                ret = [(n_iter, var_name, title_or_object +
                                        ('(*)' if prop_name in required else ''))]

                            ret.extend(drill_ret)

                        elif ret_type == 'example':
                            if ret == [{var_name: node['type']}]:
                                ret = drill_ret
                            else:
                                ret = cross_examples(ret, drill_ret, limit=limit)

                return ret

            if node['type'] == 'array':
                # array of object
                if '$ref' in node['items']:
                    ref = node['items']['$ref'].split('/')
                    definition_node = head_node[ref[1]][ref[2]]
                    ret = dto_schema_viz(head_node, var_name,
                                         definition_node, n_iter, ret_type,
                                         only_required, 'array_ref', limit)
                    if ret_type == 'tree':
                        ret[0] = (*ret[0][:-1], f'List[{ref[2]}]')
                        return ret
                    return [{var_name: [x]} for x in ret][:limit]

                # array of other types
                array_type = node['items']['type'] if 'type' in node['items'] else 'Any'
                if 'items' in node['items']:
                    array_type = ','.join([item['type'] for item in node['items']['items']])
                    array_type = f'({array_type})'
                if ret_type == 'tree':
                    return [(n_iter, var_name, f'List[{array_type}]')]
                return [{var_name: f'[{array_type}]'}]

            # ['type'] != 'array'
            # ordinary type
            type_desc = node["type"]
            if 'enum' in node:
                q = "'" if type_desc == 'string' else ''
                vals = f"{q},{q}".join(node["enum"])
                type_desc = f'{type_desc} [{q}{vals}{q}]'

            if ret_type == 'tree':
                return [(n_iter, var_name, type_desc)]
            return [{var_name: type_desc}]

        # Various Union type
        elif 'anyOf' in node or 'allOf' in node or 'oneOf' in node:
            ret = []
            of_node = node.get('anyOf', node.get('allOf', node.get('oneOf')))
            for item in of_node:
                drill_ret = dto_schema_viz(head_node, var_name, item,
                                           n_iter, ret_type, only_required,
                                           'union', limit)

                if ret_type == 'tree':
                    if len(ret) == 0:
                        ret = drill_ret
                    else:
                        ret[0] = (ret[0][0], ret[0][1], ret[0][2] +  # type: ignore
                                  ' | ' + drill_ret[0][2])
                elif ret_type == 'example':
                    if drill_ret == [{}]:
                        drill_ret = [{var_name: '{}'}]
                    if len(ret) == 0:
                        ret = drill_ret
                    else:
                        for r in ret:
                            for rr in drill_ret:
                                for k, v in rr.items():
                                    if k in r:
                                        r[var_name] = f'{r[var_name]} | {v}'
                                    else:
                                        r[var_name] = f'{r[var_name]} | {rr}'
            return ret

        # Object reference
        elif '$ref' in node:
            ref = node['$ref'].split('/')
            definition_node = head_node[ref[1]][ref[2]]
            if ret_type == 'example':
                # return [{var_name: dto_schema_viz(head_node, var_name, definition_node,
                #         n_iter, ret_type, only_required, 'ref', limit)}]
                return [{var_name: v} for v in
                        dto_schema_viz(head_node, var_name, definition_node,
                        n_iter, ret_type, only_required, 'ref', limit)][:limit]
            return dto_schema_viz(head_node, var_name, definition_node,
                                  n_iter, ret_type, only_required, 'ref', limit)

        else:
            if ret_type == 'tree':
                return [(n_iter, var_name, 'object')]
            return [{var_name: 'object'}]

    except Exception as err:
        raise ValueError(f'Unknown schema node {var_name, node, err, tag}')


def print_tree(tree, prefix, print_func):
    leaf = '\u2514\u2500'  # '\N{Leafy Green}'
    if len(tree) > 0:
        if isinstance(tree, tuple):
            nn, cc, tt = tree
            if nn > 0:
                print_func(f'{prefix}{" "*(4*nn-2)}{leaf}{cc}({tt})\n')
            else:
                print_func(f'{prefix}{" "*(4*nn)}{cc}({tt})\n')
        elif isinstance(tree, list):
            for elem in tree:
                print_tree(elem, prefix, print_func)
        elif isinstance(tree, dict):
            for elem, value in tree.items():
                print_func(f'{prefix}{elem}: {print_tree(value, prefix, print_func)}\n')
        else:
            raise ValueError(tree)
    else:
        print_func(f'{prefix}(empty)\n')


def print_example(examples, prefix, print_func):
    if len(examples) > 0:
        for n, l in enumerate(examples):
            l_with_double_quote = l.__str__().replace("'", '"')
            print_func(f'{prefix}#{n+1:02d}: {l_with_double_quote}\n')
    else:
        print_func(f'{prefix}{{}}\n')
