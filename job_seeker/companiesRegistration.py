from django.shortcuts import render,redirect,HttpResponse
from . import pool

from django.views.decorators.clickjacking import xframe_options_exempt

# corporate....................................

@xframe_options_exempt
def companiesRegistrationInterface(request):
    return render(request,"companiesRegistration.html",{'msg':''})

@xframe_options_exempt
def companiesRegistrationSubmit(request):
   try:
     db,cmd=pool.ConnectionPooling()
     cname=request.POST['cname']
     type=request.POST['type']
     category=request.POST['category']
     contact=request.POST['contact']
     email=request.POST['email']
     address=request.POST['address']
     password=request.POST['password']

     q="insert into companies(cname,type,category,contact,email,address,password) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(cname,type,category,contact,email,address,password)

     print(q)
     cmd.execute(q)
     db.commit()
     db.close()
     return render(request, "companiesRegistration.html", {'msg': 'Registered'})
   except Exception as e:
     print(e)
     return render(request, "companiesRegistration.html", {'msg': 'Fail to Submit Record'})

def CompanyLogin(request):
  return render(request, "companyLoginPage.html", {'msg': ''})

def CompanyEmailLogin(request):
  return render(request,"companyemailLogin.html")

def CheckCompanyEmailPassword(request):
 try:
  db, cmd = pool.ConnectionPooling()
  email = request.POST['email']
  password = request.POST['password']

  q = "Select * from companies where email='{0}' and password='{1}'".format(email, password)
  cmd.execute(q)
  data = cmd.fetchone()
  if (data):
    request.session['company']=data
    return render(request,"companyProfile.html",{'msg':email,'data':data})
  else:
    return render(request, "companyLoginPage.html", {'msg': 'Invalid EmailId/Password'})
 except Exception as e:
   print(e)
   return render(request, 'companyLoginPage.html', {'msg': 'Server Error'})

def CompanyLogout(request):
    del request.session['company']
    return redirect('/companylogin')

@xframe_options_exempt
def JobPost(request):
    return render(request,"jobpost.html",{'msg':''})

@xframe_options_exempt
def JobPostSubmit(request):
    try:
        db, cmd = pool.ConnectionPooling()

        title=request.POST['title']
        cname = request.POST['cname']
        contact = request.POST['contact']
        email = request.POST['email']
        location = request.POST['location']
        lastdate = request.POST['lastdate']
        type = request.POST['type']
        category = request.POST['category']
        duration = request.POST['duration']
        qualification = request.POST['qualification']
        skills = request.POST['skills']
        experience = request.POST['experience']
        salary = request.POST['salary']
        description=request.POST['description']
        iconfile = request.FILES['icon']

        q = "insert into jobpost(jobtitle,cname,contact,email,location,lastdate,jobtype,jobcategory,jobduration,qualification,skills,workexperience,salary,jobdescription,icon) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}')".format(title,cname,contact,email,location,lastdate,type,category,duration,qualification,skills,experience,salary,description, iconfile.name)

        print(q)
        cmd.execute(q)
        db.commit()
        F = open("D:/3.Projects/job_seeker/assets/" + iconfile.name, "wb")
        for chunk in iconfile.chunks():
            F.write(chunk)
        F.close()
        db.close()
        return render(request, "jobpost.html", {'msg': 'Record Submitted'})
    except Exception as e:
        print(e)
        return render(request, "jobpost.html", {'msg': 'Fail to Submit Record'})

@xframe_options_exempt
def Joblist(request):
    try:
        db, cmd = pool.ConnectionPooling()
        q = "Select * From jobpost"
        cmd.execute(q)
        records = cmd.fetchall()
        db.close()
        return render(request, "joblist.html", {'result': records})
    except Exception as e:
        print(e)
        return render(request, "joblist.html", {'result': {}})

@xframe_options_exempt
def CompanySearch(request):

    return render(request,'companysearch.html')
    return HttpResponse('this is search')
