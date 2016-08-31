import os
from sys import stdout
from time import sleep

choice = ""
prompt = "begin?"

def title():
    print('\n')
    print("##########################")
    print('serpentine 2016')
    print("##########################")
    for x in range(0, 20):
        print('\n')



while choice != 'q':
    choice = input(prompt+" ")

    if choice == "yes":
        stdout.write('here we are')
        stdout.flush()
        sleep(.5)
        stdout.write('.')
        stdout.flush()
        sleep(.5)
        stdout.write('.')
        stdout.flush()
        sleep(.5)
        stdout.write('.')
        stdout.flush()
        sleep(1)
        print(" and here you stay")
        sleep(1)
        prompt = "what now?"
    elif choice == "q":
        quit()
    else:
        print('excuse me?')

# for i in range(1,20):
#     stdout.write(".")
#     stdout.flush()
#     sleep(1)
