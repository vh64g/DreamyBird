from interpreter.keys.vars.VarHandler import VarHandler
from logger.Logger import Logger


class LineHandler:
    def __init__(self):
        self.line = ''
        self.logger = Logger('data/log/', 'last.log', __name__)
        self.var_handler = VarHandler()

    def set_line(self, line: str):
        self.line = line
        if self.line[-1] == '\n': self.line = self.line[:-1]
        self.logger.console('info', f'New Line set to {self.line if self.line != "" else "Empty Line"}')

    def count_exclamation_marks(self):
        count = 0
        qm_count = 0
        em_started = False
        for char in self.line:
            if char == ('"' or "'"): qm_count += 1
            if char == '!' and (qm_count % 2 == 0):
                if not em_started: em_started = True
                count += 1
            elif char != '!' and char != '\n':
                if em_started: return -1
        return count if (count != 0 and self.line.__len__()>0) else -1

    def handle(self):
        # Return 0 if line is empty
        if self.line == '\n' or self.line == '':
            self.logger.console('info', 'Empty line found')
            return 0
        # Return 0 if line is a comment
        if self.line.startswith('!'):
            self.logger.console('info', 'Comment found')
            return 0
        # Return -1 if line has an exclamation mark in the middle, else return the number of exclamation marks
        importance = self.count_exclamation_marks()
        if importance == -1:
            self.logger.console('error', f'Error: Exclamation Mark missing or in the middle of the line at pos {self.line.index("!") + 1 if "!" in self.line else self.line.__len__()}')
            return -1

        if self.line.startswith('var') or self.line.startswith('const'):
            self.logger.console('info', 'Variable declaration found')
            self.var_handler.set_line(self.line)
            self.line = self.var_handler.get_new()

        self.logger.console('info', f'New line: {self.line}')
