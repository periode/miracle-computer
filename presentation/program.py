import os
import random
from sys import stdout
from time import sleep
from blessings import Terminal

t = Terminal()

choice = ""
prompt = ""
stage = 0
interval = 0.03

turing = []
turing_index = 0


def setup_turing():
    turing.append("ON COMPUTABLE NUMBERS, WITH AN APPLICATION TO THE ENTSCHEIDUNGSPROBLEM\n\n\n")
    turing.append("The \"computable\" numbers may be described briefly as the real numbers whose expressions as a decimal are calculable by finite means. Although the subject of this paper is ostensibly the computable numbers. it is almost equally easy to define and investigate computable functions of an integral variable or a real or computable variable, computable predicates, and so forth. The fundamental problems involved are, however, the same in each case, and I have chosen the computable numbers for explicit treatment as involving the least cumbrous technique. I hope shortly to give an account of the relations of the computable numbers, functions, and so forth to one another. This will include a development of the theory of functions of a real variable expressed in terms of computable numbers.")

    ##red 2
    turing.append("According to my definition, a number is computable if its decimal can be written down by a machine.")

    turing.append("\n\nIn §§ 9, 10 I give some arguments with the intention of showing that the computable numbers include all numbers which could naturally be regarded as computable. In particular, I show that certain large classes of numbers are computable. They include, for instance, the real parts of all algebraic numbers, the real parts of the zeros of the Bessel functions, the numbers PI, e, etc. The computable numbers do not, however, include all definable numbers, and an example is given of a definable number which is not computable.")
    turing.append("Although the class of computable numbers is so great, and in many ways similar to the class of real numbers, ")

    ##red 5
    turing.append("it is nevertheless enumerable")

    turing.append(". In § 81 examine certain arguments which would seem to prove the contrary. By the correct application of one of these arguments, conclusions are reached which are superficially similar to those of Gödel. These results have valuable applications. In particular, it is shown (§11) that the Hilbertian Entscheidungsproblem can have no solution. In a recent paper Alonzo Church has introduced an idea of \"effective calculability\", which is equivalent to my \"computability\", but is very differently defined. Church also reaches similar conclusions about the Entscheidungsproblem. The proof of equivalence between \"computability\" and \"effective calculability\" is outlined in an appendix to the present paper.")
    turing.append("\n\n    1. Computing machines.\n\nWe have said that the computable numbers are those whose decimals are calculable by finite means. This requires rather more explicit definition. No real attempt will be made to justify the definitions given until we reach § 9. ")

    ##red
    turing.append("For the present I shall only say that the justification lies in the fact that the human memory is necessarily limited.")

    turing.append("\n\nWe may compare a man in the process of computing a real number to a machine which is only capable of a finite number of conditions q1; q2; ... qI; which will be called \"m-configuration\". The machine is supplied with a \"tape\" (the analogue of paper) running through it, and divided into sections (called \"squares\") each capable of bearing a \"symbol\". At any moment there is just one square, say the r-th, bearing the symbol <2>(r) which is \"in the machine\". We may call this square the \"scanned square\". The symbol on the scanned square may be called the \"scanned symbol\". The \"scanned symbol\" is ")
    ##red 10
    turing.append("the only one of which the machine is, so to speak, \"directly aware\"")

    turing.append(". However, by altering its m-configuration the machine can effectively remember some of the symbols which it has \"seen\" (scanned) previously. The possible behaviour of the machine at any moment is determined by the ra-configuration qn and the scanned symbol <S (r). This pair qn, (r) will be called the \"configuration\": thus the configuration determines the possible behaviour of the machine. In some of the configurations in which the scanned square is blank (i.e. bears no symbol) the machine writes down a new symbol on the scanned square: in other configurations it erases the scanned symbol. The machine may also change the square which is being scanned, but only by shifting it one place to right or left. In addition to any of these operations the m-configuration may be changed. Some of the symbols written down will form the sequence of figures which is the decimal of the real number which is being computed. ")

    ##red 12
    turing.append("The others are just rough notes to \"assist the memory \".")

    turing.append(" It will only be these rough notes which will be liable to erasure.\n")
    turing.append("It is my contention that these operations include all those which are used in the computation of a number. ")

    ##red 15
    turing.append("The defence of this contention will be easier when the theory of the machines is familiar to the reader. ")

    turing.append("In the next section, ")

    ##red 17
    turing.append("I therefore proceed with the development of the theory and assume that it is understood what is meant by \"machine\", \"tape\", \"scanned\", etc.")


def title():
    print('\n')
    print("##########################")
    print('serpentine 2016')
    print("##########################")
    for x in range(0, 20):
        print('\n')

def spell(string, line_break):
    i = 0
    while i < len(string):
        stdout.write(string[i])
        stdout.flush()
        sleep(interval)
        i += 1

    for x in range (0, line_break):
        print(" ")

def print_error():
    r = random.random()

    if r < 0.2:
        spell('excuse me?', 1)
    elif r < 0.4:
        spell('i didn\'t quite understand.', 1)
    elif r < 0.6:
        spell('can you say that again?', 1)
    elif r < 0.8:
        spell('what did you say?', 1)
    else:
        spell('i\'m sorry?', 1)

def set_style(st):
    if st == 'reverse':
        print(t.reverse+'', end="")
    elif st == 'red':
        print('{t.red}'.format(t=t), end="")

def reset_style():
    print('{t.normal}'.format(t=t), end="")

def compute():
    print("1")



######################################################### START
setup_turing()
title()
reset_style()

while choice != 'q':
    choice = input(prompt)

    if choice == "hello.":
        spell("would you like to read the text that gave me birth?", 1)
    elif choice == "sure":
        spell("it was written by ", 0)
        set_style('red')
        spell("alan turing", 1)
        reset_style()
        sleep(3)
        print("")
        while turing_index < len(turing):
            if turing_index == 2 or turing_index == 5 or turing_index == 8 or turing_index == 10 or turing_index == 12 or turing_index == 15 or turing_index == 17:
                set_style('reverse')
            else:
                reset_style()
            spell(turing[turing_index], 0)
            reset_style()
            turing_index += 1
        print("")
        print("")
        stage += 1
    elif choice == "what can you do?":
        compute()
    elif choice == "q":
        reset_style()
        spell("until next time", 1)
        quit()
    else:
        print_error()

    stage += 1
