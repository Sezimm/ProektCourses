from django.contrib import admin
from .models import  *

class Science_CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_all', 'price_month', 'period')

class Students_ScienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'age', 'email', 'phone')

class Teachers_ScienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'age', 'email', 'phone')

admin.site.register(Science_Courses, Science_CoursesAdmin)
admin.site.register(Students_Science, Students_ScienceAdmin)
admin.site.register(Teachers_Science, Teachers_ScienceAdmin)
