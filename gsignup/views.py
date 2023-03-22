from django.shortcuts import render,redirect
from .models import guide
import mysql.connector as sql
fn=''
ln=''
pn=''
ad=''
em=''
pwd=''
# Create your views here.
def gsignaction(request):
    global fn,ln,pn,ad,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="12345",database="website")
        cursor = m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="fname":
                fn=value
            if key=="lname":
                ln=value
            if key=="phone":
                pn=value
            if key=="aadhar":
                ad=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c ="insert into guide Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,pn,ad,em,pwd)
        cursor.execute(c)
        m.commit()
        return redirect('http://localhost:8000/glogin/')
    return render(request,"signup_g.html")


