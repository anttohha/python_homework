def debug(funct):
    def output_func(*args):
        s = args[0] + args[1]
        print(f'{funct.__name__} ,args[0]-{args[0]}, args[1]-{args[1]}, сумма  {s}')
        return s

    return output_func


@debug
def funct1(a, b):
    return a + b
    

s = funct1(3, 5)
