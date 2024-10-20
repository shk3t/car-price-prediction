from django.apps import apps
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email: str, password: str, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user = self._create_user(email, password, **extra_fields)

        UserParams = apps.get_model("users.UserParams")
        WarehouseParams = apps.get_model("users.WarehouseParams")
        ProductionParams = apps.get_model("users.ProductionParams")
        user_params = UserParams.objects.create(user=user)
        WarehouseParams.create_missing(user_params)
        ProductionParams.create_missing(user_params)

        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)
