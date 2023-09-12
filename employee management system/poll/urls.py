from django.urls import path
from poll.views import *

urlpatterns = [
    path('',index, name='polls_list' ),
    path('<int:id>/details/', details, name="poll_details"),
    path('<int:id>/', random, name="single_poll"),

    
]
