from django.contrib import admin
from .models import StudentProfileInfo, TeacherProfileInfo
# Register your models here.

admin.site.register(StudentProfileInfo)
admin.site.register(TeacherProfileInfo)

