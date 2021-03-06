from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from utils.forms import RegistrationForm


def temp(request):
    return render_to_response(
            'temp.html',
            RequestContext(request)
            )


def not_implemented(request):
    return render_to_response(
            'not_implemented.html',
            RequestContext(request)
            )


@login_required
def main_page(request):
    variables = RequestContext(request,
        {'active_courses' : request.user.course_set.filter(is_active=True)}
    )
    return render_to_response('main_page.html', variables)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
            )
            return HttpResponseRedirect('/register/success')
    else:
        form = RegistrationForm()
    variables = RequestContext(request,
        { 'form':form }
    )
    return render_to_response(
        'registration/register.html',
        variables,
        RequestContext(request)
    )


