from classes.models import Training_site, Class_type, Course, Student

all_students = Course.objects.all()

for student in all_students:
    student.middle_name = ''
    student.save()
    print(str(student) + 'Student new attribute' + student.middle_name)
    	

print('All done')

