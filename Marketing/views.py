from django.shortcuts import render
from .models import EmailList
# Create your views here.


def submit(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        if EmailList.objects.filter(user_email=user_email).exists():
            messages.info(request, " You are already in Our Emailist🧐..")
        else:
            obj = EmailList(user_name=user_name, user_email=user_email)
            obj.save()
            messages.info(request, "You are Now in Our Emailist🤩..")
