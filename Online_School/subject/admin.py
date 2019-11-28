from django.contrib import admin
from .models import Course, StudentMember, TeacherMember
# Register your models here.

admin.site.register(Course)
admin.site.register(StudentMember)
admin.site.register(TeacherMember)