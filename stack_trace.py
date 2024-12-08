def func_a():
    print('Function A Started')
    func_b()
    print('Function A end')

def func_b():
    print('Function B Started')
    func_c()
    print('Function B end')

def func_c():
    print('Function C Started')
    result = 10/0
    print('Function c end')

func_a()
