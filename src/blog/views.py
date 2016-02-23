from django.shortcuts import render, render_to_response,HttpResponseRedirect
import models
# Create your views here.


def list(request):
    obj = models.wenzhang.objects.all()
    
    return render_to_response('list.html',{'obj1':obj})
    
def add(request):
     
    return render_to_response('add.html')

def display(request):
     
    return render_to_response('display.html')
