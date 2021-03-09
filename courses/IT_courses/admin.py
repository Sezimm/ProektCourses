from django.contrib import admin
from .models import  *

class Prog_LangAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_all', 'price_month', 'period')

class Students_ITAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'age', 'email', 'phone')

class Teachers_ITAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'age', 'email', 'phone')

admin.site.register(Prog_Lang, Prog_LangAdmin)
admin.site.register(Students_IT, Students_ITAdmin)
admin.site.register(Teachers_IT, Teachers_ITAdmin)