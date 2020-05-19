#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

arg_list = ['-']
# The index 0 of sys.argv list is name of this file.
prog_name = sys.argv[0]
if len(sys.argv) > 1:
    arg_list = sys.argv[1:]
    
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
    