from django.shortcuts import render,redirect,HttpResponse
from . import pool

from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def userRegistrationInterface(request):
    return render(request,"userRegistration.html",{'msg':''})

@xframe_options_exempt
def userRegistrationSubmit(request):
   try:
     db,cmd=pool.ConnectionPooling()
     uname=request.POST['uname']
     contact=request.POST['contact']
     email=request.POST['email']
     address=request.POST['address']
     password=request.POST['password']

     q="insert into user(uname,contact,email,address,password) values('{0}','{1}','{2}','{3}','{4}')".format(uname,contact,email,address,password)

     print(q)
     cmd.execute(q)
     db.commit()
     db.close()
     return render(request, "userRegistration.html", {'msg': 'Registered'})
   except Exception as e:
     print(e)
     return render(request, "userRegistration.html", {'msg': 'Fail to Submit Record'})

@xframe_options_exempt
def userLogin(request):
  return render(request, "userLoginPage.html", {'msg': ''})

@xframe_options_exempt
def userEmailLogin(request):
  return render(request,"useremailLogin.html")

@xframe_options_exempt
def CheckuserEmailPassword(request):
 try:
  db, cmd = pool.ConnectionPooling()
  email = request.POST['email']
  password = request.POST['password']

  q = "Select * from user where email='{0}' and password='{1}'".format(email, password)
  cmd.execute(q)
  data = cmd.fetchone()
  if (data):
    request.session['user']=data
    return render(request,"userProfile.html",{'msg':email,'data':data})
  else:
    return render(request, "userLoginPage.html", {'msg': 'Invalid EmailId/Password'})
 except Exception as e:
   print(e)
   return render(request, 'userLoginPage.html', {'msg': 'Server Error'})

@xframe_options_exempt
def userLogout(request):
    del request.session['user']
    return redirect('/userlogin')

@xframe_options_exempt
def userWithoutLogin(request):

    return render(request, "userWithoutLogin.html", {})

@xframe_options_exempt
def UserSearch(request):
    try:
        db, cmd = pool.ConnectionPooling()

        if (request.GET['query']):
              query = request.GET['query']
              q = "Select * From jobpost where cname LIKE '%{0}%' OR jobtitle LIKE '%{0}%' OR jobcategory LIKE '%{0}%' OR location LIKE '%{0}%' OR skills LIKE '%{0}%' OR jobduration LIKE '%{0}%' OR jobtype LIKE '%{0}%' OR qualification LIKE '%{0}%' ".format(query)
              cmd.execute(q)
              if(q):
                  records = cmd.fetchall()
                  return render(request,'usersearch.html', {'result': records})
                  db.close()
              else:
                  return HttpResponse('Not found ...')
        else:
            return HttpResponse('Not found ...')
    except Exception as e:
        print(e)
        return HttpResponse('Not found ...')

@xframe_options_exempt
def UserProfile(request):
    db, cmd = pool.ConnectionPooling()

    u_id =request.GET['u_id']
    q = "Select * from user where u_id='{0}'".format(u_id)
    cmd.execute(q)
    data = cmd.fetchone()
    if (data):
        request.session['user'] = data
        return render(request,'profile.html',{'data':data})
    else:
        return HttpResponse('something went wrong...')

def UpdatedProfile(request):
    try:
        db, cmd = pool.ConnectionPooling()
        class10 = request.POST['class10']
        class12 = request.POST['class12']
        graduation = request.POST['graduation']
        skills = request.POST['skills']
        language = request.POST['language']
        experience = request.POST['experience']
        additional = request.POST['additional']
        u_id = request.POST['u_id']

        q = "insert into userprofile(class10,class12,graduation,skills,language,experience,additional,u_id) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(class10, class12, graduation, skills, language, experience, additional,u_id)

        print(q)
        cmd.execute(q)
        db.commit()
        db.close()
        return HttpResponse('Profile Updated')
    except Exception as e:
        print(e)
        return render(request, "resume.html", {'msg': 'Something went wrong'})

@xframe_options_exempt
def Resume(request):
    db, cmd = pool.ConnectionPooling()
    u_id = request.GET['u_id']
    q = "Select a.u_id,a.uname,a.contact,a.address,a.email,b.class10,b.class12,b.graduation,b.experience,b.additional,b.language,b.skills from user a,userprofile b where a.u_id=b.u_id and b.u_id='{0}'".format(u_id)
    cmd.execute(q)
    data = cmd.fetchone()
    if (data):
        request.session['user'] = data
        return render(request,"resume.html",{'data':data})
    else:
        return HttpResponse('something went wrong...')


@xframe_options_exempt
def ApplyJob(request):
    try:
        db, cmd = pool.ConnectionPooling()
        u_id=request.GET['u_id']
        q = "Select * From jobpost"
        cmd.execute(q)
        records = cmd.fetchall()
        db.close()
        return render(request, "applyjob.html", {'result': records,'u_id':u_id})
    except Exception as e:
        print(e)
        return render(request, "applyjob.html", {'result': {}})

@xframe_options_exempt
def AppliedJob(request):
   try:
     db,cmd=pool.ConnectionPooling()
     u_id=request.POST['u_id']
     job_id=request.POST['job_id']
     companyid = request.POST['companyid']

     q="insert into appliedjob(u_id,job_id,companyid) values('{0}','{1}','{2}')".format(u_id,job_id,companyid)
     print(q)
     cmd.execute(q)
     db.commit()
     db.close()
     return HttpResponse('Applied')
   except Exception as e:
     print(e)
     return render(request, "applyjob.html", {'msg': 'Something went wrong'})


