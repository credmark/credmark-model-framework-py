import inspect

from typing import (
    TypeVar,
    Generic,
    Tuple,
    List,
    Any,
    Dict,
)

import networkx as nx
import matplotlib.pyplot as plt
import dask.distributed as dask_dist

import uuid

T = TypeVar('TaskType')


def call(func, *args, **kwargs):
    return func(*args, **kwargs)


def depend_on(func, skip_n, *args, **kwargs):
    """
    skip_n means it depends on the last n-task to finish but skip to get their inputs
    """

    assert skip_n > -1
    if skip_n == 0:
        return call(func, *args, **kwargs)
    else:
        return func(*args[:(-skip_n)], **kwargs)


def depend_all(*_args, **_kwargs):
    return depend_on(lambda: True, len(_args) + len(_kwargs))


class ModelTask():
    # TODO
    pass


class Task(Generic[T]):
    """
    input is a tuple of value input, task inputs
    """

    def __init__(self, name, f, input: Tuple[List[Any], List['Task[T]']] = ([], [])):
        self._task_name = name
        self._uuid_name = f.__name__ + '-' + str(uuid.uuid4())
        self._f = f
        self._args, self._deps = input
        f_args = inspect.getfullargspec(f).args
        f_args_defaults = inspect.getfullargspec(f).defaults
        deduct = 1 if inspect.ismethod(
            f) else 0 + 0 if f_args_defaults is None else len(f_args_defaults)

        assert isinstance(self._args, list) and isinstance(self._deps, list)
        if len(f_args) - deduct > len(self._args) + len(self._deps):
            raise ValueError(
                f'Input function\'s required arguments ({len(f_args), f_args}) is longer than the input ({len(input), input})')
        self._f_args = f_args

    @property
    def task_name(self):
        return self._task_name

    @property
    def uuid_name(self):
        return self._uuid_name

    def __call__(self):
        if len(self._deps) == 0:
            return (call, self._f, *self._args)
        else:
            return (depend_on, self._f, len(self._args) + len(self._deps) - len(self._f_args), *self._args, *[t.uuid_name for t in self._deps])


class Pipe():
    def __init__(self, *ts):
        self._dag = nx.DiGraph()
        self._graph = {}
        self._tasks = []
        self._task_names = {}
        self._uuid_names = {}
        self.extend(ts)

    def add(self, t):
        self.extend([t])

    def extend(self, ts):
        self._tasks.extend(ts)
        for t in ts:
            if t.task_name in self._uuid_names:
                raise ValueError(
                    f'There is already a task of the same name {t.task_name} in the pipe.')
            self._uuid_names[t.task_name] = t.uuid_name
            self._task_names[t.uuid_name] = t.task_name
            self._graph[t.uuid_name] = t()

            self._dag.add_nodes_from([(t.uuid_name, {'call': t()})])
            # d -> t
            self._dag.add_edges_from([(d.uuid_name, t.uuid_name) for d in t.deps])

        assert nx.is_directed_acyclic_graph(self._dag)

    @property
    def graph(self):
        return self._graph

    def draw(self):
        nx.draw(nx.relabel_nodes(self._dag, self._task_names), with_labels=True, font_weight='bold')
        plt.show()

    def run(self, cluster: Cluster, output: List[str]):
        new_output = [self._uuid_names[v] for v in output]
        ret = cluster.run_graph(self.graph, new_output)
        res_dict = ret['result']
        new_dict = {(self._task_names.get(uuid_name, uuid_name))                    : v for (uuid_name, v) in res_dict.items()}
        return new_dict

    def run_seq(self, output: List[str]):
        new_output = [self._uuid_names[v] for v in output]
        res_dict = cluster.run_graph(self.)
        new_dict = {(self._task_names.get(uuid_name, uuid_name))                    : v for (uuid_name, v) in res_dict.items()}

        return new_dict
