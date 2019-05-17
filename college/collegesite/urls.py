from django.conf.urls import url
from . import views


app_name = 'collegesite'
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^student_application/$', views.student_application, name='student_application'),
    url(r'^student_registartion/$', views.student_registartion,name='student_registartion'),
    url(r'^staff_registration/$', views.staff_registration, name='staff_registration'),
    url(r'login/$', views.user_login, name='user_login'),
    url(r'logout/$', views.user_logout, name='user_logout'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^staff_profile/$', views.staff_profile, name ='staff_profile'),
    url(r'student_profile/$', views.student_profile, name='student_profile'),
    url(r'students/$', views.students, name="students"),
    url(r'staff_department/$', views.staff_department, name='staff_department'),
    url(r'staff', views.staff, name='staff'),
    #url(r'^student_login/$', views.student_login, name='student_login'),
]
