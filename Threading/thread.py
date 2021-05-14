import threading

def method1():
    while True:
        print("|----method1----|")

def method2():
    while True:
        print("<----method2---->")

thread1 = threading.Thread(target = method1)
thread2 = threading.Thread(target = method2)

thread1.start()
thread2.start()