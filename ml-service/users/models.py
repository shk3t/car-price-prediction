from typing import TYPE_CHECKING

import env
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from library.models import PerformantModel

from .managers import UserManager

if TYPE_CHECKING:
    from users import models as TypingModels


class User(AbstractUser, PerformantModel):
    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    objects: UserManager = UserManager()  # type: ignore

    name = models.CharField("Имя пользователя", max_length=64, default="")
    email = models.EmailField("Электронная почта", unique=True)
    phone = models.CharField("Номер телефона", max_length=32, default="")
    company_name = models.CharField("Название компании", max_length=64, default="")
    company_min_sales = models.DecimalField(
        "Минимальный оборот компании", max_digits=16, decimal_places=2, default=0.0
    )
    company_max_sales = models.DecimalField(
        "Максимальный оборот компании", max_digits=16, decimal_places=2, default=0.0
    )
    company_inn = models.CharField("ИНН компании", max_length=16, default="")

    username = None
    first_name = None
    last_name = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    _OWNERSHIP_LOOKUPS = {
        "Nomenclature": "card__wb_account__user",
        "Size": "nomenclature__card__wb_account__user",
        "Purchase": "nomenclature__card__wb_account__user",
        "SalesPlan": "user",
        "NomenclatureTag": "nomenclature__card__wb_account__user",
        "WbAccount": "user",
    }

    def __str__(self) -> str:
        return f"{self.email}"

    if TYPE_CHECKING:
        id: int

    def check_password(self, raw_password):
        if env.AUTH_BY_DIRECT_HASH and raw_password == self.password:
            return True

        def setter(raw_password):
            self.set_password(raw_password)
            self._password = None  # type: ignore
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)
