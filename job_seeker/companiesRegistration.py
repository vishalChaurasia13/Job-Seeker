from django.shortcuts import render
from . import pool


# corporate....................................

def companiesRegistrationInterface(request):
    return render(request,"companiesRegistration.html",{'msg':''})

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
    return render(request,"companyProfile.html",{'msg':email,'data':'data'})
  else:
    return render(request, "companyLoginPage.html", {'msg': 'Invalid EmailId/Password'})
 except Exception as e:
   print(e)
   return render(request, 'companyLoginPage.html', {'msg': 'Server Error'})
