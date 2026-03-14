from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.models import contact_details
from django.core.mail import send_mail
from myapp.models import Job,JobApplication,Job1,JobApplication1,Job2,JobApplication2,Job3,JobApplication3,alljob,alljobApplication,CVUpload
from django.conf import settings
from django.contrib.auth.decorators import login_required
from itertools import chain


def about(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    if request.method == "POST":
        message=request.POST.get("message")
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        c=contact_details(message=message,name=name,email=email,subject=subject)
        c.save()
    return render(request,"contact.html")

def index(request):
    jobs=alljob.objects.all()
    data={
        "jobs":jobs
    }
    return render(request,"index.html",data)

@login_required
def applied_page(request):
    # Applications with user field
    applications_main = JobApplication.objects.filter(user=request.user)

    # Applications without user field (fallback: filter by email = user.email)
    applications1 = JobApplication1.objects.filter(email=request.user.email)
    applications2 = JobApplication2.objects.filter(email=request.user.email)
    applications3 = JobApplication3.objects.filter(email=request.user.email)
    applications_all = alljobApplication.objects.filter(email=request.user.email)

    # Combine all applications
    applications = sorted(
        chain(applications_main, applications1, applications2, applications3, applications_all),
        key=lambda x: x.applied_at,
        reverse=True
    )

    return render(request, "applied.html", {"applications": applications})

def job_listing(request):
    jobs=alljob.objects.all()
    data={
        "jobs":jobs
    }
    return render(request,"job_listing.html",data)

def singleblog(request):
    return render(request,"single-blog.html")

def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")

        if password != password1:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("register")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # ✅ Send Welcome Email
        subject = "Welcome to JobFlnder!"
        message = f"Hi {username},\n\nThank you for registering at Jobflnder. You can now log in and start applying for jobs!"
        from_email = None  # will use DEFAULT_FROM_EMAIL
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        messages.success(request, "Registration successful. Please check your email and login.")
        return redirect("login")

    return render(request, "register.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")
            return redirect("/")  # redirect to homepage
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "login.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("/")

def design_creative(request):
    jobs=Job.objects.all()
    data={
        "jobs":jobs
    }
    return render(request, "design_creative.html",data)

def design_development(request):
    jobs=Job1.objects.all()
    data={
        "jobs":jobs
    }
    return render(request, "design_development.html",data)

def digital_marketing(request):
    jobs=Job3.objects.all()
    data={
        "jobs":jobs
    }
    return render(request, "digital_marketing.html",data)

def mobile_application(request):
    jobs=Job2.objects.all()
    data={
        "jobs":jobs
    }
    return render(request, "mobile_application.html",data)
def apply_page(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        resume = request.FILES.get("resume")

        # Save the application
        JobApplication.objects.create(
    job=job,
    user=request.user,   # ✅ save logged-in user
    name=name,
    email=email,
    resume=resume
)

        # ✅ Send confirmation email to user
        subject = f"Application Confirmation - {job.title}"
        message = f"""
        Dear {name},

        Thank you for applying for the position "{job.title}" at {job.company}.
        We have successfully received your application.

        Our HR team will review your resume and contact you soon.

        Regards,
        {job.company} HR Team
        """
        from_email = settings.EMAIL_HOST_USER   # replace with your email
        recipient_list = [email]               # send to applicant’s email

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except Exception as e:
            messages.warning(request, f"Application saved, but email could not be sent: {e}")

        messages.success(request, "Your application has been submitted successfully! A confirmation email has been sent.")
        return redirect("/")

    return render(request, "apply.html", {"job": job})
def apply_page1(request, job_id1):
    job = get_object_or_404(Job1, id=job_id1)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        resume = request.FILES.get("resume")

        # Save the application
        JobApplication1.objects.create(
    job=job,
    user=request.user,   # ✅ save logged-in user
    name=name,
    email=email,
    resume=resume
)
        # ✅ Send confirmation email to user
        subject = f"Application Confirmation - {job.title}"
        message = f"""
        Dear {name},

        Thank you for applying for the position "{job.title}" at {job.company}.
        We have successfully received your application.

        Our HR team will review your resume and contact you soon.

        Regards,
        {job.company} HR Team
        """
        from_email = settings.EMAIL_HOST_USER   # replace with your email
        recipient_list = [email]               # send to applicant’s email

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except Exception as e:
            messages.warning(request, f"Application saved, but email could not be sent: {e}")

        messages.success(request, "Your application has been submitted successfully! A confirmation email has been sent.")
        return redirect("/")

    return render(request, "apply1.html", {"job": job})
def apply_page2(request, job_id2):
    job = get_object_or_404(Job2, id=job_id2)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        resume = request.FILES.get("resume")

        # Save the application
        JobApplication2.objects.create(
    job=job,
    user=request.user,   # ✅ save logged-in user
    name=name,
    email=email,
    resume=resume
)

        # ✅ Send confirmation email to user
        subject = f"Application Confirmation - {job.title}"
        message = f"""
        Dear {name},

        Thank you for applying for the position "{job.title}" at {job.company}.
        We have successfully received your application.

        Our HR team will review your resume and contact you soon.

        Regards,
        {job.company} HR Team
        """
        from_email = settings.EMAIL_HOST_USER   # replace with your email
        recipient_list = [email]               # send to applicant’s email

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except Exception as e:
            messages.warning(request, f"Application saved, but email could not be sent: {e}")

        messages.success(request, "Your application has been submitted successfully! A confirmation email has been sent.")
        return redirect("/")

    return render(request, "apply2.html", {"job": job})
def apply_page3(request, job_id3):
    job = get_object_or_404(Job3, id=job_id3)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        resume = request.FILES.get("resume")

        # Save the application
        JobApplication3.objects.create(
    job=job,
    user=request.user,   # ✅ save logged-in user
    name=name,
    email=email,
    resume=resume
)

        # ✅ Send confirmation email to user
        subject = f"Application Confirmation - {job.title}"
        message = f"""
        Dear {name},

        Thank you for applying for the position "{job.title}" at {job.company}.
        We have successfully received your application.

        Our HR team will review your resume and contact you soon.

        Regards,
        {job.company} HR Team
        """
        from_email = settings.EMAIL_HOST_USER   # replace with your email
        recipient_list = [email]               # send to applicant’s email

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except Exception as e:
            messages.warning(request, f"Application saved, but email could not be sent: {e}")

        messages.success(request, "Your application has been submitted successfully! A confirmation email has been sent.")
        return redirect("/")

    return render(request, "apply2.html", {"job": job})
def apply_page4(request, job_id3):
    job = get_object_or_404(alljob, id=job_id3)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        resume = request.FILES.get("resume")

        # Save the application
        alljobApplication.objects.create(
    job=job,
    user=request.user,   # ✅ save logged-in user
    name=name,
    email=email,
    resume=resume
)

        # ✅ Send confirmation email to user
        subject = f"Application Confirmation - {job.title}"
        message = f"""
        Dear {name},

        Thank you for applying for the position "{job.title}" at {job.company}.
        We have successfully received your application.

        Our HR team will review your resume and contact you soon.

        Regards,
        {job.company} HR Team
        """
        from_email = settings.EMAIL_HOST_USER   # replace with your email
        recipient_list = [email]               # send to applicant’s email

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except Exception as e:
            messages.warning(request, f"Application saved, but email could not be sent: {e}")

        messages.success(request, "Your application has been submitted successfully! A confirmation email has been sent.")
        return redirect("/")

    return render(request, "apply4.html", {"job": job})
def apply_page5(request, job_id3):
    job = get_object_or_404(alljob, id=job_id3)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        resume = request.FILES.get("resume")

        # Save the application
        alljobApplication.objects.create(
            job=job,
            name=name,
            email=email,
            resume=resume
        )

        # ✅ Send confirmation email to user
        subject = f"Application Confirmation - {job.title}"
        message = f"""
        Dear {name},

        Thank you for applying for the position "{job.title}" at {job.company}.
        We have successfully received your application.

        Our HR team will review your resume and contact you soon.

        Regards,
        {job.company} HR Team
        """
        from_email = settings.EMAIL_HOST_USER   # replace with your email
        recipient_list = [email]               # send to applicant’s email

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except Exception as e:
            messages.warning(request, f"Application saved, but email could not be sent: {e}")

        messages.success(request, "Your application has been submitted successfully! A confirmation email has been sent.")
        return redirect("/")

    return render(request, "apply5.html", {"job": job})
@login_required
def upload_cv(request):
    if request.method == "POST":
        cv_file = request.FILES.get("cv")
        if cv_file:
            CVUpload.objects.create(user=request.user, cv=cv_file)
            messages.success(request, "Your CV has been uploaded successfully!")
        else:
            messages.error(request, "Please select a file to upload.")
        return redirect("/")  # redirect wherever you like
def myaccount(request):
    return render(request,"myaccount.html",{"user": request.user})

