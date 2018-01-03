from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Course, Class_type, Training_site, Student

def class_list(request):
    latest_class_list = Course.objects.order_by('-class_date_time')
    template = loader.get_template('classes/class_list.html')
    context = { 'latest_class_list':latest_class_list,}
    return HttpResponse(template.render(context, request))
   
   # output = ', '.join([q.course_type for q in latest_class_list])
   # return HttpResponse('Classes APP!'+'How many Course objects: %s' % len(latest_class_list))

def class_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    #student_list = course.student_set.all()
    context = {'course':course}  
    return render(request, 'classes/class_detail.html', context)

   # response = "Here is the most recent class offered: %s"
   # return HttpResponse(response % class_id)

def class_lists(request):
    class_array = Course.objects.all()
    context = {'class_array':class_array}
    return render(request, 'classes/class_list.html', context)

def student_list(request, course_id):
    student = get_object_or_404(Course, pk = course_id) 
    context = {'student':student}
    return render(request, 'classes/student_list.html', context)



def student_detail(request, student_id):
    student = get_object_or_404(Student, pk = student_id)
    context = {'student':student}
    return render(request, 'classes/student_detail.html', context)



# Create your views here.
