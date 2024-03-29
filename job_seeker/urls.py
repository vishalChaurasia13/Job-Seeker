"""job_seeker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import companiesRegistration,userRegistration

urlpatterns = [
    path('admin/', admin.site.urls),

# Corporate(company)

    path('companiesregistration/', companiesRegistration.companiesRegistrationInterface),
    path('companiesregistrationsubmit', companiesRegistration.companiesRegistrationSubmit),

    path('companylogin/', companiesRegistration.CompanyLogin),
    path('companyemailLogin/', companiesRegistration.CompanyEmailLogin),
    path('checkcompanyemailpassword', companiesRegistration.CheckCompanyEmailPassword),
    path('companylogout', companiesRegistration.CompanyLogout),
    #job post
    path('jobpost/', companiesRegistration.JobPost),
    path('jobpostsubmit', companiesRegistration.JobPostSubmit),
    path('joblist/', companiesRegistration.Joblist),
    path('applicant/', companiesRegistration.Applicant),
    path('applicantprofile', companiesRegistration.ApplicantProfile),

    #company search
    path('companysearch/', companiesRegistration.CompanySearch),

# User(With Login)

    path('userregistration/', userRegistration.userRegistrationInterface),
    path('userregistrationsubmit', userRegistration.userRegistrationSubmit),

    path('userlogin/', userRegistration.userLogin),
    path('useremailLogin/', userRegistration.userEmailLogin),
    path('checkuseremailpassword', userRegistration.CheckuserEmailPassword),
    path('userlogout', userRegistration.userLogout),
    path('usersearch/', userRegistration.UserSearch),

    path('profilesettings/', userRegistration.UserProfile),
    path('updatedprofile', userRegistration.UpdatedProfile),
    path('resume/', userRegistration.Resume),

    path('applyjob/', userRegistration.ApplyJob),
    path('appliedjob', userRegistration.AppliedJob),

    # User (Without Login)
    path('user/', userRegistration.userWithoutLogin),
]