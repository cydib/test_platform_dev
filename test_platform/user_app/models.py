from django.db import models


# Create your models here.


class Project(models.Model):
    '''
    项目表
    '''
    name = models.CharField("名称", max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    status = models.BooleanField("状态", default="")
    create_time = models.DateTimeField("创建时间", auto_created=True)

    # 在admin后台显示创建时的标题，而不是project1、2
    def __str__(self):
        return self.name


class Module(models.Model):
    '''
    模块表
    '''
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    create_time = models.DateTimeField("创建时间", auto_created=True)

    def __str__(self):
        return self.name
