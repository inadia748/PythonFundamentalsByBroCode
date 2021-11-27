# keyword arguments = arguments preceded by an identifier when we pass them to a function. The order of the arguments does n't matter, unlike positinal arguemnts. Python knows the names of the arguments that our function receives.

def hello(first, middle, last):
    print('Hello '+ first + ' '+ middle+' '+ last)

hello(last = 'Code', middle = 'Gal', first = 'Sis')