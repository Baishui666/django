

def login_check(fn):
    def check(request, *args, **kwargs):
        if request < 10:
            return fn(request, *args, **kwargs)
        else:
            print "no~~`"
    return check

@login_check
def f1(a,*args, **kwargs):
    a += 1
    print a
    print args
    print kwargs

f1(1,2)
f1(11)
f1(1,2,4,5,c=1,b=4)