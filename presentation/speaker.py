import pyttsx
import threading
import ctypes
import socket

ip = "127.0.0.1"
port = 2046

w_add = "111001111101011100010"

def onEnd(name, completed):
    print 'finishing', name, completed
    voice.endLoop()

def speak_out(w):
    voice = pyttsx.init()
    voice.connect('finished-utterance', onEnd)
    voice.say(w)
    voice.runAndWait()



speak_thread = None

#terminate a thread
def terminate_thread(thread):
    if not thread.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


#check if a thread is still active, then terminate it
def clear_thread():
    global speak_thread

    if speak_thread is not None:
        terminate_thread(speak_thread)
        speak_thread = None
        print ("first clearing thread...")


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))


while True:
    print "listening for orders..."

    data, address = sock.recvfrom(1024)
    order = data.decode('utf-8')
    print "...received message: %s" % order

    if order == 'kill':
        clear_thread()
    elif order == 'add':
        speak_out(w_add)
    else:
        print '?'

    print '... done speaking, for now.'
