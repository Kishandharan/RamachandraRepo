from django.shortcuts import render
import random
# Create your views here.

def home(request):
    weeks = ['', 'Mon', '', 'Wed', '', 'Fri', '', '']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    days =[]
    for i in range(0,365,1):
        rand=  random.randint(0,4)
        if rand ==1:
            days.append("rgb(209, 255, 200)")
        elif rand ==2:
            days.append("rgb(176, 255, 161)")
        elif rand>2:
            days.append("hsl(110, 100%, 70%)")
        else:
            days.append("rgb(220, 220, 220)")
    return render(request,'index.html',{"param1":weeks,"param2":months,"param3":days})