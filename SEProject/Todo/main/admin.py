from django.contrib import admin
from .models import Task, List


class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cr_date', 'due_date', 'owner', 'mark', 'list_id')
    list_display_links = ('id', 'name', 'cr_date', 'due_date', 'owner', 'mark', 'list_id')


admin.site.register(Task, TaskAdmin)
admin.site.register(List, ListAdmin)