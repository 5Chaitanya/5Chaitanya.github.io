from django.shortcuts import render, redirect
import mysql.connector as sql
em=''
pwd=''

# Create your views here.
def gloginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="12345",database="website")
        cursor = m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c ="select *from guide where email='{}'and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())   
        if t==():
            return render(request,'error.html')     
        else:
            return render(request,'welcomeg.html')
    return render(request,"login_g.html")

