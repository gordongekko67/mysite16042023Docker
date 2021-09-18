from rest_framework import serializers
from funzioniiot.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Titoli2


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']



class Titoli2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Titoli2
        fields = ['id', 'codtit2', 'codslugtit2', 'codauthortit2', 'codisintit2', 'codbodytit2']

   