from django.contrib import admin
from .models import Member, File, Field, Topic, Curriculum, Institution, Bit, Comment, Upvote, FileType

# Register your models here.

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')

admin.site.register(Institution, InstitutionAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'u_id', 'institution', 'designation')

admin.site.register(Member, MemberAdmin)

class FieldAdmin(admin.ModelAdmin):
    list_display = ('title','id')

admin.site.register(Field, FieldAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'field', 'id')

admin.site.register(Topic, TopicAdmin)

class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_by', 'topic','institution', 'id')

admin.site.register(Curriculum, CurriculumAdmin)

class BitAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_type','curriculum', 'id')

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

admin.site.register(FileType)