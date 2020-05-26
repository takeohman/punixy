#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import util.args

def simple_cat(arg_list):
    for _arg in arg_list:
        if _arg == '-':
            for _d in sys.stdin:
                sys.stdout.write(_d)
        elif os.path.isfile(_arg):
            with open(_arg, mode='r') as _fd:
                for _d in _fd.readlines():
                    sys.stdout.write(_d)
        else:
            print("{0}: {1}: No such file or directory".format(prog_name, _arg), file=sys.stderr)

# The index 0 of sys.argv list is name of this file.
prog_name = sys.argv[0]
opt_list, arg_list = util.args.parseArgs({"-n":False}, sys.argv[1:])

if len(arg_list)<=0:
    arg_list = ['-']

if len(opt_list) == 0:
    simple_cat(arg_list)
else:
    # TODO : adding options.
    for _arg in arg_list:
        if _arg == '-':
            for _d in sys.stdin:
                sys.stdout.write(_d)
        elif os.path.isfile(_arg):
            with open(_arg, mode='r') as _fd:
                for _d in _fd.readlines():
                    sys.stdout.write(_d)
        else:
            print("{0}: {1}: No such file or directory".format(prog_name, _arg), file=sys.stderr)

    