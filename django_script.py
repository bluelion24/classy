from classes.models import Training_site, Class_type, Course, Student
from datetime import date

#Course.objects.all().delete()

a = Training_site(training_site_name = 'Santa Maria')
a.save()
b = Class_type(class_name = 'Healthcare Provider', training_site = a)
b.save()
c = Course(class_date_time = date(1,2,3), id = None, class_type = b)
c.save()
d = Student(first_name = 'Aaron', last_name = 'Conover', course = c, id = None)
d.save()

print(d, 'c.id ' + str(c.id))

aa = Training_site(training_site_name = 'San Luis Obispo')
aa.save()
bb = Class_type(class_name = a, training_site = a)
bb.save()
cc = Course(class_date_time = date(1,2,3), id = None, class_type = b)
cc.save()
dd = Student(first_name = 'Ava', last_name = 'Conover', course = c, id = None)
dd.save()

print(dd)

aaa = Training_site(training_site_name = 'Santa Maria')
aaa.save()
bbb = Class_type(class_name = 'Healthcare Provider', training_site = a)
bbb.save()
ccc = Course(class_date_time = date(1,2,3), id = None, class_type = b)
ccc.save()
ddd = Student(first_name = 'Aaron', last_name = 'Conover', course = c, id = None)
ddd.save()

print(ddd)

#Printing roster
class_id = c.id
course = Course.objects.get(pk = class_id)
class_list = course.student_set.all()
for student in class_list:
    print (str(student))

