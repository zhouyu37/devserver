# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class UserInfo(models.Model):
    username=models.CharField(max_length=32,verbose_name="username")
    password=models.CharField(max_length=128,verbose_name="password")
    type_choices=[(1,"normal user"),(2,"VIP"),(3,"SVIP")]
    user_type=models.IntegerField(choices=type_choices,default=1)

    def __str__(self):
        return self.username

class UserToken(models.Model):
    user=models.OneToOneField("UserInfo")
    token=models.CharField(max_length=64)
    create_time=models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    title = models.CharField(max_length=32,unique=True,verbose_name="course_category")
    def __init__(self):
        return self.title
    class Meta:
        verbose_name="01_course_category"
        db_table=verbose_name
        verbose_name_plural =verbose_name

class Course(models.Model):
    title=models.CharField(max_length=128,unique=True,verbose_name="course_name")
    course_img=models.ImageField(upload_to="course/%Y-%m",verbose_name="course_img",null=True,blank=True)
    category=models.ForeignKey("Category",verbose_name="course_category",null=True,blank=True)
    course_type_choices=((0,"fufei"),(1,"vip"),(2,"xuewei"))
    course_type=models.SmallIntegerField(choices=course_type_choices,default=0)
    degree_course=models.ForeignKey(to="DegreeCourse",blank=True,null=True,help_text="degree course must be related to degreecourse")

    brief=models.CharField(max_length=1024,verbose_name="course_brief",null=True)
    level_choices=((0,"junior"),(1,"intermediate"),(2,"senior"))
    level=models.SmallIntegerField(choices=level_choices,default=1)
    status_choices=((0,"online"),(1,"offline"),(2,"test"))
    status=models.SmallIntegerField(choices=status_choices,default=0)
    pub_date=models.DateField(verbose_name="pub_data",blank=True,null=True)
    order=models.IntegerField(default=0,verbose_name="course_order",help_text="shun xu")
    study_num=models.IntegerField(default=1,verbose_name="learner_num",help_text="buyers")

    price_policy=GenericRelation("PricePolicy")
    often_ask_questions=GenericRelation("OftenAskedQuestion")
    course_comments=GenericRelation("Comment")

    def save(self,*args,**kwargs):
        if self.course_type == 2:
            if not self.degree_course:
                raise ValueError("degree must be related to course")
        super(Course,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="02_course_table"
        db_table=verbose_name
        verbose_name_plural=verbose_name


class CourseDetail(models.Model):
    course=models.OneToOneField(to="Course")
    hours=models.IntegerField(verbose_name="course_time",default=7)
    video_brief_link=models.CharField(max_length=256,blank=True,null=True)
    summary=models.TextField(max_length=2048,verbose_name="verbose_summary")
    why_study = models.TextField(verbose_name="why study")
    what_to_study_brief = models.TextField(verbose_name="what to study")
    career_improvement = models.TextField(verbose_name="be helped to ")
    recommend_courses = models.ManyToManyField("Course", related_name="recommend_by", blank=True)
    teachers = models.ManyToManyField("Teacher", verbose_name="course_teacher")

    def __str__(self):
        return self.course.title

    class Meta:
        verbose_name="03_course_table"
        db_table=verbose_name
        verbose_name_plural=verbose_name

class Teacher(models.Model):
    name = models.CharField(max_length=32, verbose_name="teacher_name")
    brief = models.TextField(max_length=1024, verbose_name="teacher_brief")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "04_teacher_table"
        db_table = verbose_name
        verbose_name_plural = verbose_name

class DegreeCourse(models.Model):
    title = models.CharField(max_length=32, verbose_name="degreecourse_name")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "05_degree_table"
        db_table = verbose_name
        verbose_name_plural = verbose_name

class CourseChapter(models.Model):
    course = models.ForeignKey(to="Course", related_name="course_chapters")
    chapter = models.SmallIntegerField(default=1, verbose_name="which_chapter")
    title = models.CharField(max_length=32, verbose_name="course_chapter_title")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "06_coursechapter_table"
        db_table = verbose_name
        verbose_name_plural = verbose_name
        unique_together = ("course", "chapter")

class CourseSection(models.Model):
    chapter = models.ForeignKey(to="CourseChapter", related_name="course_sections")
    title = models.CharField(max_length=32, verbose_name="keshi")
    section_order = models.SmallIntegerField(verbose_name="keshipaixu", help_text="")
    free_trail = models.BooleanField(verbose_name="shifoukekan", default=False)
    section_type_choices = ((0, 'file'), (1, 'practice'), (2, 'video'))
    section_type = models.SmallIntegerField(default=2, choices=section_type_choices)
    section_link = models.CharField(max_length=255, blank=True, null=True, help_text="if video is vid,elif file is link")

    def course_chapter(self):
        return self.chapter.chapter

    def course_name(self):
        return self.chapter.course.title

    def __str__(self):
        return "%s-%s" % (self.chapter, self.title)

    class Meta:
        verbose_name = "07_course_time_talbe"
        db_table = verbose_name
        verbose_name_plural = verbose_name
        unique_together = ('chapter', 'section_link')

class PricePolicy(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    valid_period_choices = ((1, '1day'), (3, '3day'),(7, '1week'), (14, '2week'),(30, '1month'),
                            (60, '2month'),(90, '3month'),(120, '4month'),(180, '6month'), (210, '12month'),
                            (540, '18month'), (720, '24month'),(722, '24month'), (723, '24month'),
                            )
    valid_period = models.SmallIntegerField(choices=valid_period_choices)
    price = models.FloatField()

    def __str__(self):
        return "%s(%s)%s" % (self.content_object, self.get_valid_period_display(), self.price)

    class Meta:
        verbose_name = "08_PricePolicy_table"
        db_table = verbose_name
        verbose_name_plural = verbose_name
        unique_together = ("content_type", 'object_id', "valid_period")

class OftenAskedQuestion(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    question = models.CharField(max_length=255)
    answer = models.TextField(max_length=1024)

    def __str__(self):
        return "%s-%s" % (self.content_object, self.question)

    class Meta:
        verbose_name = "09_oftenquestiontable"
        db_table = verbose_name
        verbose_name_plural = verbose_name
        unique_together = ('content_type', 'object_id', 'question')

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField(max_length=1024, verbose_name="pinglunneirong")
    user = models.ForeignKey("Userinfo", verbose_name="huiyuanming",null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "10_comment_table"
        db_table = verbose_name
        verbose_name_plural = verbose_name

class CourseOutline(models.Model):
    course_detail = models.ForeignKey(to="CourseDetail", related_name="course_outline")
    title = models.CharField(max_length=128)
    order = models.PositiveSmallIntegerField(default=1)
    content = models.TextField("neirong", max_length=2048)

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = "12_courseOutline_table"
        db_table = verbose_name
        verbose_name_plural = verbose_name
        unique_together = ('course_detail', 'title')

##############payment
class Coupon(models.Model):
    name = models.CharField(max_length=64, verbose_name="hongdongmingcheng")
    brief = models.TextField( verbose_name="youhuijuanjieshao",blank=True, null=True)
    coupon_type_choices = ((0, 'lijianjuan'), (1, 'manjianjuan'), (2, 'zhekoujuan'))
    coupon_type = models.SmallIntegerField(choices=coupon_type_choices, default=0, verbose_name="leixingjuan")

    money_equivalent_value = models.IntegerField(verbose_name="dengzhihuobi",blank=True,null=True)
    off_percent = models.PositiveSmallIntegerField("zhekoubaifenbi", help_text="zhekou，write7.9to79", blank=True, null=True)
    minimum_consume = models.PositiveIntegerField("zuidixiaofei", default=0, help_text="manjianjuanshitianxie")

    content_type = models.ForeignKey(ContentType, blank=True, null=True,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField("bangdingkecheng", blank=True, null=True, help_text="keyibayouhuijuanhekechengbangding")
    content_object = GenericForeignKey('content_type', 'object_id')

    quantity = models.PositiveIntegerField("shuliang", default=1)
    open_date = models.DateField("优惠券领取开始时间")
    close_date = models.DateField("优惠券领取结束时间")
    valid_begin_date = models.DateField(verbose_name="有效期开始时间", blank=True, null=True)
    valid_end_date = models.DateField(verbose_name="有效结束时间", blank=True, null=True)
    coupon_valid_days = models.PositiveIntegerField(verbose_name="优惠券有效期（天）", blank=True, null=True,
                                                    help_text="自券被领时开始算起")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "优惠券生成规则"

    def __str__(self):
        return "%s(%s)" % (self.get_coupon_type_display(), self.name)

class CouponRecord(models.Model):
    """优惠券发放、消费纪录"""
    coupon = models.ForeignKey("Coupon",on_delete=models.CASCADE)
    user = models.ForeignKey("Userinfo", verbose_name="拥有者",on_delete=models.CASCADE)
    status_choices = ((0, '未使用'), (1, '已使用'), (2, '已过期'))
    status = models.SmallIntegerField(choices=status_choices, default=0)
    get_time = models.DateTimeField(verbose_name="领取时间", help_text="用户领取时间")
    used_time = models.DateTimeField(blank=True, null=True, verbose_name="使用时间")

    class Meta:
        verbose_name_plural = " 优惠券发放、消费纪录"

    def __str__(self):
        return '%s-%s-%s' % (self.user,self.coupon,self.get_status_display())

######################################  订单表

class Order(models.Model):
        """订单"""
        payment_type_choices = ((0, '微信'), (1, '支付宝'), (2, '优惠码'), (3, '贝里'))
        payment_type = models.SmallIntegerField(choices=payment_type_choices)
        payment_number = models.CharField(max_length=128, verbose_name="支付第3方订单号", null=True, blank=True)
        order_number = models.CharField(max_length=128, verbose_name="订单号", unique=True)  # 考虑到订单合并支付的问题
        user = models.ForeignKey("Userinfo")
        actual_amount = models.FloatField(verbose_name="实付金额")

        status_choices = ((0, '交易成功'), (1, '待支付'), (2, '退费申请中'), (3, '已退费'), (4, '主动取消'), (5, '超时取消'))
        status = models.SmallIntegerField(choices=status_choices, verbose_name="状态")
        date = models.DateTimeField(auto_now_add=True, verbose_name="订单生成时间")
        pay_time = models.DateTimeField(blank=True, null=True, verbose_name="付款时间")
        cancel_time = models.DateTimeField(blank=True, null=True, verbose_name="订单取消时间")

        class Meta:
            verbose_name_plural = "订单表"

        def __str__(self):
            return "%s" % self.order_number

class OrderDetail(models.Model):
        """订单详情"""
        order = models.ForeignKey("Order")

        content_type = models.ForeignKey(ContentType)  # 可关联普通课程或学位
        object_id = models.PositiveIntegerField()
        content_object = GenericForeignKey('content_type', 'object_id')

        original_price = models.FloatField("课程原价")
        price = models.FloatField("折后价格")
        content = models.CharField(max_length=255, blank=True, null=True)  #
        valid_period_display = models.CharField("有效期显示", max_length=32)  # 在订单页显示
        valid_period = models.PositiveIntegerField("有效期(days)")  # 课程有效期
        memo = models.CharField(max_length=255, blank=True, null=True)

        def __str__(self):
            return "%s - %s - %s" % (self.order, self.content_type, self.price)

        class Meta:
            verbose_name_plural = "订单详细"
            unique_together = ("order", 'content_type', 'object_id')


