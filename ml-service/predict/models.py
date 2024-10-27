from django.db import models


class CarInfo(models.Model):
    class Meta:
        db_table = "user_file"
        verbose_name = "Запись об автомобиле"
        verbose_name_plural = "Записи об автомобилях"

    url = models.CharField("URL на auto.ru", max_length=256)
    image = models.CharField("URL изображения на auto.ru", max_length=512)
    brand = models.CharField("Бренд", max_length=64)
    model = models.CharField("Название модели", max_length=64)
    model_year = models.IntegerField("Год выпуска")
    milage_km = models.IntegerField("Пробег в милях")
    fuel_type = models.CharField("Тип топлива", max_length=64)
    engine_volume = models.FloatField("Объем двигателя (л.)")
    engine_power = models.IntegerField("Мощность двигателя (л.с.)")
    transmission_speed = models.IntegerField(
        "Ступеней коробки передач", null=True, blank=True
    )
    transmission_type = models.CharField("Тип коробки передач", max_length=64)
    color = models.CharField("Цвет кузова", max_length=64)
    interior_color = models.CharField(
        "Цвет салона", max_length=64, null=True, blank=True
    )
    accident = models.CharField("Участие в ДТП", max_length=128, null=True, blank=True)
    clean_title = models.BooleanField("Растаможен")
    price_rub = models.IntegerField("Цена в рублях")
    recommended_price_rub = models.IntegerField("Рекомендованная цена в рублях")