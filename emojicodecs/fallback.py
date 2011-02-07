import sys
from emojicodecs import emojidata
from emojicodecs.mappings.fallback import text_fallback_map

GETA_MARK = u'\u3013'

_cache = {}

def _get_fallback_map(encoding):
    module_name = {"x_sjis_docomo": "docomo",
                   "x_utf8_docomo": "docomo"}.get(encoding, encoding)
    if module_name in _cache:
        return _cache[module_name]
    fallback_map = getattr(sys.modules["emojicodecs.mappings.%s" % module_name],
                           "fallback_map", {})
    _cache[module_name] = fallback_map
    return _cache[module_name]

def fallback(exc):
    if isinstance(exc, UnicodeEncodeError):
        emoji = exc.object[exc.start:exc.end]
        fb = _get_fallback_map(exc.encoding).get(emoji) or \
             text_fallback_map.get(emoji) or GETA_MARK
        return (fb, exc.end)
    raise TypeError("can't handle %s" % exc.__name__)

def fallback_gmail(exc):
    if isinstance(exc, UnicodeEncodeError):
        emoji = exc.object[exc.start:exc.end]
        img = '<img src="http://mail.google.com/mail/e/%s" alt="%s" />' % \
            (repr(emoji)[-4:-1].upper(), emojidata.name(emoji))
        return (img, exc.end)
    raise TypeError("can't handle %s" % exc.__name__)

def fallback_typecast(exc):
    if isinstance(exc, UnicodeEncodeError):
        raise exc
    raise TypeError("can't handle %s" % exc.__name__)
