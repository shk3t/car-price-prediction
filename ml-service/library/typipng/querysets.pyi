from typing import Any, Self

from django.db.models import QuerySet
from django.db.models.expressions import Combinable

class TypedQuerySet(QuerySet):
    def values(self, *fields: str | Combinable, **expressions: Any) -> Self: ...
    def values_list(
        self, *fields: str | Combinable, flat: bool = ..., named: bool = ...
    ) -> Self: ...
