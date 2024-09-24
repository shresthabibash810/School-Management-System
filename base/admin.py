from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(AcademicRecord)
admin.site.register(Attendance)
admin.site.register(Examination)
admin.site.register(Grade)
admin.site.register(Book)
admin.site.register(BookTransaction)
admin.site.register(Report)
