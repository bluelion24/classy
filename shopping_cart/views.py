# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
	
from django.http import HttpResponse
from .models import Purchaser
from classes.models import Course, Class_type, Training_site, Student
	
def shopping_cart(request, course_id):
    course =  get_object_or_404(Course, pk=course_id)
    context = {'course':course}   
    return render(request, 'shopping_cart/shopping_cart.html', context)

def healthcare_provider(request):
    course_list = Class_type.objects.all()  #get_object_or_404(Course, pk=course_id)
    context = {'course_list':course_list}
    return render(request, 'shopping_cart/healthcare_provider.html', context)

#def non_healthcare_provider(request):

def class_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    context = {"course": course}
    return render(request, "shopping_cart/class_detail.html" , context)

def landing_page(request):
    context = {}
    return render(request, 'shopping_cart/landing_page.html', context)

def bls_course(request):
    course_list = Class_type.objects.filter(class_name__startswith='Health')
    context = {'course_list':course_list}
    return render(request, 'shopping_cart/bls_course.html', context)

#def class_type_page(request):
    


# Create your views here.
