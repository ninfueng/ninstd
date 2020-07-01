#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse


__all__ = ['str_to_bool']


def str_to_bool(string: str) -> None:
    """To make argparse able to parse a boolean input.
    Modified From: https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
    """
    assert isinstance(string)
    if string.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif string.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError(
            f'Your input: {string}, Boolean value expected.')

