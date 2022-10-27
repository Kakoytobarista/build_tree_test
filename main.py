from pprint import pprint
from typing import Tuple, List


def to_tree(edges: List[Tuple]):
    nodes = {}
    for parent, child in edges:
        if parent not in nodes:
            nodes[parent] = dict()

        if child not in nodes:
            nodes[child] = dict()

        assert parent in nodes and child in nodes
        if child not in nodes[parent]:
            nodes[parent].update({child: nodes[child]})

    root = nodes[None]
    return root


if __name__ == "__main__":
    source = [
        (None, 'a'),
        (None, 'b'),
        (None, 'c'),
        ('a', 'a1'),
        ('a', 'a2'),
        ('a2', 'a21'),
        ('a2', 'a22'),
        ('b', 'b1'),
        ('b1', 'b11'),
        ('b11', 'b111'),
        ('b', 'b2'),
        ('c', 'c1'),
    ]
    expected = {
        'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
        'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
        'c': {'c1': {}},
    }
    pprint(to_tree(source))
    assert to_tree(source) == expected, "Error"

