
from typing import (
    Dict,
    Any,
    List,
    TypedDict,
    Union,
)

import networkx as nx


class GraphResult(TypedDict):
    result: Dict[str, Any]
    dsk: Union[dict, nx.DiGraph]
    deps: Dict[str, str]
    futures: List[Any]


class GraphClient:
    client: str = 'sequence'

    def run_graph(self, dag: nx.DiGraph, outputs: List[Any]) -> List[Any]:
        dag_reversed = dag.reverse()

        pruned_t = None
        for node_out in outputs:
            t1 = nx.dfs_tree(dag_reversed, source=node_out).reverse()
            if pruned_t is None:
                pruned_t = t1
            else:
                pruned_t = nx.compose(pruned_t, t1)

        sorted_nodes = nx.algorithms.topological_sort(pruned_t)
        dep_nodes = {}
        pool_of_exec = []
        completed_node = set()
        exec_strategy = []
        for node_exec in list(sorted_nodes):
            es = nx.edges(dag_reversed, [node_exec])
            if es is not None:
                node_deps = [d[1] for d in es]
            else:
                node_deps = []
            dep_nodes[node_exec] = dep_nodes.get(node_exec, [])
            dep_nodes[node_exec].extend(node_deps)

            any_not_completed = len([dep for dep in node_deps if dep not in completed_node])
            if any_not_completed != 0:
                exec_strategy.append(('each', pool_of_exec))
                completed_node |= set([x[1] for x in pool_of_exec])
                pool_of_exec = []

            if len(node_deps) > 0:
                pool_of_exec.append(('compose', node_exec, node_deps))
            else:
                pool_of_exec.append(('single', node_exec))

        exec_strategy.append(('each', pool_of_exec))

        return exec_strategy
