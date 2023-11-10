from logger.Logger import Logger


class VarHandler:
    def __init__(self):
        self.line = None
        self.logger = Logger('data/log/', 'last.log', __name__)
        self.logger.console('info', 'VarHandler Setup complete...', color='green')

    def set_line(self, line: str):
        self.line = line
        self.logger.console('info', f'New Line set to {self.line}')

    def get_new(self):
        self.line = self.line.replace(' const', '').replace(' var', '').replace('const', '').replace('var', '')
        return self.line
