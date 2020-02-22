from django.db import models

# Create your models here.
class Member(models.Model):
    u_id = models.IntegerField() 
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    institution = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

