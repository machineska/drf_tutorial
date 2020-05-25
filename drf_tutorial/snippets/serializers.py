from rest_framework import serializers
from .models import Snippet


class SnippetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = "id title code lineos language style".split()
