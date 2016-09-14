import os
import math
import random
from sys import stdout
from time import sleep
from blessings import Terminal
import decimal
import string


#user files
import life
import human as h
import color as c

# import pyttsx

t = Terminal()

choice = ""
prompt = ""
stage = 0
interval = 0.03

human = h.Human()
red = c.Color()

turing = []
truth_symbols = ['F', 'NOR', 'Xq', '¬p', '↛', '¬q', 'XOR', 'NAND', 'AND', 'XNOR', 'q', 'if/then', 'p', 'then/if', 'OR', 'T']
truth_legends = ['contradiction', 'logical NOR', 'converse non-implication', 'negation', 'material non-implication', 'negation', 'exclusive disjunction', 'logical NAND', 'logical conjunction', 'logical biconditional', 'projection function', 'material implication (rule of inference)', 'projection function', 'converse implication', 'logical disjunction', 'tautology']

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

def spell(string, line_break):
    index = 0

    while index < len(string):
        stdout.write(string[index])
        stdout.flush()
        sleep(interval)
        index += 1

    for x in range (0, line_break):
        print(" ")

def set_style(st):
    if st == 'reverse':
        print(t.reverse+'', end="")
    elif st == 'red':
        print('{t.red}'.format(t=t), end="")

def reset_style():
    print('{t.normal}'.format(t=t), end="")
    print(t.on_black+"", end="")

def title():
    print('\n')
    spell("##########################",1)
    spell('serpentine 2016', 1)
    spell("##########################", 1)
    for x in range(0, 10):
        sleep(0.1)
        print('\n')


def display_turing():
    spell("it started with a text.", 1)
    print("")
    spell("it was written by ", 0)
    set_style('reverse')
    spell("alan turing", 0)
    reset_style()
    print("")
    sleep(3)
    print("")


    turing_index = 0
    global turing

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

def display_truth():
    spell("the truth functions are as follow:", 3)
    index = 0
    for index in range(0, len(truth_symbols)):
        set_style("reverse")
        spell(" "+truth_symbols[index], 1)
        reset_style()
        spell(truth_legends[index], 3)
        sleep(1)
        index += 1
    print("")

def demonstrate():
    t = 0
    while t < 10:
        spell("READ", 1)
        spell("PROCESS", 1)
        spell("WRITE", 1)
        t += 1

def compute(complexity_level):
    add = ""
    sub = ""
    mult = ""
    div = ""

    read = " "
    write = " "

    if complexity_level == 1:
        add = "+ "
        sub = "- "
        mult = "* "
        div = "/ "
    elif complexity_level == 2:
        add = ""+bin(ord('a'))[2:]+bin(ord('d'))[2:]+bin(ord('d'))[2:]+" "
        sub = ""+bin(ord('s'))[2:]+bin(ord('u'))[2:]+bin(ord('b'))[2:]+" "
        mult = ""+bin(ord('m'))[2:]+bin(ord('u'))[2:]+bin(ord('l'))[2:]+" "
        div = ""+bin(ord('d'))[2:]+bin(ord('i'))[2:]+bin(ord('v'))[2:]+" "
        read = ""+bin(ord('r'))[2:]+bin(ord('e'))[2:]+bin(ord('a'))[2:]+bin(ord('d'))[2:]+" "
        write = ""+bin(ord('w'))[2:]+bin(ord('r'))[2:]+bin(ord('i'))[2:]+bin(ord('t'))[2:]+bin(ord('e'))[2:]+" "
    elif complexity_level == 3:
        add = "ADD "
        sub = "MIN "
        mult = "MUL "
        div = "DIV "
        read = "READ "
        write = "WRITE "


    a = 0
    b = 0
    t = 0
    while t < 10:
        spell(read+str(decimal.Decimal(a)), 1)
        sleep(0.5)
        b = random.randint(0, 256)
        r = random.random()
        if r < 0.25:
            if(complexity_level == 2):
                spell(add+str(bin(b)[2:]), 1)
            else:
                spell(add+str(b), 1)
            sleep(0.5)
            a += b
        elif r < 0.5:
            if(complexity_level == 2):
                spell(sub+str(bin(b)[2:]), 1)
            else:
                spell(sub+str(b), 1)
            sleep(0.5)
            a -= b
        elif r < 0.75:
            if(complexity_level == 2):
                spell(mult+str(bin(b)[2:]), 1)
            else:
                spell(mult+str(b), 1)
            sleep(0.5)
            a *= b
        else:
            if(complexity_level == 2):
                spell(div+str(bin(b)[2:]), 1)
            else:
                spell(div+str(b), 1)
            sleep(0.5)
            a /= b
        t += 1
        spell(write+str(decimal.Decimal(a)), 1)

