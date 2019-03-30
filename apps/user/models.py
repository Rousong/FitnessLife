from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel

class User(AbstractUser, BaseModel):
    '''用户模型类'''

    class Meta:
        db_table = 'fit_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

class UserInfo(BaseModel):
    '''用户信息类'''
    gender_choices = (
        (0, ''),
        (1, '男♂'),
        (2,'女♀'),
        (3,'⚧')
    )

    blood_choices = (
        (0,''),
        (1, 'A'),
        (2, 'B'),
        (3, 'AB'),
        (4, 'O'),
    )
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='所属账户')
    gender = models.SmallIntegerField(default=0, choices=gender_choices, verbose_name='性别')
    blood = models.SmallIntegerField(default=0, choices=blood_choices, verbose_name='血型')
    image = models.ImageField(upload_to='banner', verbose_name='活动图片')
    start_workout_data = models.DateField(verbose_name='健身开始日')

    class Meta:
        db_table = 'user_userinfo'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

class WorkoutPlan(BaseModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='所属账户')
    Monday = models.CharField(max_length=50, verbose_name='周一健身计划')
    Tuesday = models.CharField(max_length=50, verbose_name='周二健身计划')
    Wednesday = models.CharField(max_length=50, verbose_name='周三健身计划')
    Thursday = models.CharField(max_length=50, verbose_name='周四健身计划')
    Friday = models.CharField(max_length=50, verbose_name='周五健身计划')
    Saturday = models.CharField(max_length=50, verbose_name='周六健身计划')
    Sunday = models.CharField(max_length=50, verbose_name='周日健身计划')


    class Meta:
        db_table = 'user_workoutplan'
        verbose_name = '健身计划'
        verbose_name_plural = verbose_name
