from django.db import models
from accounts.models import StudentProfileInfo, TeacherProfileInfo
from django.utils.text import slugify
# Create your models here.
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=256, blank=False, unique=True)
    student = models.ManyToManyField('StudentMember', blank=True, related_name='student')
    instructor = models.ManyToManyField('TeacherMember', blank=True, related_name='tutor')
    slug = models.SlugField(allow_unicode=True, unique=True, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class StudentMember(models.Model):
    course = models.ForeignKey(Course, related_name='student_memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='student_group', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

    class Meta:
        unique_together = ['course', 'user']


class TeacherMember(models.Model):
    course = models.ForeignKey(Course, related_name='teacher_memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='teacher_group', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

    class Meta:
        unique_together = ['course', 'user']
