from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from myapp.models import (
    contact_details,
    Job, JobApplication,
    Job1, JobApplication1,
    Job2, JobApplication2,
    Job3, JobApplication3,
    alljob, alljobApplication,
    CVUpload,
)

# ✅ Common admin for all Job Applications
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("job", "user", "name", "email", "applied_at", "status")
    list_filter = ("status", "applied_at", "job")
    search_fields = ("name", "email", "job__title", "job__company")
    list_editable = ("status",) 
    # ✅ Override save_model to send email when status changes
    def save_model(self, request, obj, form, change):
        if change:  # only on update
            old_obj = type(obj).objects.get(pk=obj.pk)
            if old_obj.status != obj.status:  # status changed
                subject = f"Update on your Job Application - {obj.job.title}"
                message = f"""
Hello {obj.name},

Your application status for the job "{obj.job.title}" at {obj.job.company} has been updated.

Previous Status: {old_obj.status.capitalize()}
New Status: {obj.status.capitalize()}

Thank you for applying with us!

Best Regards,
Job Finder Team
"""
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,  # sender (must be set in settings.py)
                    [obj.email],
                    fail_silently=False,
                )
        super().save_model(request, obj, form, change)

# ✅ Register Job Models
admin.site.register(contact_details)
admin.site.register(Job)
admin.site.register(Job1)
admin.site.register(Job2)
admin.site.register(Job3)
admin.site.register(alljob)

# ✅ Register Job Application Models with status
admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(JobApplication1, JobApplicationAdmin)
admin.site.register(JobApplication2, JobApplicationAdmin)
admin.site.register(JobApplication3, JobApplicationAdmin)
admin.site.register(alljobApplication, JobApplicationAdmin)

# ✅ Register CV Upload
@admin.register(CVUpload)
class CVUploadAdmin(admin.ModelAdmin):
    list_display = ("user", "cv", "uploaded_at")
    search_fields = ("user__username",)
    list_filter = ("uploaded_at",)


