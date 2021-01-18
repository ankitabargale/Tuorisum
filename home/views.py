from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable':"hi ankita"

    }
    return render(request , 'index.html', context)
    # return HttpResponse("This is home page")

def about(request):
    return render(request , 'about.html')

def services(request):
    return render(request , 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dsc = request.POST.get('dsc')
        contact = Contact(name=name, email=email, phone=phone, dsc=dsc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been send')
    return render(request , 'contact.html')
