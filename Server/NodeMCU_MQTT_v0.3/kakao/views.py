from django.shortcuts import render
from django.views.generic import TemplateView, FormView
# from kakao.forms import KaKaoTalkForm
import json
import requests
from django.contrib import messages

# Create your views here.
client_id = '6acc3abf203ac6b3b5901880bd14d69e'

class KakaoLoginView(TemplateView):
    template_name = 'kakao_login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["client_id"] = client_id
        
        return context
    
class KakaoAuthView(TemplateView):
    template_name = 'kakao_token.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        code = self.request.GET['code']
        token = self.getAccessToken(code)
        
        context['client_id'] = client_id
        context['token'] = token
        self.save_access_token(token["access_token"])
        
        return context
    
    # 세션 코드값 code 를 이용해서 ACESS TOKEN과 REFRESH TOKEN을 발급 받음
    def getAccessToken(self, code):
        url = "https://kauth.kakao.com/oauth/token"
        data = {
            'grant_type': 'authorization_code',
            'client_id': client_id,
            'redirect_url': 'http://172.20.10.5:8000/kakao/oauth',
            'code': code
        }
        headers = {
            'Cache-Control': "no-cache",
        }
        response = requests.post(url, data=data, headers=headers) 
        
        return response.json()
    
    def save_access_token(self, access_token):
        with open("access_token.txt", "w") as f:
            f.write(access_token)
