from types import NoneType
from typing import Collection, Literal, TypeAlias, TypeVar


from library.models import PerformantQuerySet


T = TypeVar("T")
PerformantQuerySetT = TypeVar("PerformantQuerySetT", bound=PerformantQuerySet)
Scalar: TypeAlias = bool | int | float | str | NoneType
C = TypeVar("C", bound=Collection)
Period = Literal["current", "previous"]
