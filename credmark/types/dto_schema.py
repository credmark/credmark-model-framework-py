from itertools import product


def combine_dict(dicts):
    dd = {}
    for d in dicts:
        dd |= d
    return dd


def cross_examples(*x, limit=10):
    return [combine_dict(ds) for ds in product(*x)][:limit]


#  -> Union[Iterable[Tuple[Any, Any, Any]], Iterable[Dict[str, str]]]
def dto_schema_viz(head_node, var_name, node, n_iter, ret_type, limit=10):
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
                if ret_type == 'tree':
                    ret = [(n_iter, var_name, node['type'])]
                else:
                    ret = [{}]

                if 'properties' in node and len(node['properties']) > 0:
                    props = node['properties']
                    required = node['required'] if 'required' in node else list(props.keys())
                    for prop_name, prop_item in props.items():
                        if prop_name in required:
                            if ret_type == 'tree':
                                if len(ret) == 1:
                                    ret = [(n_iter, var_name, node['type'])]
                                drill_ret = dto_schema_viz(
                                    head_node, prop_name, prop_item, n_iter + 1, ret_type, limit)
                                ret.extend(drill_ret)
                            elif ret_type == 'example':
                                drill_ret = dto_schema_viz(
                                    head_node, prop_name, prop_item, n_iter + 1, ret_type, limit)
                                if len(ret) == 0:
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
                                         definition_node, n_iter, ret_type, limit)
                    if ret_type == 'tree':
                        ret[0] = (*ret[0][:-1], f'List[{ref[2]}]')
                        return ret
                    return [{var_name: [x]} for x in ret]

                # array of other type
                array_type = node['items']['type'] if 'type' in node['items'] else 'Any'
                if 'items' in node['items']:
                    array_type = ','.join([item['type'] for item in node['items']['items']])
                    array_type = f'({array_type})'
                if ret_type == 'tree':
                    return [(n_iter, var_name, f'List[{array_type}]')]
                return [{var_name: array_type}]

            # ['type'] != 'array'
            # ordinary type
            if ret_type == 'tree':
                return [(n_iter, var_name, node["type"])]
            return [{var_name: node["type"]}]

        # Various Union type
        elif 'anyOf' in node or 'allOf' in node or 'oneOf' in node:
            ret = []
            of_node = node.get('anyOf', node.get('allOf', node.get('oneOf')))
            for item in of_node:
                drill_ret = dto_schema_viz(
                    head_node, var_name, item, n_iter, ret_type, limit)

                if ret_type == 'tree':
                    if len(ret) == 0:
                        ret = drill_ret
                    else:
                        ret[0] = (ret[0][0], ret[0][1], ret[0][2] + ' | ' + drill_ret[0][2])
                elif ret_type == 'example':
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
            return dto_schema_viz(head_node, var_name, definition_node, n_iter, ret_type, limit)

        else:
            if ret_type == 'tree':
                return [(n_iter, var_name, 'object')]
            return [{var_name: 'object'}]
    except Exception as err:
        raise ValueError(f'Unknown schema node {var_name, node, err}')


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
            print_func(f'{prefix}#{n+1:02d}: {l}\n')
    else:
        print_func(f'{prefix}{{}}\n')