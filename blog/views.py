from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post #LIstView로 보여줄 객체를 post로 지정하기 위해서 post import 합니다.

# Create your views here.
class PostLV(ListView):
    model = Post

class PostDV(DetailView):
    model = Post

