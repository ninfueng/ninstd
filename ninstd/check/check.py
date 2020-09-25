#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Collections of functions for asserting or checking.
Note that if the module is related to check, the priority is to put at here.
"""
import os
import sys
import shutil
from collections.abc import Iterable
from typing import Tuple

__all__ = [
    'is_imported',
    'is_dir',
    'is_exist',
    'is_iterable',
    'check_file_type',
    'is_defined',
    ]


def is_imported(module: str) -> bool:
    r"""Check the module is load or not.
    From: https://stackoverflow.com/questions/30483246/how-to-check-if-a-python-module-has-been-imported
    """
    if module in sys.modules:
        return True
    else:
        return False

def is_dir(directory: str) -> bool:
    r"""Return True if that directory is dir.
    """
    return os.path.isdir(os.path.join(os.getcwd(), directory))


def is_exist(directory: str) -> bool:
    r"""Return True if that directory is dir.
    """
    return os.path.exists(os.path.join(os.getcwd(), directory))

def is_iterable(var) -> bool:
    return isinstance(var, Iterable)


def is_all_type(instance: type, *variables) -> bool:
    r"""Return True, if all type of `list_var is `instance`.
    """
    return all(list(map(lambda x: isinstance(x, instance), variables)))


def check_type_args(*args: str, type: str) -> Tuple[list, bool]:
    r"""Assert that all args has same type as type.
    """
    check_list: list = []
    for arg in args:
        check_list.append(isinstance(arg, type))
    return check_list, all(check_list)


def check_file_type(directory: str, suffix: str) -> bool:
    r"""Split a file type from directory and check that is same as file_type or not.
    """
    assert isinstance(directory, str)
    assert isinstance(suffix, str)
    return suffix == directory.split('.')[-1]


def is_defined(var: str) -> bool:
    r"""Checking that this variable is defined or not.
    """
    isinstance(var, str)
    return str(var) in locals() or var in globals
