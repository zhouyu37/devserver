# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-01-09 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app01', '0002_auto_20200108_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='course_category')),
            ],
            options={
                'db_table': '01_course_category',
                'verbose_name': '01_course_category',
                'verbose_name_plural': '01_course_category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content', models.TextField(max_length=1024, verbose_name='pinglunneirong')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'db_table': '10_comment_table',
                'verbose_name': '10_comment_table',
                'verbose_name_plural': '10_comment_table',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='hongdongmingcheng')),
                ('brief', models.TextField(blank=True, null=True, verbose_name='youhuijuanjieshao')),
                ('coupon_type', models.SmallIntegerField(choices=[(0, 'lijianjuan'), (1, 'manjianjuan'), (2, 'zhekoujuan')], default=0, verbose_name='leixingjuan')),
                ('money_equivalent_value', models.IntegerField(blank=True, null=True, verbose_name='dengzhihuobi')),
                ('off_percent', models.PositiveSmallIntegerField(blank=True, help_text='zhekou\uff0cwrite7.9to79', null=True, verbose_name='zhekoubaifenbi')),
                ('minimum_consume', models.PositiveIntegerField(default=0, help_text='manjianjuanshitianxie', verbose_name='zuidixiaofei')),
                ('object_id', models.PositiveIntegerField(blank=True, help_text='keyibayouhuijuanhekechengbangding', null=True, verbose_name='bangdingkecheng')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='shuliang')),
                ('open_date', models.DateField(verbose_name='\u4f18\u60e0\u5238\u9886\u53d6\u5f00\u59cb\u65f6\u95f4')),
                ('close_date', models.DateField(verbose_name='\u4f18\u60e0\u5238\u9886\u53d6\u7ed3\u675f\u65f6\u95f4')),
                ('valid_begin_date', models.DateField(blank=True, null=True, verbose_name='\u6709\u6548\u671f\u5f00\u59cb\u65f6\u95f4')),
                ('valid_end_date', models.DateField(blank=True, null=True, verbose_name='\u6709\u6548\u7ed3\u675f\u65f6\u95f4')),
                ('coupon_valid_days', models.PositiveIntegerField(blank=True, help_text='\u81ea\u5238\u88ab\u9886\u65f6\u5f00\u59cb\u7b97\u8d77', null=True, verbose_name='\u4f18\u60e0\u5238\u6709\u6548\u671f\uff08\u5929\uff09')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': '\u4f18\u60e0\u5238\u751f\u6210\u89c4\u5219',
            },
        ),
        migrations.CreateModel(
            name='CouponRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(0, '\u672a\u4f7f\u7528'), (1, '\u5df2\u4f7f\u7528'), (2, '\u5df2\u8fc7\u671f')], default=0)),
                ('get_time', models.DateTimeField(help_text='\u7528\u6237\u9886\u53d6\u65f6\u95f4', verbose_name='\u9886\u53d6\u65f6\u95f4')),
                ('used_time', models.DateTimeField(blank=True, null=True, verbose_name='\u4f7f\u7528\u65f6\u95f4')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Coupon')),
            ],
            options={
                'verbose_name_plural': ' \u4f18\u60e0\u5238\u53d1\u653e\u3001\u6d88\u8d39\u7eaa\u5f55',
            },
        ),
        migrations.CreateModel(
            name='CourseChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.SmallIntegerField(default=1, verbose_name='which_chapter')),
                ('title', models.CharField(max_length=32, verbose_name='course_chapter_title')),
            ],
            options={
                'db_table': '06_coursechapter_table',
                'verbose_name': '06_coursechapter_table',
                'verbose_name_plural': '06_coursechapter_table',
            },
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField(default=7, verbose_name='course_time')),
                ('video_brief_link', models.CharField(blank=True, max_length=256, null=True)),
                ('summary', models.TextField(max_length=2048, verbose_name='verbose_summary')),
                ('why_study', models.TextField(verbose_name='why study')),
                ('what_to_study_brief', models.TextField(verbose_name='what to study')),
                ('career_improvement', models.TextField(verbose_name='be helped to ')),
            ],
            options={
                'db_table': '03_course_table',
                'verbose_name': '03_course_table',
                'verbose_name_plural': '03_course_table',
            },
        ),
        migrations.CreateModel(
            name='CourseOutline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('order', models.PositiveSmallIntegerField(default=1)),
                ('content', models.TextField(max_length=2048, verbose_name='neirong')),
                ('course_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_outline', to='app01.CourseDetail')),
            ],
            options={
                'db_table': '12_courseOutline_table',
                'verbose_name': '12_courseOutline_table',
                'verbose_name_plural': '12_courseOutline_table',
            },
        ),
        migrations.CreateModel(
            name='CourseSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='keshi')),
                ('section_order', models.SmallIntegerField(verbose_name='keshipaixu')),
                ('free_trail', models.BooleanField(default=False, verbose_name='shifoukekan')),
                ('section_type', models.SmallIntegerField(choices=[(0, 'file'), (1, 'practice'), (2, 'video')], default=2)),
                ('section_link', models.CharField(blank=True, help_text='if video is vid,elif file is link', max_length=255, null=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_sections', to='app01.CourseChapter')),
            ],
            options={
                'db_table': '07_course_time_talbe',
                'verbose_name': '07_course_time_talbe',
                'verbose_name_plural': '07_course_time_talbe',
            },
        ),
        migrations.CreateModel(
            name='DegreeCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='degreecourse_name')),
            ],
            options={
                'db_table': '05_degree_table',
                'verbose_name': '05_degree_table',
                'verbose_name_plural': '05_degree_table',
            },
        ),
        migrations.CreateModel(
            name='OftenAskedQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField(max_length=1024)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'db_table': '09_oftenquestiontable',
                'verbose_name': '09_oftenquestiontable',
                'verbose_name_plural': '09_oftenquestiontable',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.SmallIntegerField(choices=[(0, '\u5fae\u4fe1'), (1, '\u652f\u4ed8\u5b9d'), (2, '\u4f18\u60e0\u7801'), (3, '\u8d1d\u91cc')])),
                ('payment_number', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u652f\u4ed8\u7b2c3\u65b9\u8ba2\u5355\u53f7')),
                ('order_number', models.CharField(max_length=128, unique=True, verbose_name='\u8ba2\u5355\u53f7')),
                ('actual_amount', models.FloatField(verbose_name='\u5b9e\u4ed8\u91d1\u989d')),
                ('status', models.SmallIntegerField(choices=[(0, '\u4ea4\u6613\u6210\u529f'), (1, '\u5f85\u652f\u4ed8'), (2, '\u9000\u8d39\u7533\u8bf7\u4e2d'), (3, '\u5df2\u9000\u8d39'), (4, '\u4e3b\u52a8\u53d6\u6d88'), (5, '\u8d85\u65f6\u53d6\u6d88')], verbose_name='\u72b6\u6001')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='\u8ba2\u5355\u751f\u6210\u65f6\u95f4')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='\u4ed8\u6b3e\u65f6\u95f4')),
                ('cancel_time', models.DateTimeField(blank=True, null=True, verbose_name='\u8ba2\u5355\u53d6\u6d88\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u8ba2\u5355\u8868',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('original_price', models.FloatField(verbose_name='\u8bfe\u7a0b\u539f\u4ef7')),
                ('price', models.FloatField(verbose_name='\u6298\u540e\u4ef7\u683c')),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
                ('valid_period_display', models.CharField(max_length=32, verbose_name='\u6709\u6548\u671f\u663e\u793a')),
                ('valid_period', models.PositiveIntegerField(verbose_name='\u6709\u6548\u671f(days)')),
                ('memo', models.CharField(blank=True, max_length=255, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Order')),
            ],
            options={
                'verbose_name_plural': '\u8ba2\u5355\u8be6\u7ec6',
            },
        ),
        migrations.CreateModel(
            name='PricePolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('valid_period', models.SmallIntegerField(choices=[(1, '1day'), (3, '3day'), (7, '1week'), (14, '2week'), (30, '1month'), (60, '2month'), (90, '3month'), (120, '4month'), (180, '6month'), (210, '12month'), (540, '18month'), (720, '24month'), (722, '24month'), (723, '24month')])),
                ('price', models.FloatField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'db_table': '08_PricePolicy_table',
                'verbose_name': '08_PricePolicy_table',
                'verbose_name_plural': '08_PricePolicy_table',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='teacher_name')),
                ('brief', models.TextField(max_length=1024, verbose_name='teacher_brief')),
            ],
            options={
                'db_table': '04_teacher_table',
                'verbose_name': '04_teacher_table',
                'verbose_name_plural': '04_teacher_table',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='username')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_type', models.IntegerField(choices=[(1, 'normal user'), (2, 'VIP'), (3, 'SVIP')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.UserInfo')),
            ],
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '02_course_table', 'verbose_name_plural': '02_course_table'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='img',
        ),
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
        migrations.AddField(
            model_name='course',
            name='brief',
            field=models.CharField(max_length=1024, null=True, verbose_name='course_brief'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_img',
            field=models.ImageField(blank=True, null=True, upload_to='course/%Y-%m', verbose_name='course_img'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.SmallIntegerField(choices=[(0, 'fufei'), (1, 'vip'), (2, 'xuewei')], default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.SmallIntegerField(choices=[(0, 'junior'), (1, 'intermediate'), (2, 'senior')], default=1),
        ),
        migrations.AddField(
            model_name='course',
            name='order',
            field=models.IntegerField(default=0, help_text='shun xu', verbose_name='course_order'),
        ),
        migrations.AddField(
            model_name='course',
            name='pub_date',
            field=models.DateField(blank=True, null=True, verbose_name='pub_data'),
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'online'), (1, 'offline'), (2, 'test')], default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='study_num',
            field=models.IntegerField(default=1, help_text='buyers', verbose_name='learner_num'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=128, unique=True, verbose_name='course_name'),
        ),
        migrations.AlterModelTable(
            name='course',
            table='02_course_table',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserInfo'),
        ),
        migrations.AddField(
            model_name='coursedetail',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.Course'),
        ),
        migrations.AddField(
            model_name='coursedetail',
            name='recommend_courses',
            field=models.ManyToManyField(blank=True, related_name='recommend_by', to='app01.Course'),
        ),
        migrations.AddField(
            model_name='coursedetail',
            name='teachers',
            field=models.ManyToManyField(to='app01.Teacher', verbose_name='course_teacher'),
        ),
        migrations.AddField(
            model_name='coursechapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_chapters', to='app01.Course'),
        ),
        migrations.AddField(
            model_name='couponrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserInfo', verbose_name='\u62e5\u6709\u8005'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.UserInfo', verbose_name='huiyuanming'),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Category', verbose_name='course_category'),
        ),
        migrations.AddField(
            model_name='course',
            name='degree_course',
            field=models.ForeignKey(blank=True, help_text='degree course must be related to degreecourse', null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.DegreeCourse'),
        ),
        migrations.AlterUniqueTogether(
            name='pricepolicy',
            unique_together=set([('content_type', 'object_id', 'valid_period')]),
        ),
        migrations.AlterUniqueTogether(
            name='orderdetail',
            unique_together=set([('order', 'content_type', 'object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='oftenaskedquestion',
            unique_together=set([('content_type', 'object_id', 'question')]),
        ),
        migrations.AlterUniqueTogether(
            name='coursesection',
            unique_together=set([('chapter', 'section_link')]),
        ),
        migrations.AlterUniqueTogether(
            name='courseoutline',
            unique_together=set([('course_detail', 'title')]),
        ),
        migrations.AlterUniqueTogether(
            name='coursechapter',
            unique_together=set([('course', 'chapter')]),
        ),
    ]