import codecs
from emojicodecs.encodings import codec_factory


Codec = codec_factory("x_sjis_emoji_none", {}, "cp932")

def getregentry():
    return codecs.CodecInfo(
        name="x_sjis_emoji_none",
        encode=Codec().encode,
        decode=Codec().decode)