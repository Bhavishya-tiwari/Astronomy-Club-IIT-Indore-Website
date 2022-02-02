from audioop import lin2adpcm
from code import interact
from venv import EnvBuilder
from wsgiref.util import request_uri
from django.shortcuts import render
from os import pipe
from django import http
from django.db import reset_queries
from django.http import response
from django.shortcuts import render, HttpResponse, redirect

# from home.models import Contact
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Event, Blog, Profile
import json
import datetime

# Create your views here.
def home(request):
    return render(request, "astro/home.html")


def about(request):
    return render(request, "astro/about.html")


def addevent(request):
    if request.method == "POST":
        nm = request.POST.get("Namee")
        disc = request.POST.get("disc")
        urll = ""
        for i in range(1, 100):
            s = "url" + str(i)
            val = request.POST.get(s)
            if val == None:
                break
            elif val != "":
                l = str(val)
                urll += l + "$$"
        info = ""
        for i in range(1, 100):
            s = "info" + str(i)
            val = request.POST.get(s)
            if val == None:
                break
            elif val != "":
                l = str(val)
                info += l + "$$"
        hl = ""
        for i in range(1, 100):
            s = "high" + str(i)
            val = request.POST.get(s)
            if val == None:
                break
            elif val != "":
                l = str(val)
                hl += l + "$$"

        if nm != "" and disc != "":
            event = Event(
                Name=nm, Discription=disc, imgUrls=urll, Info=info, Highlights=hl
            )
            event.save()
        return redirect("addevent")

    else:
        return render(request, "astro/addevents.html")

def showevent(request):
    events = Event.objects.all().order_by('Event_id')
    ev=[]
    for e in events:
        urls = e.imgUrls
        urrr = urls.split('$$')
        

        # info = e.Info
        # inf = info.split('$$')

        # high = e.Highlights
        # hig = high.split('$$')
        
        

        oo = {
            "id":e.Event_id,
            "name":e.Name,
            "disc":e.Discription,
            "img":urrr[0],
            # "urls":urrr,
            # "inf":inf,
            # "hig":hig,
        }
        ev.append(oo)
    evs = {
        "evs":ev
    }


        

    return render(request, 'astro/event.html', evs)

def eventDetail(request, eid):
    event = Event.objects.filter(Event_id=eid).first()
    urls = event.imgUrls
    urrr = urls.split('$$')
    urrr.pop()
        

    info = event.Info
    inf = info.split('$$')
    inf.pop()


    high = event.Highlights
    hig = high.split('$$')
    hig.pop()





    return render(request, 'astro/event_detail.html',{"Name":event.Name, "Disc":event.Discription,"imgs":urrr, "infs":inf, "higs":hig})

def addblog(request):
    if request.method == "POST":
        T = request.POST.get("title")
        D = request.POST.get("disc")
        C = request.POST.get("content")
        hi = request.POST.get("headimage")
        blog = Blog(Title=T, headimg=hi, Discription=D,Content=C)
        if T !="" and D !="" and C !="" and hi !="":
            blog.save()

    return render(request, 'astro/AddBlog.html')

def blogs(request):

    blogs = Blog.objects.all().order_by('Blog_id')
    send =[]
    for b in blogs:
        oo ={
            "Title":b.Title,
            "id":b.Blog_id,
            "disc":b.Discription,
            "img":b.headimg
        }
        send.append(oo)

    

    return render(request, 'astro/blogs.html', {"bls":send})
def readblog(request, bid):
    b = Blog.objects.filter(Blog_id=bid).first()
    oo ={
            "Title":b.Title,
            "id":b.Blog_id,
            "disc":b.Discription,
            "img":b.headimg,
            "cnt":b.Content,
        }

    return render(request,'astro/Blog_detail.html',oo)


def addmember(request):
    if request.method == "POST":
        nm = request.POST.get("Name")
        abt = request.POST.get("abt")
        branchyear = request.POST.get("branchyear")
        mno = request.POST.get("mno")
        email = request.POST.get("email")
        por = request.POST.get("POR")
        img = request.POST.get("img")
        old = request.POST.get("old")
        new = request.POST.get("new")
        ghub = request.POST.get("ghub")
        lin = request.POST.get("lin")
        insta = request.POST.get("insta")
        fb = request.POST.get("fb")
        act = ""
        for i in range(1, 100):
            s = "url" + str(i)
            s1 = "urll" + str(i)
            head = request.POST.get(s)
            dc = request.POST.get(s1)
            if head == None or dc == None:
                break
            elif head != None and dc != None:
                l = str(head)
                j = str(dc)
                act += l + "##"+ j +"$$"

        
        intrests = ""
        for i in range(1, 100):
            s = "info" + str(i)
            val = request.POST.get(s)
            if val == None:
                break
            elif val != "":
                l = str(val)
                intrests += l + "$$"

        print(nm,abt,branchyear,mno,email,por,img,old,new,act,intrests)
        b=branchyear + "$$" + mno + "$$"+ email + "$$"+ por
        lll= str(ghub) + "$$" + str(lin) + "$$"+ str(insta) + "$$"+ str(fb)
        
        ol=""
        if old==1:
            ol="old" 
        elif new==1:
            ol="new"



        profile = Profile(Name=nm,branch_year_mobilenumber_email_por=b,About=abt,Intrests=intrests,Activities=act,img=img,git_lin_insta_fb=lll,old=ol  )
        if nm !="" and b !="" and abt !="" and intrests !="" and act !="" and img !="" and lll !="":
            profile.save()
    return render(request,'astro/addMember.html')

def team(request):
    members = Profile.objects.all().order_by('memb_id')
    send =[]
    
    for b in members:
        data = b.branch_year_mobilenumber_email_por
        dat = data.split('$$')
        
        oo ={
            "Name":b.Name,
            "id":b.memb_id,
            "img":b.img,
            "branch_year":dat[0],
            "mno":dat[1],
            "email":dat[2],
            "por":dat[3],
            "abt":b.About,

        }
        send.append(oo)

    
    return render(request,"astro/team.html",{"membrs":send}) 

def profile(request,mid):
    b = Profile.objects.filter(memb_id=mid).first()
    data = b.branch_year_mobilenumber_email_por
    dat = data.split('$$')

    ints = b.Intrests
    int = ints.split('$$')
    int.pop()

    actvs = b.Activities,
    acts = actvs[0].split('$$')
    acs = acts.pop()

    handles = b.git_lin_insta_fb,
    hands = handles[0].split('$$')
    print(hands)

    activities =[]
    for ac in acts:
        d = ac.split('##')
        o = {
            "Heading":d[0],
            "Disc":d[1],
        }

        activities.append(o)
    
        
    main ={
            "Name":b.Name,
            "id":b.memb_id,
            "img":b.img,
            "branch_year":dat[0],
            "mno":dat[1],
            "email":dat[2],
            "por":dat[3],
            "abt":b.About,
            "ints":int,
            "git":hands[0],
            "linkdIn":hands[1],
            "insta":hands[2],
            "fb":hands[3],

            
        }

        # old new wala dekh lena






    return render(request, 'astro/member_profile.html',{"p":main, "aa":activities})



        
        
      



