from django.shortcuts import render
from .models import Group, GroupMember
from django.utils.text import slugify
from .forms import GroupCreateForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
import misaka


def CreateGroup(request):
    if request.method == 'POST':
        create_form = GroupCreateForm(request.POST)
        if create_form.is_valid:
            group_form = create_form.save(commit=False)
            group_form.slug = slugify(group_form.name)
            group_form.description_html = misaka.html(group_form.description)
            #group_form.members.add(request.user)
            group_form.save()
            
            return HttpResponseRedirect(reverse('index'))
        else:
            print(create_form.errors)
    else:
        create_form = GroupCreateForm()
    return render(request, 'groups/../../social_copy1/groups/templates/groups/group_create.html', {'create_form': create_form})
            

def GroupList(request):
    group_list = Group.objects.all()
    return render(request, 'groups/../../social_copy1/groups/templates/groups/group_list.html', {'group_list': group_list})


def GroupSingle(request, slug):
    group = Group.objects.get(slug=slug)
    return render(request, 'groups/../../social_copy1/groups/templates/groups/group_single.html', {'group':group})


def GroupJoin(request, slug):
    group = Group.objects.get(slug=slug)
    group_member = GroupMember.objects.create(group=group.name, user=request.User)
    group_mem = group_member.save()
    group.members.add(group_mem)
    return HttpResponseRedirect(reverse('groups:group_single', slug=slug))
