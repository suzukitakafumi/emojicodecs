import codecs
from emojicodecs.fallback import fallback, fallback_gmail, fallback_typecast


_cache = {}

_aliases = {}

def search_function(encoding):
    encoding = encoding.replace("-", "_")
    if encoding in _cache:
        return _cache[encoding]
    try:
        module = __import__("emojicodecs.encodings.%s" % encoding,
                            globals=globals(),
                            locals=locals(),
                            fromlist=["*"],
                            level=-1)
    except ImportError:
        return None
    _cache[encoding] = module.getregentry()
    return _cache.get(encoding, None)

codecs.register(search_function)
codecs.register_error('fallback', fallback)
codecs.register_error('fallback_gmail', fallback_gmail)
codecs.register_error('fallback_typecast', fallback_typecast)
