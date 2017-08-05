from django.shortcuts import render
from .forms import SubscribersForm

# Create your views here.
def landing(request):
    form = SubscribersForm(request.POST or None)
    if request.method == 'POST':
        print (form)
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())