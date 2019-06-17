from django.shortcuts import render,redirect
from django.utils import timezone, six
from django.http import HttpResponse
from .models import Complaint
from .forms import ComplaintForm
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def group_required(group, login_url=None, raise_exception=False):
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups =(group, )
        else:
            groups = group
        if user.groups.filter(name__in=groups).exists():
            return True
        if raise_exception:
            raise PermissionDenied
        return False
    return user_passes_test(check_perms, login_url=login_url)

@login_required
def home(request):

    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():

            context = Complaint()
            context.author = request.user
            context.complaint = form.cleaned_data['complaint']
            context.dept = form.cleaned_data['dept']
            context.save()
            return render(request, 'complaint-registered.html', {'form':context})

    form = ComplaintForm()
    context = {'form':form}
    return render(request, 'complaint-register.html', context)


@login_required
@group_required('staff')
def dashboard(request):
    context = {
        'complaints' : Complaint.objects.all()
        }
    return render(request, 'complaint-dashboard.html', context)

@login_required
def done(request):
    context = 0
    content = {
    "form": context
        }
    return render(request, 'complaint-registered.html', content)
