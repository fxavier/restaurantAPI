import graphene
from graphene_django.types import DjangoObjectType
from .models import YourModel


class ModelType(DjangoObjectType):
    class Meta:
        model = YourModel


class Query:
    attrs = graphene.List(ModelType)
    attr = graphene.Field(ModelType, attr_id=graphene.String(required=True))

    def resolve_attrs(self, info, **kwargs):
        # Querying a list
        return YourModel.objects.all()

    def resolve_attr(self, info, attr_id):
        # Querying a single question
        return YourModel.objects.get(pk=attr_id)
