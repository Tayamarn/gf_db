import hashlib
import urllib.parse

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import CreationForm
from django.urls import reverse_lazy


@login_required
def index(request):
    template = 'users/index.html'
    user = request.user

    avatar_size = 400
    gravatar_url = "https://www.gravatar.com/avatar/"
    gravatar_url += hashlib.md5(user.email.lower().encode('utf-8')).hexdigest()
    gravatar_url += "?" + urllib.parse.urlencode({'s':str(avatar_size)})

    context = {
        'user': user,
        'gravatar_url': gravatar_url,
    }
    return render(request, template, context)


def help(request):
    template = 'users/help.html'
    return render(request, template)


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('users:main')
    template_name = 'users/signup.html'
