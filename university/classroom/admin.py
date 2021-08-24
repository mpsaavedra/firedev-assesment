from django.contrib import admin
from .models import City, ClassRoom, Student, Teacher


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass