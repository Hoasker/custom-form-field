import csv
from io import StringIO

from django.contrib import admin
from django.http import HttpResponse

from .models import ExtraInfo


class ExtraInfoAdmin(admin.ModelAdmin):
    actions = ['download_csv'] 
    list_display = ('user', 'student_group',)
    list_display_links = ('user', 'student_group',)
    list_filter = ('user',)
    search_fields = ('user', 'student_group',)
    list_per_page = 25  
    def download_csv(self, request, queryset,*args, **kwargs):
        import csv
        f = open('some.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(['user', 'student_group',])
        for s in queryset:
            writer.writerow([s.user, s.student_group])
        
        f.close()
        f = open('some.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response    
    download_csv.short_description = "Download CSV "



admin.site.register(ExtraInfo, ExtraInfoAdmin)
     
