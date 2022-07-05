#spam.py
a = 3
def foo():
    pass
def bar():
    print("I'm function bar() calling foo()")
    foo()   
    
class Spam(object):
    def grok(self):
        print("I'm Spam.grok")