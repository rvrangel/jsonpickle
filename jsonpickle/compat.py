from __future__ import absolute_import, division, unicode_literals
import sys
import types

PY_MAJOR = sys.version_info[0]
PY2 = PY_MAJOR == 2
PY3 = PY_MAJOR == 3

class_types = type,

if PY3:
    import queue
    string_types = (str,)
    numeric_types = (int, float)
    ustr = str
    from base64 import encodebytes, decodebytes
else:
    import Queue as queue
    string_types = (basestring,)
    numeric_types = (int, float, long)
    ustr = unicode
    from base64 import encodestring as encodebytes
    from base64 import decodestring as decodebytes
    class_types += types.ClassType,


def iterator(class_):
    if PY2 and hasattr(class_, '__next__'):
        class_.next = class_.__next__
    return class_
