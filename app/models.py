from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class File(models.Model):
    file = models.FileField(null=True, default=None)

    def __str__(self):
        return self.file

class Institution(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Member(models.Model):
    u_id = models.ForeignKey(User, related_name='member', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    
    """
    Allowing institution to be null as superusers are also added
    in this model and filling institutionis not a requirement
    in django for them (naturally).

    Although, Institution should never be allowed to be blank.

    Therefore, you don't mix superusers with normal users. 
    """
    institution = models.ForeignKey(Institution, related_name='member', on_delete=models.CASCADE, null=True, blank=False)
    designation = models.CharField(max_length=200)
    image = models.ForeignKey(File, related_name='image_path', on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.username

class Field(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Topic(models.Model):
    field = models.ForeignKey(Field, related_name='topic', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Subject(models.Model):
    topic = models.ForeignKey(Topic, related_name='subject', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Curriculum(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(Member, related_name='curriculum', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='curriculum', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified']

class Bit(models.Model):

    BIT_CHOICES = [
        ('docx', 'Microsoft Word document'),
        ('pdf', 'PDF File'),
        ('zip', 'Compressed file (zip)'),
        ('video', 'Video file'),
        ('url', 'Weblink (URL)')
    ]

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(Member, related_name='bit', on_delete=models.CASCADE)
    bit_type = models.CharField(max_length=100, choices=BIT_CHOICES)
    curriculum = models.ForeignKey(Curriculum, related_name='bit', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)    
    description = models.CharField(max_length=1000, default="")
    file = models.ForeignKey(File, related_name='bit', on_delete=models.CASCADE, blank=True)
    text = models.CharField(max_length=2000, blank=True)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified']

class Comment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    member = models.ForeignKey(Member, related_name='comment', on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, related_name='comment', on_delete=models.CASCADE, null=True)
    bit = models.ForeignKey(Bit, related_name='comment', on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.comment

class ChangeLog(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(Member, related_name='changelog', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    curriculum = models.ForeignKey(Curriculum, related_name='changelog', on_delete=models.CASCADE, null=True)
    bit = models.ForeignKey(Bit, related_name='changelog', on_delete=models.CASCADE, null=True, blank=True, default=None)
    comment = models.ForeignKey(Comment, related_name='changelog', on_delete=models.CASCADE, blank=True, default=None)

    def __str__(self):
        return self.description

class Upvote(models.Model):
    member = models.ForeignKey(Member, related_name='upvote', on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, related_name='upvote', on_delete=models.CASCADE, null=True) 
    bit = models.ForeignKey(Bit, related_name='upvote', on_delete=models.CASCADE, null=True)
    changelog = models.ForeignKey(ChangeLog, related_name='upvote', on_delete=models.CASCADE, null=True)

class Subscription(models.Model):
    member = models.ForeignKey(Member, related_name='subscription', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='subscription', on_delete=models.CASCADE, null=True)
    curriculum = models.ForeignKey(Curriculum, related_name='subscription', on_delete=models.CASCADE, null=True)

class Teach(models.Model):
    member = models.ForeignKey(Member, related_name='teach', on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, related_name='teach', on_delete=models.CASCADE)