def display_datatypes():
    spell("a ", 0)
    set_style("reverse")
    spell("boolean", 0)
    reset_style()
    spell(" is a datatype which represents the value true or false.", 2)

    sleep(1)

    spell("a ", 0)
    set_style("reverse")
    spell("floating point", 0)
    reset_style()
    spell(" is a datatype which represents rational numbers.", 2)

    sleep(1)

    spell("a ", 0)
    set_style("reverse")
    spell("integer", 0)
    reset_style()
    spell(" is a datatype which represents whole numbers.", 2)

    sleep(1)

    spell("a ", 0)
    set_style("reverse")
    spell("fixed point", 0)
    reset_style()
    spell(" is a datatype which represents a monetary value.", 2)

    sleep(1)

    spell("an ", 0)
    set_style("reverse")
    spell("array", 0)
    reset_style()
    spell(" is a datatype which stores a number of elements of the same type in a specific order.", 2)

    sleep(1)

    spell("an ", 0)
    set_style("reverse")
    spell("object", 0)
    reset_style()
    spell(" is a datatype which contains a number of data fields, as well as a number of subroutines for accessing or modifying them, called methods.", 2)

    sleep(1)

    spell("an ", 0)
    set_style("reverse")
    spell("object", 0)
    reset_style()
    spell(" is a datatype which can be ", 0)
    set_style("reverse")
    spell("anything", 0)
    reset_style()
    spell(".", 2)

def dislay_object_skeleton():
    spell("Object(){", 1)
    spell("\t be_something = ''", 1)
    spell("\t store_something = 0", 1)
    spell("\t do_something(arg){", 1)
    spell("\t\t ...", 1)
    spell("\t }", 1)
    spell("}", 2)
    spell("let o = new Object()", 3)

def generate_string():
    output = ''
    length = random.randint(3, 14)
    index = 0
    while index < length:
        output += random.choice(string.ascii_letters)
        index += 1
    return output

def generate_int():
    output = ''
    length = random.randint(3, 14)
    index = 0
    while index < length:
        output += str(random.randint(0, 9))
        index += 1
    return output

def elaborate_object():
    index = 0

    while index < 20:
        r = random.random()

        new_string = generate_string()
        new_int = generate_int()

        if r < 0.33:
            set_style("reverse")
            spell("be", 0)
            reset_style()
            spell("_something = '"+new_string+"'", 2)
        elif r < 0.66:
            set_style("reverse")
            spell("store", 0)
            reset_style()
            spell("_something = "+new_int+"", 2)
        else:
            set_style("reverse")
            spell("do", 0)
            reset_style()
            spell("_something(else)", 2)

        index += 1

def extrapolate_human():
    spell(str(human), 2)
    sleep(1)
    property_names = vars(human)
    for key in property_names:
        print("%s: %s" % (key, property_names[key]))

    print("")
    sleep(3)
    spell("this is what consitutes a human", 1)

def enumerate_red():
    spell(str(red), 2)
    sleep(1)
    property_names = vars(red)
    for key in property_names:
        print("%s: %s" % (key, property_names[key]))

def blood_rain():
    ind = 0
    modulo = 1
    while ind < 10000000:
        if ind % int(modulo) == 0:
            print(t.on_red+"  ", end="")
        else:
            print(t.normal+" ", end="")
        ind+=1
        modulo += 0.00001


def run_life():
    step = 0
    while step < 40:
        print("life at step # %i" % step)
        print(life.my_game.display())
        sleep(0.2)
        life.my_game.step(step)
        step += 1

######################################################### START
setup_turing()
title()
reset_style()
blood_rain()

