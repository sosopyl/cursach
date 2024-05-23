from django.contrib import admin
from .models import lesson, weeklesson, group, student,mark, Attendence

class lessonAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'lesson_type'] 

class markAdmin(admin.ModelAdmin):
    list_display = ['date', 'lesson', 'group'] 

class groupAdmin(admin.ModelAdmin):
    list_display = ['group', 'group_type', 'group_number'] 
class weeklessonAdmin(admin.ModelAdmin):
    list_display = ['lessonday', 'lesson_1', 'group_1', 'lesson_2', 'group_2', 'lesson_3', 'group_3', 'lesson_4', 'group_4'] 
class studentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'second_name', 'first_name', 'father_name', 'group', 'birthday'] 

admin.site.register(mark, markAdmin)
admin.site.register(lesson, lessonAdmin)  
admin.site.register(weeklesson, weeklessonAdmin) 
admin.site.register(group, groupAdmin) 
admin.site.register(student, studentAdmin) 
admin.site.register(Attendence) 