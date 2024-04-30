# Context Manager
file = open('context.txt','r')
try:
    file = open('context.txt', 'r')
    print(file.read())
except FileNotFoundError as e:
    print(e)
finally:
    if file and not file.closed:
        file.close()

with open('context.txt', 'r') as f:
    print(f.read())


class ContextManager:
    def __init__(self):
        print('Init method called')

    def __enter__(self):
        print('Entering method')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting method')


with ContextManager() as f:
    print('With block statement')




class OpenContextManager:
    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode

    def __enter__(self):
        print('Entering context manager')
        self.file = open(self.file, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting context manager')
        if self.file and not self.file.closed:
            self.file.close()


with OpenContextManager('context.txt', 'w') as file:
    file.write('Writing 1\n')
    file.write('Writing 2')
