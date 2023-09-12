from django.urls import path
from employee import views 


urlpatterns = [
    path('', views.home,name="employee_home"),
]
