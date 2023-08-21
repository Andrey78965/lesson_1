from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text='Отметьте, если торг уместен')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, null = True, blank = True)
    image = models.ImageField('изображение', upload_to='advertisements/')

    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style=" color: green; font-weight: bold; ">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y")

    @admin.display(description='дата обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style=" color: blue; font-weight: bold; ">Сегодня в {}</span>', updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y")
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    @admin.display(description='изображение')
    def image_1(self):
        if self.image:
         return format_html(
             '<img src="{}" style="max-height: 200px; max-width: 200px;">', self.image.url
         )

    class Meta:
        db_table = "advertisements"
'''http://127.0.0.1:8000/admin/app_advertisements/advertisement/advertisements.media
http://127.0.0.1:8000/advertisements/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2023-08-14_161438_VQUALDO.png'''

