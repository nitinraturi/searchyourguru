from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings
from .mail import *
from apps.users.tokens import account_activation_token

def send_account_activation_mail(request,user):
    current_site = get_current_site(request)
    mail_subject = "Activate Your SearchYourGuru Account"
    to_email = user.email
    template = 'mailers/activate_account_email.html'
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    context = {
        'user': user,
        'domain': current_site.domain,
        'uid':uid,
        'token':token,
    }
    body = render_to_string(template,context=context)
    send_mail(to_email,mail_subject,body)