while choice != 'q':
    choice = input(prompt)

    if choice == "hello.":
        spell("hello.", 2)

    elif choice == "what are you?":
        spell("i'm a universal machine.", 2)

    elif choice == "what can you do?":
        spell("i can count.", 2)

    elif choice == "what can you count?":
        spell("anything that is a real number.", 2)

    elif "truth" in choice:
        display_truth()

    elif choice == "how can you count?":
        display_turing()
        spell("and he goes on to describe what the universal machine is.", 1)
        spell("do you want to see it in action?", 1)
        stage += 1

    elif choice == "sure." or choice == "sure":
        spell("it kinda goes like this...", 2)
        sleep(1)
        demonstrate()
        spell("should i continue?", 2)
        interrupt = input()
        while interrupt != "no, thank you.":
            demonstrate()
            spell("should i continue?", 2)
            interrupt = input()
        spell("what else?", 2)

    elif choice == "and you do that with numbers.":
        spell('yes.', 2)
        sleep(3)
        compute(1)
        spell("should i continue?", 2)
        interrupt = input()
        while interrupt != "no, thank you.":
            compute(1)
            spell("should i continue?", 2)
            interrupt = input()
        spell("what else?", 2)


    elif choice == "how do you understand it?":
        spell('one way or another.', 2)
        sleep(3)
        compute(2)
        spell("should i continue?", 2)
        interrupt = input()
        while interrupt != "no, thank you.":
            compute(2)
            spell("should i continue?", 2)
            interrupt = input()
        spell("what else?", 2)

    elif choice == "can you translate it?":
        spell('for you, it would be something like this:', 2)
        sleep(3)
        compute(3)
        spell("should i continue?", 2)
        interrupt = input()
        while interrupt != "no, thank you.":
            compute(3)
            spell("should i continue?", 2)
            interrupt = input()
        spell("what else?", 2)

    elif choice == "is this all you understand?":
        spell("i understand data types based on numerical values.", 3)
        sleep(1)
        display_datatypes()

    elif "object" in choice:
        spell("they all have the same skeleton.", 2)
        sleep(1)
        dislay_object_skeleton()
        elaborate_object()
        spell("should i continue?", 2)
        interrupt = input()
        while "no" not in interrupt:
            elaborate_object()
            spell("should i continue?", 2)
            interrupt = input()

    elif "human" in choice:
        spell("of course.", 2)
        sleep(1)
        print(human)
        sleep(1)
        spell("i need more information", 2)
        spell("what's your name?", 1)
        human.name = input()
        print("")
        spell("how old are you?", 1)
        human.age = input()
        print("")
        spell("what's your gender?", 1)
        human.gender = input()
        if type(human.name) != int:
            set_style("reverse")
            spell("ERR", 0)
            reset_style()
            spell(": human.gender attribute must be of type ", 0)
            set_style("reverse")
            spell("binary", 0)
            reset_style()
            spell(".", 2)
            sleep(1)
            spell("what's your gender? (0-1)", 1)
            human.gender = input()
        print("")
        spell("are you employed? (yes/no)", 1)
        human.employed = input()
        human.employed = True
        print("")
        spell("what's your job?", 1)
        human.job = input()
        print("")
        spell("what's your country of origin?", 1)
        human.country_of_origin = input()
        print("")
        spell("what's your country of residence?", 1)
        human.country_of_residence = input()
        print("")
        spell("how is your health?", 1)
        human.health = input()
        print("")
        spell("how are you feeling?", 1)
        human.feeling = input()
        set_style("reverse")
        spell("ERR", 0)
        reset_style()
        spell(": human.feeling attribute must be of type ", 0)
        set_style("reverse")
        spell("integer", 0)
        reset_style()
        spell(".", 1)
        spell("how are you feeling? (0-10)", 1)
        human.feeling = input()
        print("")
        sleep(1)
        spell("thank you for your input.",1)
        sleep(2)
        spell("processing", 0)
        interval = 0.1
        spell("........................", 0)
        spell("done", 2)
        interval = 0.03
        extrapolate_human()

    elif "red" in choice:
        spell("i know that red is a triplet of values sent to the graphics output device, ranging from 0 to 255", 1)
        sleep(0.5)
        spell("red is [255, 0, 0]", 2)

    elif "blood" in choice:
        spell("i did not know that.", 2)
        sleep(0.5)
        set_style("reverse")
        spell("we", 0)
        reset_style()
        spell(" can create an object to structure that data.", 2)
        sleep(0.25)
        print("")
        sleep(0.25)
        enumerate_red()
        blood_rain()

    elif choice == "life":
        run_life()

    elif choice == "ok, i'm done.":
        reset_style()
        spell("until next time", 1)
        quit()
    else:
        print_error()

    stage += 1
