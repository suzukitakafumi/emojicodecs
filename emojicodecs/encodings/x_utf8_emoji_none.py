import codecs
from emojicodecs.encodings import codec_factory


Codec = codec_factory("x_utf8_emoji_none", {}, {}, "utf_8")

def getregentry():
    return codecs.CodecInfo(
        name="x_utf8_emoji_none",
        encode=Codec().encode,
        decode=Codec().decode)
