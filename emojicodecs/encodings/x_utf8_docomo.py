import codecs
from emojicodecs.encodings import codec_factory
from emojicodecs.mappings.docomo import decoding_map


Codec = codec_factory(
    "x_utf8_docomo",
    decoding_map,
    "utf_8")

def getregentry():
    return codecs.CodecInfo(
        name="x_utf8_docomo",
        encode=Codec().encode,
        decode=Codec().decode)
