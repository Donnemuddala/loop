from this import d
from django.shortcuts import render

# Create your views here. 
def loop(request):
    d={'names':'sunil'}
    return render(request,'loop.html',context=d)