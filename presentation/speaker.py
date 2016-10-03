import pyttsx
import threading
import ctypes

def speak_out():
    # def onStart(name):
    #     #do
    # def onWord(name, location, length):
    #
    # def onEnd(name, completed):
    #     engine.stop()
    #     engine.endLoop()


    engine = pyttsx.init()
    # engine.connect('started-utterance', onStart)
    # engine.connect('started-word', onWord)
    # engine.connect('finished-utterance', onEnd)
    engine.say('Thanks for this. The result was a bit of a surprise, but first I think I should very briefly explain what my code is doing: the program I\'m running is a mod for Quake that makes it accessible to vision-impaired and blind gamers')
    engine.startLoop()

def speak_out2():
    # def onStart(name):
    #     #do
    # def onWord(name, location, length):
    #
    # def onEnd(name, completed):
    #     engine.stop()
    #     engine.endLoop()


    engine = pyttsx.init()
    # engine.connect('started-utterance', onStart)
    # engine.connect('started-word', onWord)
    # engine.connect('finished-utterance', onEnd)
    engine.say('Thanks for this. I hate you vanessa.')
    engine.startLoop()


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


speak_thread = threading.Thread(target=speak_out, args=())
speak_thread.start()


while True:
    command = raw_input('what? ')

    if command == 'kill':
        clear_thread()
    elif command == 'again':
        speak_thread = threading.Thread(target=speak_out2, args=())
        speak_thread.start()
    else:
        print('?')
