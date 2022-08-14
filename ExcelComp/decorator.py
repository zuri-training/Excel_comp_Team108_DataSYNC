from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_funct(request, *a, **kw):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *a, **kw)

    return wrapper_funct
