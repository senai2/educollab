from django.contrib import admin
from .models import Member, File, Field, Topic, Curriculum, Institution, Bit, Comment, Upvote, Subscription, Subject

# Register your models here.

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')

admin.site.register(Institution, InstitutionAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'u_id', 'institution', 'designation')

admin.site.register(Member, MemberAdmin)

class FieldAdmin(admin.ModelAdmin):
    list_display = ('title','id')

admin.site.register(Field, FieldAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'field', 'id')

admin.site.register(Topic, TopicAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'id')

admin.site.register(Subject, SubjectAdmin)

class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_by', 'subject', 'id')

admin.site.register(Curriculum, CurriculumAdmin)

class BitAdmin(admin.ModelAdmin):
    list_display = ('title','curriculum', 'id')

admin.site.register(Bit, BitAdmin)

class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'id')

admin.site.register(File, FileAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'bit', 'member', 'id')

admin.site.register(Comment, CommentAdmin)

class UpvoteAdmin(admin.ModelAdmin):
    list_display = ('bit', 'member', 'id')

admin.site.register(Upvote, UpvoteAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('curriculum', 'member', 'id')

admin.site.register(Subscription, SubscriptionAdmin)