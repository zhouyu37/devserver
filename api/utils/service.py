#!/usr/bin/python
# -*- coding:utf-8 -*-
from api import models

def process_basic(asset_info,hostname):
    basic_dict={}
    basic_dict.update(asset_info['basic']['data'])
    basic_dict.update(asset_info['cpu']['data'])
    basic_dict.update(asset_info['board']['data'])
    models.Server.objects.filter(hostname=hostname).update(**basic_dict)

def process_disk(asset_info,server):
    disk_queryset = models.Disk.objects.filter(server=server)
    disk_info=asset_info['disk']['data']

    disk_queryset_set = {row.slot for row in disk_queryset}
    disk_info_set = set(disk_info)

    update_disk_slot_list = disk_queryset_set & disk_info_set
    add_disk_slot_list = disk_info_set - disk_queryset_set
    del_disk_slot_list = disk_queryset_set - disk_info_set
#####update disk
    for slot in update_disk_slot_list:
        # models.Disk.objects.filter(slot=slot, server=server).update(**disk_info[slot])
        obj=models.Disk.objects.filter(slot=slot,server=server).first()
        row_dict = disk_info[slot]
        record_list=[]
        for name,new_value in row_dict.items():
            old_value = str(getattr(obj,name))
            if old_value != new_value:
                setattr(obj,name,new_value)
                verbose_name = models.Disk._meta.get_field(name).verbose_name
                msg="[disk change] slot %s:%s from %s to %s"%(slot,verbose_name,old_value,new_value)
                record_list.append(msg)
        obj.save()
        if record_list:
            models.AssetRecord.objects.create(server=server,content=';'.join(record_list))
####del disk
    models.Disk.objects.filter(server=server, slot__in=del_disk_slot_list).delete()
    if del_disk_slot_list:
        msg = "[disk change]remove slot %s disk" %(';'.join(del_disk_slot_list))
        models.AssetRecord.objects.create(server=server, content=msg)

##########add disk
    for slot in add_disk_slot_list:
            row_dict = disk_info[slot]
            row_record_list = []
            for name,new_value in row_dict.items():
                verbose_name = models.Disk._meta.get_field(name).verbose_name
                tpl = "%s:%s" %(verbose_name,new_value,)
                row_record_list.append(tpl)

            msg = "[disk change]slot %s add disk ,disk info:%s" %(slot, ';'.join(row_record_list),)
            models.AssetRecord.objects.create(server=server, content=msg)
            row_dict['server'] = server
            models.Disk.objects.create(**row_dict)

def process_nic(asset_info,server):

    nic_queryset = models.NIC.objects.filter(server=server)
    nic_info = asset_info['net']['data']

    nic_queryset_set = {row.name for row in nic_queryset}
    nic_info_set = set(nic_info)

    update_nic_slot_list = nic_info_set & nic_queryset_set
    add_nic_slot_list = nic_info_set - nic_queryset_set
    del_nic_slot_list = nic_queryset_set - nic_info_set

    # update
    for slot in update_nic_slot_list:
        obj = models.NIC.objects.filter(name=slot, server=server).first()
        row_dict = nic_info[slot]
        record_list = []
        for name, new_value in row_dict.items():
            old_value = str(getattr(obj, name))
            if old_value != new_value:
                setattr(obj, name, new_value)
                verbose_name = models.NIC._meta.get_field(name).verbose_name
                msg = "[nic change] slot %s:%s from %s to %s" % (slot, verbose_name, old_value, new_value)
                record_list.append(msg)
        obj.save()
        if record_list:
            models.AssetRecord.objects.create(server=server, content=';'.join(record_list))

    # 删除
    models.NIC.objects.filter(server=server, name__in=del_nic_slot_list).delete()
    if del_nic_slot_list:
        msg = "[nic change]remove slot %s nic" %(';'.join(del_nic_slot_list))
        models.AssetRecord.objects.create(server=server, content=msg)

        ##########add disk
    for slot in add_nic_slot_list:
        row_dict = nic_info[slot]
        row_record_list = []
        for name, new_value in row_dict.items():
            verbose_name = models.NIC._meta.get_field(name).verbose_name
            tpl = "%s:%s" % (verbose_name, new_value,)
            row_record_list.append(tpl)

        msg = "[nic change]slot %s add nic ,nic info:%s" % (slot, ';'.join(row_record_list),)
        models.AssetRecord.objects.create(server=server, content=msg)
        row_dict['server'] = server
        row_dict['name'] = slot
        models.NIC.objects.create(**row_dict)

def process_memory(asset_info,server):
    memory_queryset = models.Memory.objects.filter(server=server)
    memory_info = asset_info['mem']['data']

    memory_queryset_set = {row.slot for row in memory_queryset}
    memory_info_set = set(memory_info)

    update_memory_slot_list = memory_info_set & memory_queryset_set
    add_memory_slot_list = memory_info_set - memory_queryset_set
    del_memory_slot_list = memory_queryset_set - memory_info_set

    # 更新
    for slot in update_memory_slot_list:
        obj = models.Memory.objects.filter(slot=slot, server=server).first()
        row_dict = memory_info[slot]
        record_list = []
        for name, new_value in row_dict.items():
            old_value = str(getattr(obj, name))
            if old_value != new_value:
                setattr(obj, name, new_value)
                verbose_name = models.Memory._meta.get_field(name).verbose_name
                msg = "[mem change] slot %s:%s from %s to %s" % (slot, verbose_name, old_value, new_value)
                record_list.append(msg)
        obj.save()
        if record_list:
            models.AssetRecord.objects.create(server=server, content=';'.join(record_list))
    # 删除
    models.Memory.objects.filter(server=server, slot__in=del_memory_slot_list).delete()
    if del_memory_slot_list:
        msg = "[mem change]remove slot %s nic" %(';'.join(del_nic_slot_list))
        models.AssetRecord.objects.create(server=server, content=msg)

    # 添加
    for slot in add_memory_slot_list:
        row_dict = memory_info[slot]
        row_record_list = []
        for name, new_value in row_dict.items():
            verbose_name = models.Memory._meta.get_field(name).verbose_name
            tpl = "%s:%s" % (verbose_name, new_value,)
            row_record_list.append(tpl)

        msg = "[mem change]slot %s add nic ,nic info:%s" % (slot, ';'.join(row_record_list),)
        models.AssetRecord.objects.create(server=server, content=msg)
        row_dict['server'] = server
        models.Memory.objects.create(**row_dict)


