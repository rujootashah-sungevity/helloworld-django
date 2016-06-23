from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {"my_name": "Adrian",'bool_value': False, 'album_name':'hihihi'}
    return render(request,'music/index.html',context)

