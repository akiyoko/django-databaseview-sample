from django.db import models


class SalesTarget(models.Model):
    """売上目標モデル"""

    class Meta:
        db_table = 'sales_target'
        verbose_name = verbose_name_plural = '売上目標'

    sales_month = models.DateField('売上月')
    amount = models.PositiveIntegerField('目標金額')
    created_at = models.DateTimeField('登録日時', auto_now_add=True)

    def __str__(self):
        return f'{self.sales_month:%Y年%m月}'


class SalesResult(models.Model):
    """売上実績モデル"""

    class Meta:
        db_table = 'sales_result'
        verbose_name = verbose_name_plural = '売上実績'

    sales_date = models.DateField('売上日')
    amount = models.PositiveIntegerField('売上金額')
    subject = models.CharField('件名', max_length=255)
    created_at = models.DateTimeField('登録日時', auto_now_add=True)

    def __str__(self):
        return f'{self.sales_date:%Y年%m月%d日} - {self.subject}'


class SalesResultPerMonth(models.Model):
    """月別合計売上金額モデル"""

    class Meta:
        managed = False
        db_table = 'sales_result_per_month'
        verbose_name = verbose_name_plural = '月別合計売上金額'

    sales_month = models.DateField('売上月')
    total_amount = models.PositiveIntegerField('合計売上金額')
    target_amount = models.PositiveIntegerField('目標売上金額')
