from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
from django.contrib import messages
def index (request):
    if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        age=request.POST.get('age')
        adress=request.POST.get('adress')
        if age<'18':
            messages.success(request,'you are under age not to submit the form ')
        else:
            data = Data(name=name, mobile=mobile, age=age, adress=adress)
            data.register()
            messages.success(request, 'your message has been sent successfully ! contact you soon')


    else:
        return render(request,'index.html')

    return render(request,'index.html')


