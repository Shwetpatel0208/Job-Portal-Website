from django.contrib import admin
from myapp.models import contact_details,Job,JobApplication,JobApplication1,Job1,JobApplication2,Job2,JobApplication3,Job3,alljob,alljobApplication,CVUpload
admin.site.register(contact_details)
admin.site.register(Job)
admin.site.register(JobApplication)
admin.site.register(Job1)
admin.site.register(JobApplication1)
admin.site.register(Job2)
admin.site.register(JobApplication2)
admin.site.register(Job3)
admin.site.register(JobApplication3)
admin.site.register(alljob)
admin.site.register(alljobApplication)
# Register your models here.
 

@admin.register(CVUpload)
class CVUploadAdmin(admin.ModelAdmin):
    list_display = ("user", "cv", "uploaded_at")
