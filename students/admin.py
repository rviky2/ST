from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'registration_number', 'grade')
    search_fields = ('first_name', 'last_name', 'email', 'registration_number')
    list_filter = ('grade', 'date_joined')
