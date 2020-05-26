from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Snippet
from .serializers import SnippetSerializers


@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    LIST all code snippets, or create a new snippet
    :param request:
    :return:
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializers = SnippetSerializers(snippets, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = SnippetSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    retrieve, update or delete a code snippet
    :param request:
    :param pk:
    :return:
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializers(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
