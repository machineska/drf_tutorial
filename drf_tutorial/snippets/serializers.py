from rest_framework import serializers
from .models import Snippet


class SnippetSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False, allow_blank=True,
        max_length=100,
    )
    code = serializers.CharField(style={'base_template': 'text_area.html'})
    lineos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(
        choices=Snippet.LANGUAGE_CHOICES,
        default='python',
    )
    style = serializers.ChoiceField(
        choices=Snippet.STYLE_CHOICES,
        default='friendly'
    )

    def create(self, validated_data):
        """
        Create and return a new Snippet instance, given the validated data
        :param validated_data:
        :return:
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance: Snippet, validated_data):
        """
        Update and return an existing Snippets instance, given validated data
        :param instance:
        :param validated_data:
        :return:
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.lineos = validated_data.get('lineos', instance.lineos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
