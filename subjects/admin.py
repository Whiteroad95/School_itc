from django.contrib import admin

from .models import School, ClassGroup, Students, Lessons


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['director', 'senior_teachers', 'teachers', 'classes', 'students', 'teacher']


admin.site.register(School, SchoolAdmin)
admin.site.register(ClassGroup)
admin.site.register(Students)
admin.site.register(Lessons)
