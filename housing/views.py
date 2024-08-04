from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def title1(text):
    return f'<h1>{text}</h1>'


def index(request):
    main_page = _("Main page")
    return HttpResponse(title1(main_page))


def about(request):
    about_text = _("About")
    return HttpResponse(title1(about_text))


def contacts(request):
    contact_text = _("Contacts")
    return HttpResponse(title1(contact_text))



