#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


def parseArgs(allowed_opt_dict, arg_list):
    """
    Parse command line arguments


    Parameters:
    ----------
    allowed_opt_dict:dict
        allowd options
    arg_list:list
        command line parameters

    Returns
    ----------
    options: list
    params: list

    >>> parseArgs({"-c":True}, ['-', 'file1','-c', '2'])
    ([], ['-', 'file1', '-c', '2'])
    >>> parseArgs({'-c':True}, ['-c', '2'])
    ([('-c', '2', 0)], [])
    >>> parseArgs({'-c':True}, ['-c', '2', 'file1', 'file2'])
    ([('-c', '2', 0)], ['file1', 'file2'])
    >>> parseArgs({'-b':True, '-c':False}, ['-b', '3', '-c', '2'])
    ([('-b', '3', 0), ('-c', None, 0)], ['2'])
    >>> parseArgs({'-b':True, '-c':False}, ['-b', '3', '-d', '2'])
    ([('-b', '3', 0), ('-d', None, 1)], ['2'])
    >>> parseArgs({'-b':True, '-c':False}, ['-b', '-d', '2'])
    ([('-b', '-d', 1)], ['2'])

    """
    prev_opt = None
    opt_ended = False
    opt_list = []
    param_list = []
    param_cnt = len(arg_list)

    for _ix, _elm in enumerate(arg_list, 0):
        if not opt_ended and _elm.startswith('-') and len(_elm) > 1:
            # options
            if prev_opt and allowed_opt_dict[prev_opt]:
                opt_list.append((prev_opt, _elm, 1))
                prev_opt = None

            elif _elm in allowed_opt_dict:
                if allowed_opt_dict[_elm] is False:
                    opt_list.append((_elm, None, 0))
                    prev_opt = None
                else:
                    if _ix + 1 < param_cnt and arg_list[_ix + 1] not in allowed_opt_dict:
                        prev_opt = _elm
                    else:
                        opt_list.append((_elm, None, 1))
                        prev_opt = None
            else:
                opt_list.append((_elm, None, 1))
        else:
            if prev_opt is not None:
                # option's value
                if prev_opt in allowed_opt_dict and allowed_opt_dict[prev_opt] is True:
                    # if _elm in allowed_opt_dict:
                    #     opt_list.append((prev_opt, None, 1))
                    #     prev_opt = _elm
                    if _elm.startswith('-'):
                        opt_list.append((prev_opt, None, 1))
                        prev_opt = None
                    else:
                        opt_list.append((prev_opt, _elm, 0))
                        prev_opt = None
                else:
                    opt_list.append((prev_opt, _elm, 0))
                    prev_opt = None
            else:
                opt_ended = True
                # a parameter such as a file name.
                param_list.append(_elm)
    return opt_list, param_list

if __name__ == '__main__':
    import doctest
    doctest.testmod() 