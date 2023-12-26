from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from arnarpkan.settings import EMAIL_HOST_USER
from .import forms  
from .models import Account
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
from django.db import connection

# Create your views here.
def subscribe(request):
  sub = forms.Subscribe()
  if request.method == 'POST':
    sub = forms.Subscribe(request.POST)
    name = sub['Name'].value()
    name=mark_safe(name)
    subject = 'KAYA Newsletter Subscription'
    message = ''
    html_message = 'Dear '+name+', Thank you for subscribing to our monthly newsletter.'
    recepient = str(sub['Email'].value())
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False, html_message=html_message)
    return render(request, 'success.html', {'name': name, 'email': recepient})
  return render(request, 'kaya.html', {'form':sub})

def login(request):
    template=loader.get_template("login.html")
    return HttpResponse(template.render({}, request))

def account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        with connection.cursor() as cursor:
           query = f"SELECT id FROM kaya_account WHERE username = '{username}' AND password = '{password}'"
           print("SQL Query:", query)
           cursor.execute(query)
           user_id = cursor.fetchone()
           if user_id:
              request.session['user_id'] = user_id[0]
              return HttpResponseRedirect(reverse('welcome'))
           else:
              return HttpResponseRedirect(reverse('login'))
           
def welcome(request):
  template=loader.get_template("account.html")
  return HttpResponse(template.render({}, request))