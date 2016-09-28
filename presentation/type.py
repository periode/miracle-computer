from sys import stdout

def spell(string, line_break):
    index = 0

    while index < len(string):
        stdout.write(string[index])
        stdout.flush()
        sleep(interval)
        index += 1

    for x in range (0, line_break):
        print(" ")
