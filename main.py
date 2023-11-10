from logger.Logger import Logger
from interpreter.Interpreter import DreamyBirdyInterpreter
import time


class DreamyBirdy:
    def __init__(self):
        self.logger = Logger('data/log/', 'last.log', __name__)
        self.setup()
        self.main()

    def setup(self):
        self.logger.console('info', 'Setting up...')
        self.logger.test()
        self.logger.open()
        self.logger.write('-- DreamyBirdy v0.1 --\n -- ' + time.ctime() + ' --\n\n')
        self.logger.close()
        with open('data/messages/hello.txt', 'r') as file:
            self.logger.console('info', file.read())
        self.logger.console('info', 'Setting up complete.', color='green')

    def main(self):
        self.logger.console('info', 'Starting interpreter...')
        DreamyBirdyInterpreter()


if __name__ == '__main__':
    dbthree = DreamyBirdy()
