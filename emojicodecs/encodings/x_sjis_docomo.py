import codecs
from emojicodecs.encodings import codec_factory
from emojicodecs.mappings.docomo import decoding_map


Codec = codec_factory(
    "x_sjis_docomo",
    decoding_map,
    "cp932")

def getregentry():
    return codecs.CodecInfo(
        name="x_sjis_docomo",
        encode=Codec().encode,
        decode=Codec().decode)
