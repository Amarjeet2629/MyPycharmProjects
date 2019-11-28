from django.shortcuts import render
from .models import Course, TeacherMember, StudentMember
from accounts.models import StudentProfileInfo, TeacherProfileInfo
from .forms import CourseCreateForm
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def CourseList(request):
    list = Course.objects.all()
    return render(request, 'subject/course_list.html', {'list': list})


@login_required
def CourseCreate(request):
    if request.method == 'POST':
        course_create_form = CourseCreateForm(request.POST)
        if course_create_form.is_valid():
            course_form = course_create_form.save(commit=False)
            course_form.slug = slugify(course_form.name)
            course_form.save()
            return HttpResponseRedirect(reverse('subject:course_list'))
        else:
            return course_create_form.errors
    else:
        course_create_form = CourseCreateForm()
        return render(request, 'subject/course_create.html', {'course_create_form': course_create_form})


def CourseDetail(request, slug):
    obj = Course.objects.get(slug=slug)
    return render(request, 'subject/course_detail.html', {'obj': obj})



@login_required
def CourseJoin(request, slug):
    course = Course.objects.get(slug=slug)
    user = request.user
    obj1 = StudentProfileInfo.objects.filter(user=request.user).exists()
    obj2 = TeacherProfileInfo.objects.filter(user=request.user).exists()

    if obj1:
        new_member = StudentMember(course=course, user=request.user)
        new_member.save()
        course.student.add(new_member)
        return HttpResponseRedirect(reverse('subject:course_detail', kwargs={'slug': slug}))
    else:
        new_member = TeacherMember(course=course, user=request.user)
        new_member.save()
        course.teacher.add(new_member)
        return HttpResponseRedirect(reverse('subject:course_detail', kwargs={'slug': slug}))


@login_required
def CourseLeave(request, slug):
    course = Course.objects.get(slug=slug)
    user = request.user
    obj1 = StudentProfileInfo.objects.filter(user=request.user).exists()
    obj2 = TeacherProfileInfo.objects.filter(user=request.user).exists()

    if obj1:
        mem = get_object_or_404(StudentMember, user=user)
        course.student.remove(mem)
        mem.delete()
        return HttpResponseRedirect(reverse('subject:course_detail', kwargs={'slug': slug}))
    else:
        mem = get_object_or_404(TeacherMember, user=user)
        course.instructor.remove(mem)
        mem.delete()
        return HttpResponseRedirect(reverse('subject:course_detail', kwargs={'slug': slug}))

