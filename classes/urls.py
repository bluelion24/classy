from django.conf.urls import url
from . import views

app_name = 'classes'
urlpatterns = [
    url(r'^$', views.class_list, name='class_list'),
    url(r'^(?P<course_id>[0-9]+)/$', views.class_detail, name='class_detail'),
   # url(r'^(?P<class_id>[0-9]+)/class_detail/$', views.class_detail, name='class_detail'),
    url(r'^class_list/$', views.class_list, name='class_list'),
    url(r'^(?P<student_id>[0-9]+)/student_detail/$', views.student_detail, name='student_detail'),
]
