# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from emails.forms import SignupForm
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.db import IntegrityError

   # Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

@csrf_exempt
def twillio_page(request):
    try:
        if request.method == 'POST':
            sub = Subscriber(email=request.POST['email'], name = request.POST['name'], conf_num=random_digits())
            sub.save()
            message = Mail(
                from_email=settings.FROM_EMAIL,
                to_emails=sub.email,
                subject='Newsletter Confirmation',
                html_content='Thank you for signing up for my email newsletter! \
                    Please complete the process by \
                    <a href="{}?email={}&conf_num={}"> clicking here to \
                    confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                        sub.email,
                                                        sub.conf_num))
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            return render(request, 'signup/twillioSignup.html', {'email': sub.email, 'action': 'added', 'form': SignupForm()})
        else:
            return render(request, 'signup/twillioSignup.html', {'form': SignupForm()})
    except IntegrityError as e:
        return render(request, 'signup/twillioSignup.html', {'form': SignupForm(), 'message' : e.__cause__})
            

def confirm_page(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'signup/confirm.html', {'name': sub.name, 'message': 'Email confirmed! Welcome to the Ayekah giving family'})
    else:
        return render(request, 'signup/confirm.html   ', {'message': 'Somethings wrong'})