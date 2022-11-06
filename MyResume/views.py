from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def index(request):
    if request.method=='POST':
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        sender=request.POST.get('email')
        msg=request.POST.get('message')
        message=name + ', '+ msg
        recipient=['sotile16@gmail.com']
        send_mail(subject, message, sender, recipient)
        
        return HttpResponse("Thank you for your consideration! I will get back to you as soon as possible")
    return render(request, 'MyResume/index.html')