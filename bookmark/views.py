from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark #bookmark 클래스가 필요하여 modes.py 에 있는bookmark 클래스를 import 합니다.
# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark
class BookmarkDV(DetailView):#Detai View는 상세 페이지를 만들어주는 역할을 함.
    model = Bookmark
