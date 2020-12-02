from django.contrib import admin

from common.helpers.admin_helper import format_yen, format_yyyy_nen_mm_gatsu
from .models import SalesResult, SalesResultPerMonth, SalesTarget


class SalesResultAdmin(admin.ModelAdmin):
    """売上実績モデル用 ModelAdmin"""

    ###############################
    # モデル一覧画面のカスタマイズ
    ###############################
    list_display = ('sales_date', 'format_amount', 'subject')
    ordering = ('sales_date', 'created_at')

    def format_amount(self, obj):
        return format_yen(obj.amount)

    format_amount.short_description = '売上金額'
    format_amount.admin_order_field = 'amount'

    ###############################
    # モデル追加・変更画面のカスタマイズ
    ###############################
    readonly_fields = ('id', 'created_at')


class SalesTargetAdmin(admin.ModelAdmin):
    """売上目標モデル用 ModelAdmin"""

    ###############################
    # モデル一覧画面のカスタマイズ
    ###############################
    list_display = ('format_sales_month', 'format_amount')
    ordering = ('sales_month',)

    def format_sales_month(self, obj):
        return format_yyyy_nen_mm_gatsu(obj.sales_month)

    format_sales_month.short_description = '売上月'
    format_sales_month.admin_order_field = 'sales_month'

    def format_amount(self, obj):
        return format_yen(obj.amount)

    format_amount.short_description = '目標金額'
    format_amount.admin_order_field = 'amount'

    ###############################
    # モデル追加・変更画面のカスタマイズ
    ###############################
    readonly_fields = ('id', 'created_at')


class SalesResultPerMonthAdmin(admin.ModelAdmin):
    """月別合計売上金額モデル用 ModelAdmin"""

    ###############################
    # モデル一覧画面のカスタマイズ
    ###############################
    list_display = ('format_sales_month', 'format_target_amount', 'format_total_amount')
    ordering = ('sales_month',)

    def format_sales_month(self, obj):
        return format_yyyy_nen_mm_gatsu(obj.sales_month)

    format_sales_month.short_description = '売上月'
    format_sales_month.admin_order_field = 'sales_month'

    def format_target_amount(self, obj):
        return format_yen(obj.target_amount)

    format_target_amount.short_description = '目標売上金額'
    format_target_amount.admin_order_field = 'target_amount'

    def format_total_amount(self, obj):
        return format_yen(obj.total_amount)

    format_total_amount.short_description = '合計売上金額'
    format_total_amount.admin_order_field = 'total_amount'

    ###############################
    # その他のカスタマイズ
    ###############################
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(SalesTarget, SalesTargetAdmin)
admin.site.register(SalesResult, SalesResultAdmin)
admin.site.register(SalesResultPerMonth, SalesResultPerMonthAdmin)
