from django.shortcuts import render
import random
import datetime as dt
import os 
def random1(request):    # Random calender
    weeks = ['', 'Mon', '', 'Wed', '', 'Fri', '']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    year = dt.datetime.now().year
    days =  make_calender(year-1) 
    list1 =[]
    for i in range(0,371,1):
        rand=  random.randint(0,4)
        if rand ==1:
            list1.append([days[i][0],"rgb(209, 255, 200)",days[i][1]])
        elif rand ==2:
            list1.append([days[i][0],"rgb(176, 255, 161)",days[i][1]])
        elif rand>2:
            list1.append([days[i][0],"hsl(110, 100%, 70%)",days[i][1]])
        else:
            list1.append([days[i][0],"rgb(220, 220, 220)",days[i][1]])
    return render(request,'index.html',{"param1":weeks,"param2":months,"param3":list1})


def home(request):
    weeks = ['', 'Mon', '', 'Wed', '', 'Fri', '']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    list1 = git_calender_prep()
    return render(request,'index.html',{"param1":weeks,"param2":months,"param3":list1})


def make_calender(year):
    from datetime import date, timedelta
    start_date = date(year, 12, 11)
    day = []
    combine =[]
    months =['Jan','Feb','Mar','Apr','May',"Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']
    for i in range(371):
        day.append(start_date+timedelta(i))
    for d in day:
        combine.append([str(d.day)+"-"+months[d.month-1]+"-"+str(d.year),weeks[d.weekday()]])
    return combine

def git_calender_prep():
    content = make_calender(year = dt.datetime.now().year-1)
    list1 =[]
    list2 =[]
    dates =[]
    commit=[]
    final_list=[]
    file = os.path.join('templates',"GitHubActivity_4MW21AD043.txt")
    with open(file,'r')as f:
        list1=f.read().split('\n')
    for l in list1:
        list2 = l.replace("\n","").split(",")
        dates.append(list2[0])
        commit.append(list2[1])
    for c1 in content:
        e= c1[0]
        if e in dates:
            if int(commit[dates.index(e)]) ==1:
                final_list.append([c1[0],"rgb(209, 255, 200)",c1[1]])
            elif int(commit[dates.index(e)]) ==2:
                final_list.append([c1[0],"rgb(176, 255, 161)",c1[1]])
            elif int(commit[dates.index(e)]) >2:
                final_list.append([c1[0],"hsl(110, 100%, 70%)",c1[1]])
            else:
                final_list.append([c1[0],"rgb(220, 220, 220)",c1[1]])
        else :
            final_list.append([c1[0],"rgb(220, 220, 220)",c1[1]])
    return final_list