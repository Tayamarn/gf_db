import hashlib
import urllib.parse

from .forms import CreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


def user_context(user):
    avatar_size = 400
    gravatar_url = "https://www.gravatar.com/avatar/"
    gravatar_url += hashlib.md5(user.email.lower().encode('utf-8')).hexdigest()
    gravatar_url += "?" + urllib.parse.urlencode({'s':str(avatar_size)})

    context = {
        'user': user,
        'gravatar_url': gravatar_url,
    }
    return context

@login_required
def index(request):
    template = 'users/index.html'
    user = request.user

    context = user_context(user)
    return render(request, template, context)


@login_required
def user(request, user_id):
    template = 'users/user.html'
    user = get_user_model().objects.get(id=int(user_id))

    context = user_context(user)
    return render(request, template, context)


def help(request):
    template = 'users/help.html'
    return render(request, template)


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('users:main')
    template_name = 'users/signup.html'
