import wave
import struct


def chip_and_dale(number):
    sound1 = wave.open('in.wav', 'rb')
    sound2 = wave.open('out.wav', 'wb')
    sound2.setparams(sound1.getparams())
    frames1 = struct.unpack('<' + str(sound1.getnframes()) + 'h', sound1.readframes(sound1.getnframes()))
    frames2 = frames1[::number]
    frames2 = struct.pack('<' + str(len(frames2)) + 'h', *frames2)
    sound2.writeframes(frames2)
    sound1.close()
    sound2.close()


chip_and_dale(2)
