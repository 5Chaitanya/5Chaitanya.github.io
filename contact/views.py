from django.shortcuts import render, redirect
from .models import feedback
import mysql.connector as sql
n=''
em=''
msg=''
# Create your views here.
def contact(request):
    global n,em,msg
    if request.method =='POST':
        m=sql.connect(host="localhost",user="root",password="12345",database="website")
        cursor = m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                n=value
            if key=="email":
                em=value
            if key=="message":
                msg=value
        c ="insert into feedback Values('{}','{}','{}')".format(n,em,msg)
        cursor.execute(c)
        m.commit()
        return redirect('thankyou')
    return render(request,'contact.html')

def thankyou(request):
    return render(request, 'thankyou.html')
