#global variable
a=10
def fun1():
    print(a)
def fun2():
    print(a)

fun1()
fun2()

#local variable
def fun3():
    b=10
    print(b)
def fun4():
    print(b)

fun3()
fun4()

    