from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def form_eval(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            category = form.cleaned_data['category']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            print(name, email)

    form = ContactForm()
    return render(request,'forms.html',{'Form':form})
