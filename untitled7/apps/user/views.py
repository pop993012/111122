from django.shortcuts import render
from rest_framework import status
# Create your views here.
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# from dysms_python.demo_sms_send import  send_sms
from  apps.user.models import  User
import json
#from  front.checkaa   import *
from rest_framework import viewsets
#from .sers import SmsSerializer
#from rest_framework.views import Response
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            print(111111)
            if user.check_password(password):
                print(22222)
                return user
        except Exception as e:
            return None


# def  zhale(request):
#
#         r = string.digits
#         r=''.join(random.sample(r,4))
#         saveCode(fm.data.get('telephone'),r)
#         print(r)
#         print(fm.data.get('telephone'))
#         r = send_sms(phone_numbers=fm.data.get('telephone'),smscode=r)
#         print(1111111111)
#         print(r)
        # if json.loads(r.decode("utf-8"))['Code'] == 'OK':
        #     return HttpResponse('发送成功')
        # else:  # 发送失败
        #     return HttpResponse('请检查网络')
#class  SendCodeView(viewsets.ModelViewSet):
    # serializer_class = SmsSerializer
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

