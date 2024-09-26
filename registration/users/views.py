import hashlib
import urllib.parse

from .forms import CreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView

from .models import Profile

#User = get_user_model()


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

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'users/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class CreateProfilePageView(CreateView):
    model = Profile

    template_name = 'users/create_profile.html'
    fields = ['telegram', 'vk', 'email', 'nikname', 'civilname']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('tasks')
