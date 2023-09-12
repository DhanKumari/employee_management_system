from django.contrib import admin
from poll.models import *

# Register your models here.

admin.site.register(Question) # models present in  polls model 
admin.site.register(Choice)
admin.site.register(Answer)

