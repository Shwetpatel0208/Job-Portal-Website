from django.db import models
from django.contrib.auth.models import User
class contact_details(models.Model):
    message=models.TextField()
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    requirements = models.TextField()
    logo = models.ImageField(upload_to="company_logos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="job_applications",  # unique
        null=True,
        blank=True
    )
    name = models.CharField(max_length=150)
    email = models.EmailField()
    resume = models.FileField(upload_to="resumes/")
    applied_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("reviewing", "Reviewing"),
        ("shortlisted", "Shortlisted"),
        ("rejected", "Rejected"),
        ("hired", "Hired"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="submitted")

    def __str__(self):
        return f"{self.name} applied for {self.job.title}"

class Job1(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    requirements = models.TextField()
    logo = models.ImageField(upload_to="company_logos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
class JobApplication1(models.Model):
    job = models.ForeignKey(Job1, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="job1_applications",  # unique
        null=True,
        blank=True
    )
    name = models.CharField(max_length=150)
    email = models.EmailField()
    resume = models.FileField(upload_to="resumes/")
    applied_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("reviewing", "Reviewing"),
        ("shortlisted", "Shortlisted"),
        ("rejected", "Rejected"),
        ("hired", "Hired"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="submitted")
    def __str__(self):
        return f"{self.name} applied for {self.job.title}"
# Create your models here.
class Job2(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    requirements = models.TextField()
    logo = models.ImageField(upload_to="company_logos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
class JobApplication2(models.Model):
    job = models.ForeignKey(Job2, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="job2_applications",  # unique
        null=True,
        blank=True
    )
    name = models.CharField(max_length=150)
    email = models.EmailField()
    resume = models.FileField(upload_to="resumes/")
    applied_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("reviewing", "Reviewing"),
        ("shortlisted", "Shortlisted"),
        ("rejected", "Rejected"),
        ("hired", "Hired"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="submitted")
    def __str__(self):
        return f"{self.name} applied for {self.job.title}"
# Create your models here.
class Job3(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    requirements = models.TextField()
    logo = models.ImageField(upload_to="company_logos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
class JobApplication3(models.Model):
    job = models.ForeignKey(Job3, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="job3_applications",  # unique
        null=True,
        blank=True
    )
    name = models.CharField(max_length=150)
    email = models.EmailField()
    resume = models.FileField(upload_to="resumes/")
    applied_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("reviewing", "Reviewing"),
        ("shortlisted", "Shortlisted"),
        ("rejected", "Rejected"),
        ("hired", "Hired"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="submitted")

    def __str__(self):
        return f"{self.name} applied for {self.job.title}"
# Create your models here.
class alljob(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    requirements = models.TextField()
    logo = models.ImageField(upload_to="company_logos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
class alljobApplication(models.Model):
    job = models.ForeignKey(alljob, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="alljob_applications",  # unique
        null=True,
        blank=True
    )
    name = models.CharField(max_length=150)
    email = models.EmailField()
    resume = models.FileField(upload_to="resumes/")
    applied_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("reviewing", "Reviewing"),
        ("shortlisted", "Shortlisted"),
        ("rejected", "Rejected"),
        ("hired", "Hired"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="submitted")

    def __str__(self):
        return f"{self.name} applied for {self.job.title}"
class CVUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # link to registered user
    cv = models.FileField(upload_to="cvs/")  # files saved in MEDIA_ROOT/cvs/
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.cv.name}"
# Create your models here.
