import codecs
from emojicodecs.encodings import codec_factory
from emojicodecs.mappings.x_sjis_softbank import decoding_map


Codec = codec_factory(
    "x_sjis_softbank",
    decoding_map,
    "cp932")

def getregentry():
    return codecs.CodecInfo(
        name="x_sjis_softbank",
        encode=Codec().encode,
        decode=Codec().decode)