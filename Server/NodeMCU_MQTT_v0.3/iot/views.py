from django.shortcuts import render
from . import sub
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SecFile
# View 관련
from django.views import generic

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

def detect_intrusion(request):
    print("intrusion Detection . . .")
    print("send Notification by kakaotalk")
    
    msg = {"result" : "success"}
    return JsonResponse(msg)

class SecFileListView(generic.ListView):
    model = SecFile
    template_name = 'iot/sec_file_list.html'
    context_object_name = 'sec_files' #context 변수
    
class SecFileDetailView(generic.DetailView):
    model = SecFile
    template_name = 'iot/sec_file_detail.html'
    context_object_name = 'vfile'
    
class CamView(generic.TemplateView):
    template_name = "cam.html"
    
    def get_context_data(self):
        context = super().get_context_data()
        context['model'] = self.request.GET.get('mode', '#')
        return context