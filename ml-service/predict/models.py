from django.db import models


class CarEntry(models.Model):
    class Meta:
        db_table = "user_file"
        verbose_name = "Запись об автомобиле"
        verbose_name_plural = "Записи об автомобилях"

    brand = models.CharField("Бренд", max_length=64)
    model = models.CharField("Название модели", max_length=64)
    model_year = models.IntegerField("Год выпуска")
    milage = models.IntegerField("Пробег в милях")
    fuel_type = models.CharField("Тип топлива", max_length=64)
    engine = models.CharField("Двигатель", max_length=128)
    transmission = models.CharField("Коробка передач", max_length=64)
    ext_col = models.CharField("Цвет кузова", max_length=64)
    int_col = models.CharField("Цвет салона", max_length=64)
    accident = models.CharField("Участие в ДТП", max_length=128)
    clean_title = models.CharField("Чистый номер", max_length=64)
    price = models.IntegerField("Цена в долларах")
