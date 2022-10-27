from src.core.command_factory import CommandFactory

class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        while True:
            input_line = input()
            if input_line.lower() == 'exit':
                break
            
            try:
                command = self._command_factory.create(input_line)
                print(f'\033[92m{command.execute()}\033[00m')
            except ValueError as error:
                print(f'\033[92m{error}\033[00m')

        print('\033[95mHave a nice day!\033[00m')
