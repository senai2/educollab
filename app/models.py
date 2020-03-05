from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class File(models.Model):
    file = models.FileField()

    def __str__(self):
        return self.file.url

class Institution(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Member(models.Model):
    u_id = models.ForeignKey(User, related_name='member', on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    institution = models.ForeignKey(Institution, related_name='member', on_delete=models.CASCADE, blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(File, related_name='image_path', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.username

class Field(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Topic(models.Model):
    title = models.CharField(max_length=100)
    field = models.ForeignKey(Field, related_name='topic', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Subject(models.Model):
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, related_name='subject', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Curriculum(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, related_name='curriculum', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default="", blank=True)
    posted_by = models.ForeignKey(Member, related_name='curriculum', on_delete=models.CASCADE, default=1)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified']

class Bit(models.Model):
    title = models.CharField(max_length=100)
    bit_type = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, default="")
    file = models.ForeignKey(File, related_name='bit', on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=2000, blank=True)
    curriculum = models.ForeignKey(Curriculum, related_name='bit', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified']

class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    bit = models.ForeignKey(Bit, related_name='comment', on_delete=models.CASCADE, null=True)
    curriculum = models.ForeignKey(Curriculum, related_name='comment', on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(Member, related_name='comment', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.comment

class ChangeLog(models.Model):
    curriculum = models.ForeignKey(Curriculum, related_name='changelog', on_delete=models.CASCADE, null=True)
    bit = models.ForeignKey(Bit, related_name='changelog', on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=1000)
    comment = models.ForeignKey(Comment, related_name='changelog', on_delete=models.CASCADE)
    member = models.ForeignKey(Member, related_name='changelog', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.description

class Upvote(models.Model):
    bit = models.ForeignKey(Bit, related_name='upvote', on_delete=models.CASCADE, null=True)
    curriculum = models.ForeignKey(Curriculum, related_name='upvote', on_delete=models.CASCADE, null=True) 
    member = models.ForeignKey(Member, related_name='upvote', on_delete=models.CASCADE)
    changelog = models.ForeignKey(ChangeLog, related_name='upvote', on_delete=models.CASCADE, null=True)

class Subscription(models.Model):
    curriculum = models.ForeignKey(Curriculum, related_name='subscription', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, related_name='subscription', on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(Member, related_name='subscription', on_delete=models.CASCADE)

class Teach(models.Model):
    curriculum = models.ForeignKey(Curriculum, related_name='teach', on_delete=models.CASCADE)
    member = models.ForeignKey(Member, related_name='teach', on_delete=models.CASCADE)