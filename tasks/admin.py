from django.contrib import admin
from .models import Task, Category

admin.site.register(Task)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)
    ordering = ('parent__name', 'name')

admin.site.register(Category, CategoryAdmin)