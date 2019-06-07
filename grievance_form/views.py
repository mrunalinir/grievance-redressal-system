from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import Grievance_form

def register_grievance(request):
    if request.method=='POST':
        form = Grievance_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/tokens/')
    else:
        form=Grievance_form()

    return render(request,'grievanceform.html', {'form': form })
