"""Core function of ninstd.
"""
import sys
import multiprocessing
from functools import reduce
from typing import Iterable, Any

__all__ = [
    'reduce_sum', 
    'reduce_prod',
    'map_prod',
    'recur_getattr',
    'get_num_worker',
    'get_num_worker',
    'MININT',
    'MAXINT',
    'MINFLOAT',
    'MAXFLOAT',    
    ]

MININT: int = -sys.maxsize - 1
MAXINT: int = sys.maxsize
MINFLOAT: float = -sys.float_info.max
MAXFLOAT: float = sys.float_info.max


def reduce_sum(itertor: Iterable) -> Any:
    r"""Reduce by adding all element in iterator.
    """
    return reduce(lambda x, y: x + y, itertor) 


def reduce_prod(itertor: Iterable) -> Any:
    r"""Reduce by producting all element in iterator.
    """
    return reduce(lambda x, y: x*y, itertor)


def map_prod(x: Iterable, y: Iterable) -> list:
    r"""Product pair by pair from `itertor0` to `itertor1`.
    """
    assert len(x) == len(y)
    return list(map(lambda x, y: x*y, x, y))


def recur_getattr(cls, *attrs):
    r"""Instead of using getattr(getattr(class, 'attr1'), 'attr2')
    using this recur_getattr(class, 'attr1', 'attr2').
    """
    cls_attr = cls
    for attr in attrs:
        cls_attr = getattr(cls_attr, attr)
    return cls_attr


def get_num_worker() -> int:
    r"""Get number of cpu for putting into DataLoader or others.
    """
    return multiprocessing.cpu_count()
