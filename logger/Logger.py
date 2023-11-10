colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'grey': '\033[90m',
    'white': '\033[97m',
}

headers = {
    'error': 'red',
    'success': 'green',
    'warning': 'yellow',
    'info': 'blue',
    'debug': 'purple',
    'test': 'cyan',
    'default': 'grey',
}


class Logger:
    def __init__(self, path, filename, executing_file=__name__):
        self.auto_write = True
        self.path = path
        self.filename = filename
        self.file = None
        self.colors = colors
        self.headers = headers
        self.executing_file = executing_file

    def open(self):
        self.file = open(self.path + self.filename, 'w+')

    def write(self, data):
        self.file.write(data)

    def append(self, data):
        with open(self.path + self.filename, 'a') as file:
            file.write(data)

    def close(self):
        self.file.close()

    def test(self):
        self.console('info', 'Testing logger...')
        self.console('test', f'{self.path + self.filename}')
        for color, code in self.colors.items():
            self.console('test', f'{code + color}\033[0m', end=', ')
        print()
        self.console('info', 'Logger testing completed', color='green')

    def console(self, header='default', data='', color='none', end='\n'):
        if color == 'none': color = f'{self.headers[header]}'
        print(f'{self.colors[self.headers[header]]}[{header.upper()}] '
              f'{self.colors["white"]}{self.executing_file}: '
              f'{self.colors[color]}{data}\033[0m', end=end)
        if self.auto_write:
            self.append(f'[{header.upper()}] {self.executing_file}: {data}\n')