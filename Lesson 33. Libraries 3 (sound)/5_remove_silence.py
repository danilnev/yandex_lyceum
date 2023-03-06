import wave
import struct


def break_the_silence():
    sound1 = wave.open('in.wav', 'rb')
    sound2 = wave.open('out.wav', 'wb')
    sound2.setparams(sound1.getparams())
    frames = struct.unpack('<' + str(sound1.getnframes()) + 'h', sound1.readframes(sound1.getnframes()))
    frames = list(filter(lambda x: not (-5 <= x <= 5), frames))
    frames = struct.pack('<' + str(len(frames)) + 'h', *frames)
    sound2.writeframes(frames)
    sound1.close()
    sound2.close()


break_the_silence()
