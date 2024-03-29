from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.
def home(request):
    return render(request,'home.html')


# Create your views here.
class PostList(generic.ListView):
    queryset=Post.objects.filter(status=1).order_by('-published_on')
    template_name='index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name='post_detail.html'