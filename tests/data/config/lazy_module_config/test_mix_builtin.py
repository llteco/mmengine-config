# Copyright (c) OpenMMLab. All rights reserved.
import os
import os.path as osp
from sys import platform
from functools import partial
from itertools import chain
from os.path import basename
from os.path import exists as ex
from os.path import splitext

import numpy as np

path = osp.join('a', 'b')
name, suffix = splitext('a/b.py')
chained = list(chain([1, 2], [3, 4]))
existed = ex(__file__)
cfgname = partial(basename, __file__)()
d = dict(thread=os.cpu_count())
if platform == "win32":
    d.update(name="win32")
else:
    d.update(name=platform.lower())
