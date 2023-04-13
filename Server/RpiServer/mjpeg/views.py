from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from .cam import MJpegStreamCam

mjpegstream = MJpegStreamCam()

# Create your views here.
class CamView(TemplateView):
    template_name = "cam.html"
    
    def get_context_data(self):
        context = super().get_context_data()
        context['model'] = self.request.GET.get('mode', '#')
        return context
    
def snapshot(request):
    image = mjpegstream.snapshot()
    return HttpResponse(image, content_type = 'image/jpeg')

def stream(request):
    return StreamingHttpResponse(mjpegstream, content_type='multipart/x-mixed-replace;boundary=--myboundary')