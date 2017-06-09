from api_client import Generator
import struct
import wave
# import random

DURATION = 3
RATE = 44100
SAMPLE_SIZE = 1
SAMPLE_LIM = 32767

class WhiteNoiseGenerator(Generator):
    def _parser(self):
        parser = super(WhiteNoiseGenerator, self)._parser()
        parser.add_argument('-o', '--output', help='Filename of output file, e.g. foo.wav', default='noise.wav')
        return parser

    def generate(self):
        wav = wave.open(self.args.output, 'w')
        wav.setparams((1, SAMPLE_SIZE, RATE, 0, 'NONE', 'not compressed'))

        # testing using python random library
        # for i in range(0, RATE * DURATION):
            # value = random.randint(-32767, 32767)
            # packed_value = struct.pack('h', value)
            # wav.writeframes(packed_value)
        
        data = self._random_ints(-SAMPLE_LIM, SAMPLE_LIM, RATE * DURATION)
        for value in data:
            packed_value = struct.pack('h', value)
            wav.writeframes(packed_value)
        wav.close()

if __name__ == '__main__':
    WhiteNoiseGenerator().generate()