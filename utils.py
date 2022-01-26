import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def count_files(path):

    i = 0
    for filename in os.listdir(path):
        i += 1
    # print(f"Total Number of files inside '{path}': {i}")
    return i
