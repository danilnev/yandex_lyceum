import wave
import struct


def pitch_and_toss():
    sound1 = wave.open('in.wav', 'rb')
    sound2 = wave.open('out.wav', 'wb')
    sound2.setparams(sound1.getparams())
    frames = struct.unpack('<' + str(sound1.getnframes()) + 'h', sound1.readframes(sound1.getnframes()))
    length = len(frames) // 4
    parts = [frames[length * 2: length * 3], frames[length * 3:], frames[:length], frames[length: length * 2]]
    frames = parts[0] + parts[1] + parts[2] + parts[3]
    frames = struct.pack('<' + str(len(frames)) + 'h', *frames)
    sound2.writeframes(frames)
    sound1.close()
    sound2.close()


pitch_and_toss()
