from django.contrib import admin
from .models import Member, Image, Field, Topic, Curriculum, Institution

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
