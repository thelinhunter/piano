from MIDIFileGenerator import Scales

class test:

    def __init__(self):
        self.name = 'test'
        self.test = Scales(200)

    def generator(self):
        self.test.c5(1)
        self.test.c5s(1)
        self.test.d5(1)
        self.test.d5s(1)
        self.test.e5(1)
        self.test.f5(1)
        self.test.f5s(1)
        self.test.g5(1)
        self.test.g5s(1)
        self.test.a5(1)
        self.test.a5s(1)
        self.test.b5(1)
        self.test.c6(1)

        with open(self.name, "wb") as output_file:
            self.test.get_midi().writeFile(output_file)
        return self.name