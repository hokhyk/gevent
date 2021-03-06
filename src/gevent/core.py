# Copyright (c) 2009-2015 Denis Bilenko and gevent contributors. See LICENSE for details.
from __future__ import absolute_import

import os

from gevent._util import copy_globals

try:
    if os.environ.get('GEVENT_CORE_CFFI_ONLY'):
        raise ImportError("Not attempting corecext")

    from gevent.libev import corecext as _core
except ImportError:
    if os.environ.get('GEVENT_CORE_CEXT_ONLY'):
        raise

    # CFFI/PyPy
    lib = os.environ.get('GEVENT_CORE_CFFI_ONLY')
    if lib == 'libuv':
        from gevent.libuv import loop as _core
    else:
        try:
            from gevent.libev import corecffi as _core
        except ImportError:
            from gevent.libuv import loop as _core

copy_globals(_core, globals())

__all__ = _core.__all__ # pylint:disable=no-member
