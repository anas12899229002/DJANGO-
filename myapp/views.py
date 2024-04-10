from django.shortcuts import render, redirect
from sched import UserFormInput
from sched import  TRAINPARIS
from random import randint

def index(request) :
    all = TRAINPARIS .objects.get
    needed = []

    for i in range(5):
        needed.append(all[i])

    lucky = randint(0,4)  

    return render(request , "index.html",{
        "line" : needed,
        "lucky" : all[lucky]
    })

def detail (request, name):
    train =  TRAINPARIS.objects.get(name = name)
    
    return render(request, "detail.html", {' TRAIN': train})

def userform (request):
    if request.method == 'POST':
        form = UserFormInput(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/vtart/')
    else:
        form = UserFormInput()
    return render(request, 'userform.html', {'form': form})


def map(request):
    return render(request,"map.html",{})
