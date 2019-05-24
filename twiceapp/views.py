# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Twice

def ShowMember(request):
    members = Twice.objects.all
    japanese = Twice.objects.filter(nationality = 'JP')
    #return render(request, 'home.html', {'members':members})
    return render(request, 'home.html', {'members':members, 'japanese':japanese})
