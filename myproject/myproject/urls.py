"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('blog/',views.blog),
    path('contact/',views.contact),
    path('',views.index),
    path('elements/',views.elements),
    path("upload-cv/", views.upload_cv, name="upload_cv"),
    path('job_listing/',views.job_listing),
    path('single-blog/',views.singleblog),
    path("register/", views.register_page, name="register"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path('design_creative/',views.design_creative,name="design_creative"),
    path('design_development/',views.design_development,name="design_development"),
    path('digital_marketing/',views.digital_marketing,name="digital_marketing"),
    path('mobile_application/',views.mobile_application,name="mobile_application"),
    path("apply/<int:job_id>/", views.apply_page, name="apply_page"),
    path("apply1/<int:job_id1>/", views.apply_page1, name="apply_page1"),
    path("apply2/<int:job_id2>/", views.apply_page2, name="apply_page2"),
    path("apply3/<int:job_id3>/", views.apply_page3, name="apply_page3"),
     path("apply4/<int:job_id3>/", views.apply_page4, name="apply_page4"),
    path("apply5/<int:job_id3>/", views.apply_page5, name="apply_page5"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
