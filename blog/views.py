from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post #LIstView로 보여줄 객체를 post로 지정하기 위해서 post import 합니다.
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class PostLV(ListView):
    model = Post

class PostDV(DetailView):
    model = Post


class PostCV(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'image', 'description']
    initial = {'slug':'auto-filling-do-not-input'}
    success_url = reverse_lazy('blog_index')

    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super(PostCV, self).form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog_index')
