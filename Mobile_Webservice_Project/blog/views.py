from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

#added
from rest_framework import viewsets
from .serializers import PostSerializer

class IntruderImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer