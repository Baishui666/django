from django.http import HttpResponseRedirect


def login_check(fn):
    def check(request, *args, **kwargs):
        if request.session.has_key('user_id'):
            return fn(request, *args, **kwargs)

        else:
            red = HttpResponseRedirect('/user/login')
            print 'usercheck', request.get_full_path()
            red.set_cookie('url', request.get_full_path())
            return red
    return check