from django.contrib import admin

from .models import Student, Course, Customer, Training_site, Class_type, Instructor

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Customer)
admin.site.register(Training_site)
admin.site.register(Class_type)
admin.site.register(Instructor)


# Register your models here.
