# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from api import models
from utils.service import process_basic,process_disk,process_memory,process_nic

def server_info(request):
    if request.method == "GET":
        hostlist=['c1.com', 'c2.com', 'c3.com']
        return HttpResponse(json.dumps(hostlist))
    elif request.method == "POST":
        data=json.loads(request.body)
        print(data)
        return HttpResponse("post ok")


#@method_decorator(csrf_exempt,name='dispatch')
# class server(View):
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(server,self).dispatch(request,*args,**kwargs)
    #
    # def get(self,request,*args,**kwargs):
    #     hostlist = ['c1.com', 'c2.com', 'c3.com']
    #     return HttpResponse(json.dumps(hostlist))
    #
    # def post(self,request,*args,**kwargs):
    #     data = json.loads(request.body)
    #     print("test4", data["data"].get("disk"))
    #     return HttpResponse("post ok")
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.security import decrypt
from django.conf import settings
import hashlib
def gen_sign(ctime):
    val = '%s|%s' %(settings.URL_AUTH_KEY,ctime)
    obj = hashlib.md5()
    obj.update(val.encode('utf-8'))
    return obj.hexdigest()

SIGN_RECORD = {}
class APIAuthView(APIView):
    def dispatch(self, request, *args, **kwargs):
        client_sign = request.GET.get('sign')  # 客户端签名
        print("test11",client_sign)
        client_ctime = int(request.GET.get('ctime'))  # 客户端时间
        print("test22", client_sign)
        server_time = int(time.time() * 1000)  # 服务端时间

        if server_time - client_ctime > 0:
            request.session["status"]=1
        if client_sign in SIGN_RECORD:
            request.session["status"] = 1

        server_sign = gen_sign(client_ctime)
        if server_sign != client_sign:
            request.session["status"] = 3

        SIGN_RECORD[client_sign] = client_ctime
        return super(APIAuthView,self).dispatch(request, *args, **kwargs)

class server(APIAuthView):
    def get(self,request,*args,**kwargs):
        hostlist = ['c1.com', 'c2.com', 'c3.com']
        return Response(hostlist)
    def post(self,request,*args,**kwargs):
        if request.session["status"]:
            return Response({'status': False, 'data': request.session["status"], 'error': None})
        body = decrypt(request._request.body)
        asset_info = json.loads(body.decode('utf-8'))
        # print("hello111",asset_info)
        # print("test33",asset_info["net"])
        result = {'status': True, 'data': None, 'error': None}
        asset_type = asset_info.get('type')
        if asset_type == "create":
            server_dict = {}
            server_dict.update(asset_info['basic']['data'])
            server_dict.update(asset_info['cpu']['data'])
            server_dict.update(asset_info['board']['data'])
            server = models.Server.objects.create(**server_dict)
            disk_info = asset_info['disk']['data']
            for k, v in disk_info.items():
                v['server']=server
                print("test",v)
                models.Disk.objects.create(**v)
            net_info = asset_info['net']['data']
            for k,v in net_info.items():
                v['server']=server
                v['name']=k
                models.NIC.objects.create(**v)
            mem_info=asset_info['mem']['data']
            for k, v in mem_info.items():

                v['server'] = server
                models.Memory.objects.create(**v)

        elif asset_type == 'update':
            hostname=asset_info['basic']['data']['hostname']
            server=models.Server.objects.filter(hostname=hostname).first()
            process_basic(asset_info, hostname)
            process_disk(asset_info, server)
            process_nic(asset_info,server)
            process_memory(asset_info,server)
        elif asset_type == 'host_update':
            hostname=asset_info['cert']
            server=models.Server.objects.filter(hostname=hostname).first()
            process_basic(asset_info, hostname)
            process_disk(asset_info, server)
            process_nic(asset_info, server)
            process_memory(asset_info, server)
        result['data']=asset_info['basic']['data']['hostname']
        return Response(result)

