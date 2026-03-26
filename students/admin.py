from django.contrib import admin
from .models import Teacher, Student

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
    search_fields = ['name', 'subject']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    filter_horizontal = ['teachers']
    search_fields = ['name']
    list_filter = ['age']
