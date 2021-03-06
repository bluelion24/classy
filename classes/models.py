from django.db import models

class Training_site(models.Model):
    training_site_name = models.CharField(max_length=100, default='nully')
    class_street_address = models.CharField(max_length = 200, default='nully')
    class_street_apt_suite = models.CharField(max_length = 200, default='nully')
    class_city = models.CharField(max_length = 200, default='nully')
    training_site_state = models.CharField(max_length=2, default='nully')
    training_site_country = models.CharField(max_length=100, default='nully')
    training_site_zip_code = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Training site: " + self.training_site_name
    
    def get_training_site(self):
        return self.training_site_name + ' ' + self.class_street_address + ' ' + self.class_city 

class Class_type(models.Model):
    training_site = models.ForeignKey(Training_site, on_delete=models.CASCADE)
    class_name = models.CharField(max_length = 200, default = 'nully')
    
    def __str__(self):
        return str(self.training_site) + "   Class name: " + self.class_name 

class Course(models.Model):
    class_type = models.ForeignKey(Class_type, on_delete=models.CASCADE)
   # class_date_time = models.DateTimeField(null=True, blank=True)  
    class_date_time = models.DateField(null=True, blank=True)
    class_roster = models.CharField(max_length = 200, default='nully')
    class_query_type = models.CharField(max_length = 200, default='nully')
#    roster = Student.Coursey.all()
#    class_id = models.AutoField(primary_key=True)
#    def __myTimeFunction__(year, month, day):
#        self.class_date_time = year
#         self.class_date_time = month
#         self.class_date_time = day

    def myfunction(self):
        return 'myfunction() works!'

    def print_roster(self):
        return 'test'

    def __str__(self):
        return str(self.class_type) + "   Class date:  "  + str(self.class_date_time) + "   Course_id: " + str(self.id)  

class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 75, default='nully')
    last_name = models.CharField(max_length = 150, default='nully')
    middle_name = models.CharField(max_length = 100, blank = True, default='')
    class_type = models.TextField(max_length = 200, default='nully')
    order_id = models.CharField(max_length = 200, default='nully')
    order_date = models.CharField(max_length = 200, default='nully')
    order_discount_code = models.CharField(max_length = 200, default='nully')
    class_registered = models.CharField(max_length = 200)
    classes_completed = models.CharField(max_length = 200)
    classes_incomplete = models.CharField(max_length = 200)
#    roster = Coursey.objects.all()

    def studentDetail(self):
        return 'Student name: ' + self.first_name + '  ' + self.last_name + '  ' + str(self.course)
    def __str__(self):
        return 'Student name: ' + self.last_name + '  '  + self.first_name 

    class Meta:
        #Alphabetical order
        ordering = ['last_name']

class Customer(models.Model):
    coursex = models.ForeignKey(Student, related_name = 'Student')
    first_name = models.CharField(max_length = 75)
    last_name = models.CharField(max_length = 75, default='last_name')
    def __str__(self):
        return self.first_name + self.last_name

class Instructor(models.Model):
    instructor_first_name = models.CharField(max_length=100, default='nully')
    instructor_last_name = models.CharField(max_length=100, default='nully')
    instructor_id = models.CharField(max_length=100, default='nully')
    instructor_email = models.EmailField(max_length=254)
    instructor_phone_number = models.CharField(max_length=50)




