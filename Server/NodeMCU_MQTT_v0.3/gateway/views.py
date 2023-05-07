from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# View 관련
from django.views import generic
# openCV
import cv2
#Haar
from .haarDetect import HarrDetect
#OS
import subprocess
import os
#Upload
from ..Rpi_videoUpload import fileUpload

# Create your views here.
@csrf_exempt
def upload(request):
    if request.method == "POST":
        file_name = request.POST['file_name']
        sec_file = request.FILES['sec_file']
        model = SecFile(file_name=file_name, sec_file=sec_file)
        model.save()
        
        cvt_file_name = convert(file_name)
        cvt_path = f"C:/Users/duswn/Desktop/git_repo/Gateway/Server/NodeMCU_MQTT_v0.3/{cvt_file_name}"
        cvt_url = "http://172.20.10.5:8000/cvt_upload/"
        upload(cvt_path, cvt_url)
        print(f"{cvt_file_name} // Cvt Fin----!")

def convert(file_name):
    # get Img
    y  = file_name.split("_")[0]
    imgSrc = f"./media/sec_file/{y[0:4]}/{y[4:6]}/{y[6:8]}/{file_name}"
    imgFile = cv2.imread(imgSrc)
    harrXml = "haarcascade_frontalface_alt.xml"
    
    # get Detect
    harr = HarrDetect(harrXml)
    faceLst = harr.detect(imgFile)

    getDetect = harr.draw_rect(imgFile, faceLst)
    cv2.imwrite(f"cvt_{file_name}", getDetect)
    
    return f"cvt_{file_name}"

def cvt_upload(request):
    if request.method == "POST":
        file_name = request.POST['file_name']
        sec_file = request.FILES['sec_file']
        model = DetectFile(file_name=file_name, sec_file=sec_file)
        model.save()

class SecFileListView(generic.ListView):
    model = SecFile
    template_name = 'gateway/sec_file_list.html'
    context_object_name = 'sec_files' #context 변수
    
class SecFileDetailView(generic.DetailView):
    model = SecFile
    template_name = 'gateway/sec_file_detail.html'
    context_object_name = 'vfile'