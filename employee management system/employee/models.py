from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save #  the signal  when the user is newly added 
from django.dispatch import receiver # to recieve the signal  .. decorator 

# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE) # 1 to 1 relation , one user ne profile 
    designation =models.CharField(max_length=20, null=False, blank=False)  #null = fale : there  has to be a defualt value 
    salary= models.IntegerField(null=True,blank=True)

    class Meta:
        ordering = ('-salary',) # -ve : salary in descending order 

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)
    
@receiver(post_save, sender=User)   # when the signal is send from post save, this method/function is executeed 
def user_is_created(sender,instance, created, **kwargs):
    print(created)
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

    
