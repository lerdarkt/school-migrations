from django.shortcuts import render
from .models import Student

def student_list(request):
    """Отображает список всех учеников с их учителями"""
    students = Student.objects.all().prefetch_related('teachers')
    return render(request, 'students/student_list.html', {'students': students})
