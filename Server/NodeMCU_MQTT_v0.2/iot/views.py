from django.shortcuts import render
from . import sub
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SecFile

# Create your views here.
@csrf_exempt
def upload(request):
    if request.method == "POST":
        file_name = request.POST['file_name']
        sec_file = request.FILES['sec_file']
        
        model = SecFile(file_name=file_name, sec_file=sec_file)
        model.save()
        print('upload file', file_name, sec_file)
        
        msg = {'result' : 'success'}
    else: msg = {'result' : 'fail'}
    
    return JsonResponse(msg)