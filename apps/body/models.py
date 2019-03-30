from django.db import models
from db.base_model import BaseModel

class BodyManage(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='所属账户')
    # Decimal 实例表示固定精度的十进制数的字段。它有两个必须的参数：max_digits：数字允许的最大位数 decimal_places：小数的最大位数
    height = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='身高')
    weight = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='体重')
    BMI = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='BMI')
    fat_rate = models.DecimalField(max_digits=2, decimal_places=2, verbose_name='体脂率')
    xiongwei = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='胸围')
    biwei = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='臂围')
    jiankaun = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='肩宽')
    yaowei = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='腰围')
    tunwei = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='臀围')
    datuiwei = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='腿围')

    class Meta:
        db_table = 'body_bodymanage'
        verbose_name = '身材记录管理'
        verbose_name_plural = verbose_name