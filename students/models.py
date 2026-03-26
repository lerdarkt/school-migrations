from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя учителя")
    subject = models.CharField(max_length=100, verbose_name="Предмет")
    
    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
    
    def __str__(self):
        return f"{self.name} ({self.subject})"

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя ученика")
    age = models.IntegerField(verbose_name="Возраст")
    teachers = models.ManyToManyField(
        Teacher, 
        related_name='students',
        verbose_name="Учителя",
        blank=True
    )
    
    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"
    
    def __str__(self):
        return self.name
