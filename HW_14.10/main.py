import commands


commands.first_help()

command = ''
while command != 'exit':
    command = input('Введите комманду: ')
    commands.do(command)