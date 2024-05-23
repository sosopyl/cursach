from django.shortcuts import render
from .models import *
from datetime import datetime, timedelta
from django.http import HttpResponse
from .utils import menu
from .forms import checking, marks
from django.views.generic import DetailView
from django.shortcuts import redirect


# def modelmultiplechoicefield(request):
#     form = checking(request.POST or None)
#     groupes = group.objects.all()
#     if request.POST and form.is_valid():
#         date = form.cleaned_data['date']
#         lessons = form.cleaned_data['lessons']
#         groups = form.cleaned_data['groups']
        
#         obj = check(
#             date=date, 
#             lessons = lessons, 
#             groups = groups,
#         )

#         obj.save()
#         form2 = checking(request.POST, instance=obj)
#         form2.save(commit=False)
#         form2.save_m2m()
#         return render(request, 'main/groups.html', {'groups': groups})

#     context = {'form':form,
#                'groups': groupes}
#     return render(request, 'main/groups.html', context)

def main(request):
    lessons = weeklesson.objects.all()
    groups = group.objects.all()
    today = datetime.date(datetime.today())
    tomorrow = datetime.date(datetime.today() + timedelta(days=1))
    weektoday = (datetime.weekday(datetime.today()))+1
    nextweektoday = (datetime.weekday(datetime.today()))+2
    return render(request, 'main/main.html', { 'groups':groups, 'lessons': lessons, 'today': today, 'weektoday': weektoday, 'tomorrow': tomorrow, 'nextweektoday': nextweektoday})

def notify(request):
    return render(request, 'main/notify.html')

# def marks(request, group):
#     data = {'weeklessons': weeklessons, 
#             'lessons': lessons, 
#             'groups': groups, 
#             'students':students,
#             'checks': check}
#     return render(request, 'main/checking_students.html',data )
def checkin(request):
    if request.method == 'POST':
        form = marks(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('main')
            except:
                form.add_error('Данные урока не созранены')
    else:
        form = marks()
    students = student.objects.all()
    weeklessons = weeklesson.objects.all()
    groups = group.objects.all()
    lessons = lesson.objects.all()
    data = {'weeklessons': weeklessons, 
            'lessons': lessons, 
            'groups': groups, 
            'students':students,
            'checking': checking, 
            'marks': marks}
    return render(request, 'main/checking_students.html',data )

def lessons(request):
    lessons = lesson.objects.all()
    return render(request, 'main/lessons.html', {'lessons': lessons})

def classes(request):
    groups = group.objects.all()
    return render(request, 'main/groups.html', {'groups': groups})