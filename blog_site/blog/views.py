from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerilizer
# Create your views here.
class blogpost(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class =  BlogPostSerilizer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response ('All Blog Post have been deleted', status=status.HTTP_204_NO_CONTENT)

class post(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class =  BlogPostSerilizer
    lookup_field = 'pk'

@api_view()
def filter_blog(request):
    items = BlogPost.objects.all()
    get_title = request.query_params.get('title')
    if get_title:
        items = items.filter(title__contains = get_title)

    serialized_item = BlogPostSerilizer(items, many=True)
    return Response(serialized_item.data)

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response('This is a secret message', status=status.HTTP_200_OK)
