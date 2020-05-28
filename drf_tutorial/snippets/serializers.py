from rest_framework import serializers
from .models import Snippet


class SnippetSerializers(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = "id owner title code lineos highlighted language style".split()
