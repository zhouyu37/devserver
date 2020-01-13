# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from django.views import View

# Create your views here.
import json
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from rest_framework.response import Response
from app01.models import Course,CourseDetail,UserInfo,UserToken
from utils.serializer import CourseSerializer,CourseDetailSerializer
from utils.auth import LoginAuth

class CourseView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [LoginAuth]
    def list(self, request, *args, **kwargs):
        response = {"code": 1000, "data": None, "msg": ""}
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page=self.paginate_queryset(queryset)
            if page is not None:
                serializer=self.get_serializer(page,many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            response['data']=serializer.data
        except Exception as e:
            response['code'] = 1001
            response['msg'] = str(e)
        return Response(response)

class CourseDetailView(ModelViewSet):
    queryset = CourseDetail.objects.all()
    serializer_class =CourseDetailSerializer

class LoginView(APIView):
    def get_random_str(self,user):
        import hashlib, time
        ctime = str(time.time())
        md5 = hashlib.md5(bytes(user, encoding="utf8"))
        md5.update(bytes(ctime, encoding="utf8"))
        return md5.hexdigest()
    def post(self,request):
        user=request.data.get("user")
        pwd=request.data.get("pwd")
        response = {"user": None, "msg": ""}
        try:
            user=UserInfo.objects.filter(username=user,password=pwd).first()
            if user:
                random_str=self.get_random_str(user.username)
                UserToken.objects.update_or_create(user=user.username,{"token":random_str})
                response["user"] = user.username
                response["token"] = random_str
            else:
                response["msg"] = "userorpassword is wrong!"
        except Exception as e:
            response["msg"]=str(e)

class test(View):
    def get(self,request):
        courses=Course.objects.all()
        ret=[]
        for obj in courses:
            ret.append(
                {
                    "title":obj.title,
                    "price":obj.price,
                    "img":obj.img,
                }
            )
        return HttpResponse(json.dumps(ret))


