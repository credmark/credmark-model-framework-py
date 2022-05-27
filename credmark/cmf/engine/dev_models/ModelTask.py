import inspect

from typing import (
    TypeVar,
    Generic,
    Tuple,
    List,
    Any,
)

import networkx as nx
import matplotlib.pyplot as plt

import uuid

TASKT = TypeVar('TASKT')


def depend_on(func, skip_n, *args):
    """
    skip_n means it depends on the last n-task to finish but skip to get their inputs
    """

    assert skip_n > -1
    if skip_n == 0:
        return func(*args)
    else:
        return func(*args[:(-skip_n)])


def depend_all(*_args):
    return depend_on(lambda: True, len(_args))


class ModelTask(Generic[TASKT]):
    """
    input is a tuple of value input, task inputs
    """

    def __init__(self, model_name, model_input, model_depend, return_type, block_number):
        self._model_name = model_name
        self._model_input = model_input
        self._model_depend = model_depend
        self._return_type = return_type
        self._block_number = block_number
        self._task_name = model_name + '-' + str(uuid.uuid4())

    @property
    def task_name(self):
        return self._task_name

    @property
    def depend(self):
        return self._model_depend

    def __call__(self):
        return {'model_name': self._model_name,
                'model_input': self._model_input,
                'model_return_type': self._return_type,
                'block_number': self._block_number}


class Pipe():
    def __init__(self, tasks: List[ModelTask]):
        self._dag = nx.DiGraph()
        self._graph = {}
        self._tasks = []
        self._task_names = {}
        self.extend(tasks)

    def add(self, task: ModelTask):
        self.extend([task])

    def extend(self, tasks: List[ModelTask]):
        self._tasks.extend(tasks)
        for t in tasks:
            self._graph[t.task_name] = t()
            self._dag.add_nodes_from([(t.task_name, {'call': t()})])
            # d -> t
            if t.depend is not None:
                self._dag.add_edges_from([(t.depend.task_name, t.task_name)])

        assert nx.is_directed_acyclic_graph(self._dag)

    @ property
    def graph(self):
        return self._graph

    @ property
    def dag(self):
        return self._dag

    def draw(self):
        nx.draw(nx.relabel_nodes(self._dag, self._task_names), with_labels=True, font_weight='bold')
        plt.show()

    def run(self, cluster, output: List[ModelTask]):
        new_output = [v.task_name for v in output]
        ret = cluster.run_graph(self.dag, new_output)
        return ret
