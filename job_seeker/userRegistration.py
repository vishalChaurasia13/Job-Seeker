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

def userLogin(request):
  return render(request, "userLoginPage.html", {'msg': ''})

def userEmailLogin(request):
  return render(request,"useremailLogin.html")

def CheckuserEmailPassword(request):
 try:
  db, cmd = pool.ConnectionPooling()
  email = request.POST['email']
  password = request.POST['password']

  q = "Select * from user where email='{0}' and password='{1}'".format(email, password)
  cmd.execute(q)
  data = cmd.fetchone()
  if (data):
    request.session['company']=data
    return render(request,"userProfile.html",{'msg':email,'data':data})
  else:
    return render(request, "userLoginPage.html", {'msg': 'Invalid EmailId/Password'})
 except Exception as e:
   print(e)
   return render(request, 'userLoginPage.html', {'msg': 'Server Error'})

def userLogout(request):
    del request.session['company']
    return redirect('/userlogin')