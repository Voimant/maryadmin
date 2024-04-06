from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Affairs, Record
# Register your models here.


@admin.register(Affairs)
class AffairsAdmin(admin.ModelAdmin):
    fields = ['number_affair', 'date', 'plaintiff', 'defendant', 'court', 'dispute', 'summ_plaintiff', 'result_client', 'result_court',
               'purist', 'urls', 'category', 'sub_category', 'image_result', 'role']

    list_display = [
        'number_affair', 'category', 'sub_category'
    ]
    readonly_fields = [
        'number_affair', 'category', 'sub_category'
    ]

    search_fields = [
        'number_affair', 'category', 'sub_category'
    ]

    list_filter = [
        'number_affair', 'category', 'sub_category'
    ]

    save_on_top = True

    @admin.display(description="Изображение")
    def post_photo(self, info: Affairs):
        if info.image_result:
            return mark_safe(f"<img src='{info.image_result.url}' width=50 hieght=50>")
        return "Нет изображения"


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    fields = [
        'name', 'numbers_phone', 'dispute', 'username'
    ]

    list_display = [
        'name', 'numbers_phone', 'dispute', 'username'
    ]

