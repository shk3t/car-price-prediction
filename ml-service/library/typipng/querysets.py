from django.db.models import QuerySet


class TypedQuerySet(QuerySet):
    class Meta:
        abstract = True
