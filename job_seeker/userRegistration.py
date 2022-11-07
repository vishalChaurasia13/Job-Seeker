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