#!/usr/bin/python
# -*- coding:utf-8 -*-

from rest_framework import serializers
from app01.models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDetail
        fields="__all__"
    course=serializers.SerializerMethodField()
    def get_course(self,obj):
        return [obj.course.pk,obj.course.title]


