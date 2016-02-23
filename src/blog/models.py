#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

class lanmu(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name=u'栏目'
        verbose_name_plural=u'文章栏目'

class wenzhang(models.Model):
    lanmu = models.ForeignKey(lanmu,verbose_name=u'文章栏目')
    title = models.CharField(max_length=100,verbose_name=u'文章标题')
    neirong =models.TextField(max_length=10000)
    author=models.ForeignKey(User,verbose_name=u'文章作者')
    dgroup = models.ManyToManyField('Group')
    date = models.DateTimeField(auto_now_add=True,verbose_name=u'日期')
    
    
    def __unicode__(self):
        return u'%s %s'%(self.title,self.neirong)
    class Meta:
        verbose_name=u'文章'
        verbose_name_plural=u'文章'
    
class Adisplay(admin.ModelAdmin):
    list_display= ('lanmu','title','author','date')
class Group(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name=u'组'
        verbose_name_plural=u'组名'
    
class pinglun(models.Model):
    wenzhang = models.ForeignKey(wenzhang)
    neiroog = models.TextField(max_length=10000)
    
    class Meta:
        verbose_name=u'评论'
        verbose_name_plural=u'文章评论'

class AdminM(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __unicode__(self):
        return self.user.username
    class Meta:
        verbose_name=u'用户'
        verbose_name_plural=u'用户注册'


