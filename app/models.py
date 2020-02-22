from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.FileField()

    def __str__(self):
        return self.image.url

class Institution(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Member(models.Model):
    u_id = models.IntegerField() 
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    institution = models.ForeignKey(Institution, related_name='member', on_delete=models.CASCADE)
    designation = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    # image = models.ForeignKey(Image, related_name='image_path', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

class Field(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Topic(models.Model):
    title = models.CharField(max_length=100)
    field = models.ForeignKey(Field, related_name='topic', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Curriculum(models.Model):
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, related_name='curriculum', on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, related_name='curriculum', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default="")
    posted_by = models.ForeignKey(Member, related_name='curriculum', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title