from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import pickle, os, sklearn
from static.classificatorapp.AI import singlextract, formatingData

def home(request):
    return render(request,'home.html')

def extract_validate(request):
    filename= "static\\classificatorapp\\AI\\Predictor_Model"
    Url = formatingData.execute(request.POST['Input'])
    loaded = pickle.load(open(filename,'rb'))
    extracted = singlextract.execute(Url)
    result = loaded.predict([extracted])
    if result[0] == 0:
        return render(request,'benign.html',{'Url':request.POST['Input']})
    else:
        return render(request,'malicious.html',{'Url':request.POST['Input']})

def redirect(request):
    if request.POST['InputURL'] == "home":
        return render(request,'home.html')
    else:
        return HttpResponseRedirect(request.POST['InputURL'])

def github(request):
    return HttpResponseRedirect("https://github.com/Diego-Luiz")

def githubproject(request):
    return HttpResponseRedirect("https://github.com/Diego-Luiz/URLYZER")

def linkedin(request):
    return HttpResponseRedirect("https://www.linkedin.com/in/diego-luiz-n-gon%C3%A7alves-5a1584191/")
