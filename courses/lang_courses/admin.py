from django.contrib import admin
from .models import  *

class Lang_CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_all', 'price_month', 'period')

class Students_LangAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'age', 'email', 'phone')

class Teachers_LangAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'age', 'email', 'phone')

admin.site.register(Lang_Courses, Lang_CoursesAdmin)
admin.site.register(Students_Lang, Students_LangAdmin)
admin.site.register(Teachers_Lang, Teachers_LangAdmin)
