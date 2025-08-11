"""
Copyright Wenyi Tang 2025

:Author: Wenyi Tang
:Email: wenyitang@outlook.com

Test builtin module imported as expected:
- Not a lazy object
- Can be pickled

Example::

    # config.py
    import os
    from sys import platform

    d = dict(thread=os.cpu_count())
    if platform == "win32":
        d.update(name="windows")
    else:
        d.update(name=platform.lower())

    # main.py
    cfg = Config.fromfile("config.py")
    # Do not import builtin module, because it can't be pickled.
    assert cfg.os is None
    # Builtin variable can be imported normally.
    assert cfg.platform == cfg.d.name
"""

import os.path as osp
import sys
from copy import deepcopy

import numpy as np

from mme.config import Config
from mme.config.lazy import LazyObject

data_path = osp.join(osp.dirname(osp.dirname(__file__)), "data/")


def test_import_builtin():
    cfg = Config.fromfile(
        osp.join(data_path, "config/lazy_module_config/test_mix_builtin.py")
    )
    assert cfg.path in ("a/b", "a\\b")
    assert cfg.name == "a/b"
    assert cfg.suffix == ".py"
    assert cfg.chained == [1, 2, 3, 4]
    assert cfg.existed is True
    assert cfg.cfgname == "test_mix_builtin.py"
    assert cfg.d.name == sys.platform.lower()
    assert not isinstance(cfg.np, LazyObject)  # cfg is not lazy
    assert cfg.np is np
    assert "os" not in cfg
    assert "osp" not in cfg
    # make sure cfg can be pickled
    deepcopy(cfg)
