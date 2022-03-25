'''
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
    print(num)
    print(x)

test2()

def outer():
    out = 'Global Out'
    num1 = 5
    def inner():
        print(out)
        num1 = 6
        print(num1)
        print(x)

    inner()

outer()



import builtins
print(dir(builtins))   #NOTE: these can be overwritten!!


