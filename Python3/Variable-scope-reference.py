'''
How to use global and nonlocal keywords

LEGB
Local, Enclosing, Global, Built-in

'''

x = 'global x'  # Global
num = 1 #global
def test():
    y = 'local y'  #Local
    x = 'local x'
    print(y)   # local
    print(x)   # local


test()
print (x)  #global
#print(y)  --- THROW ERROR

def test2():
    global x
    global num
    num = 7
    print(num)
    print(x)

test2()
print(num)

def outer():
    out = 'Enclosing Out'
    num1 = 5
    def inner():
        global num
        nonlocal  out        ##this will make the next statement update the Encloding Out
        out = "inner Out"
        num1 = 6
        num = 8
        print(out)
        print(num1)
        print(x)

    inner()
    print(out)  # will print inner out
    print(num) # will print 8

outer()

import builtins
print(dir(builtins))   #NOTE: these can be overwritten!!