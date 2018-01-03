from django.conf.urls import url

from . import views

app_name = 'shopping_cart'

urlpatterns = [
    url(r'^$', views.landing_page, name='landing_page' ),
    url(r'^shopping_cart/(?P<course_id>[0-9]+)$', views.shopping_cart, name='shopping_cart' ),
    url(r'^(?P<course_id>[0-9]+)$', views.class_detail, name='class_detail' ),
    url(r'^healthcare_provider$', views.healthcare_provider, name='healthcare_provider' ),
    url(r'^bls_course$', views.bls_course, name='bls_course'),
    url(r'^class_detail$', views.class_detail, name='class_detail' ),
]

