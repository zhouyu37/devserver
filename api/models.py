# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BusinessUnit(models.Model):
    name = models.CharField("业务线",max_length=64,unique=True)
    class Meta:
        verbose_name_plural = "业务线表"
    def __str__(self):
        return self.name

class IDC(models.Model):
    name=models.CharField("机房",max_length=32)
    floor=models.IntegerField("楼层",default=1)
    class Meta:
        verbose_name_plural = "机房表"

    def __str__(self):
        return self.name

class Server(models.Model):
    device_status_choices = {
        (1,"上架"),
        (2,"在线"),
        (3,"离线"),
        (4,"下架"),
    }
    device_status_id = models.IntegerField(choices=device_status_choices,default=1)
    idc=models.ForeignKey("IDC",verbose_name="IDC机房",null=True,blank=True)
    # cabinet_num = models.CharField('机柜号', max_length=30, null=True, blank=True)
    # cabinet_order = models.CharField('机柜中序号', max_length=30, null=True, blank=True)
    business_unit = models.ForeignKey('BusinessUnit', verbose_name='属于的业务线', null=True, blank=True)
    ####basic+cpu+board
    hostname = models.CharField(max_length=128, unique=True)
    os_platform = models.CharField('系统', max_length=16, null=True, blank=True)
    os_version = models.CharField('系统版本', max_length=16, null=True, blank=True)

    sn = models.CharField('SN号', max_length=64, db_index=True)
    manufacturer = models.CharField(verbose_name='制造商', max_length=64, null=True, blank=True)
    model = models.CharField('型号', max_length=64, null=True, blank=True)

    cpu_count = models.IntegerField('CPU个数', null=True, blank=True)
    cpu_physical_count = models.IntegerField('CPU物理个数', null=True, blank=True)
    cpu_model = models.CharField('CPU型号', max_length=128, null=True, blank=True)

    latest_date = models.DateField(null=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name_plural = "服务器表"

    def __str__(self):
        return self.hostname

class Disk(models.Model):
    slot = models.CharField('插槽位', max_length=8)
    model = models.CharField('磁盘型号', max_length=128)
    # capacity = models.FloatField('磁盘容量GB')
    capacity = models.CharField('磁盘容量GB', max_length=8)
    pd_type = models.CharField('磁盘类型', max_length=32)
    server = models.ForeignKey(verbose_name='服务器',to='Server', related_name='disk_list')

    class Meta:
        verbose_name_plural = "硬盘表"

    def __str__(self):
        return self.slot

class NIC(models.Model):
    name = models.CharField('网卡名称', max_length=128)
    hwaddr = models.CharField('网卡mac地址', max_length=64)
    netmask = models.CharField(max_length=64)
    ipaddrs = models.CharField('ip地址', max_length=256)
    up = models.BooleanField(default=False)
    server = models.ForeignKey('Server', related_name='nic_list')

    class Meta:
        verbose_name_plural = "网卡表"

    def __str__(self):
        return self.name

class Memory(models.Model):
    slot = models.CharField('插槽位', max_length=32)
    manufacturer = models.CharField('制造商', max_length=32, null=True, blank=True)
    model = models.CharField('型号', max_length=64)
    capacity = models.FloatField('容量', null=True, blank=True)
    sn = models.CharField('内存SN号', max_length=64, null=True, blank=True)
    speed = models.CharField('速度', max_length=16, null=True, blank=True)
    server = models.ForeignKey('Server', related_name='memory_list')

    class Meta:
        verbose_name_plural = "内存表"

    def __str__(self):
        return self.slot

class AssetRecord(models.Model):
    server = models.ForeignKey('Server', related_name='servers')
    content = models.TextField(null=True)
    # creator = models.ForeignKey('UserProfile', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "资产记录表"


class ErrorLog(models.Model):
    """
    错误日志,如：agent采集数据错误 或 运行错误
    """
    server = models.ForeignKey('Server', null=True, blank=True)
    title = models.CharField(max_length=16)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "错误日志表"
    def __str__(self):
        return self.title



