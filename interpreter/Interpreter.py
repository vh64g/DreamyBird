from logger.Logger import Logger
from interpreter.LineHandler import LineHandler


def read_file(file_path: str):
    with open(file_path, 'r') as file:
        return file.readlines()


class DreamyBirdyInterpreter:
    def __init__(self):
        self.code = read_file('data/db3code/code.db3')
        self.line_handler = LineHandler()
        self.logger = Logger('data/log/', 'last.log', __name__)
        self.logger.console('info', 'Interpreter Setup complete...', color='green')
        self.main()

    def main(self):
        for line in self.code:
            self.line_handler.set_line(line)
            handler_respo = self.line_handler.handle()
            if handler_respo == -1:
                self.logger.console('error', f'Error: In line {self.code.index(line)+1}')
                return -1