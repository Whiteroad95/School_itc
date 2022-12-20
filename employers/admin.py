from django.contrib import admin
from .models import Headmaster, Teachers, Headteacher
from django.utils.safestring import mark_safe


class HeadmasterAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'get_image', 'number']
    search_fields = ['name_surname', 'number']
    list_display_links = ['name_surname']
    list_editable = ['number']
    list_filter = ['number']

    def get_image(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' weight='150' height='200'>")
        return 'Images not found!'


admin.site.register(Headmaster, HeadmasterAdmin)


class TeachersAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'photo', 'number', 'address']


admin.site.register(Teachers, TeachersAdmin)


class HeadteacherAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'photo', 'number']


admin.site.register(Headteacher, HeadteacherAdmin)
