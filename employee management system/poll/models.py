from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.TextField(null=True, blank=True)
    status = models.CharField(default='inactive',max_length=10) # CharField therefore we need to add length
    created_by= models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE) # which hr created .. foreignkey means 1 HR(user) can create mulptiple question
    # on_delete . imagine 2 hr, when one hr is delete we have to remove all the field 

    start_date= models.DateTimeField(null=True, blank=True)
    end_date= models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) # Tracks when it was updated last 

    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choice_set.all() # Returns all the choices 

class Choice(models.Model):
    question= models.ForeignKey('poll.Question',on_delete=models.CASCADE) #app name , class
    text = models.TextField(null=True, blank=True)  

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.text
    
    @property
    def votes(self):
        return self.answer_set.count()
    
    
class Answer(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    choice=models.ForeignKey(Choice, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.user.first_name + '-'+ self.choice.text  # showing the ans 
        


