import codecs
import re
from itertools import izip
from emojicodecs.mappings.fallback import text_fallback_map
from emojicodecs.emojidata import google_emoji_re


#google_emoji_re = re.compile(
#    (u'\udbb8[\udc00-\udc5b\udd90-\udde3\udf20-\udf69]|'
#     u'\udbb9[\udcb0-\udd53\udfd0-\udfff]|'
#     u'\udbba[\udc00-\udc3c\udd60-\udd88\udef0-\udfa2]|'
#     u'\udbbb[\ude10-\ude33\ude40-\ude4a\ude70-\ude7d\udea0]'))

def codec_factory(encoding, decoding_map, base_encoding):
    base_codec = codecs.lookup(base_encoding)
    encoding_map = dict(izip(decoding_map.itervalues(),
                             decoding_map.iterkeys()))
    emoji_re = re.compile(u"|".join(decoding_map.iterkeys()))

    class _Codec(codecs.Codec):
        def encode(self, input, errors='strict'):
            error = codecs.lookup_error(errors)
            def repl(match):
                start, end = match.span()
                return encoding_map.get(match.group()) or \
                       error(UnicodeEncodeError(encoding, input, start, end, 
                                                "undefined conversion emoji"))[0]
            output = google_emoji_re.sub(repl, input)
            return (base_codec.encode(output, errors)[0], len(input))

        def decode(self, input, errors='strict'):
            output, length = base_codec.decode(input, errors)
            output = emoji_re.sub(lambda m: decoding_map[m.group()], output)
            return (output, length)

    return _Codec
