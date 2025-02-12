# -*- coding: utf-8 -*-

import typing as t
from abc import ABC, abstractmethod


class AbstractNode(ABC):
    """
    Abstract class for all nodes.
    """

    @property
    @abstractmethod
    def neighbors(self: t.Self) -> t.Iterable["AbstractNode"]:
        """
        Return the neighbors of the node.

        :return: the neighbors of the node
        """


class AbstractAlgorithm[Node: AbstractNode](ABC):
    """
    Abstract class for all algorithms.
    """

    @abstractmethod
    def run(self: t.Self, s: Node, k: int):
        """
        Run the algorithm.

        :param k: number of agents
        """


__all__ = ["AbstractNode", "AbstractAlgorithm"]
