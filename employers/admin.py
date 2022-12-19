from django.contrib import admin
from .models import Headmaster, Teachers, Headteacher


class HeadmasterAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'photo', 'number']


admin.site.register(Headmaster, HeadmasterAdmin)


class TeachersAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'photo', 'number', 'address']


admin.site.register(Teachers, TeachersAdmin)


class HeadteacherAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'photo', 'number']


admin.site.register(Headteacher, HeadteacherAdmin)