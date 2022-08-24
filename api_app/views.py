from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from .models.account import Account
from .models.community import Community
from .models.issue import Issue
from .models.question import Question
from .models.message import Message
from .models.tag import Tag
from .models.webpage import Webpage
from . import serializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = serializer.AccountSerializer
    
class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = serializer.CommunitySerializer
    
class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = serializer.IssueSerializer
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = serializer.QuestionSerializer
    
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = serializer.MessageSerializer
    
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = serializer.TagSerializer
    
class WebpageViewSet(viewsets.ModelViewSet):
    queryset = Webpage.objects.all()
    serializer_class = serializer.WebpageSerializer

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('api_app:login'))
    
    return HttpResponseRedirect(reverse('api_app:home'))

def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'api_app/sign_up.html')
    
def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            logout(request)
        return render(request, 'api_app/login.html')
    if request.method == 'POST':
        user_name = request.POST.get('userName')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        
        if user is not None:
            login(request, user)
            # return HttpResponseRedirect(reverse('home'))
            html = '<html><body>success</body></html>'
            return HttpResponse(html)
                
        messages.error(request, '入力情報に間違いがあります')
        return HttpResponseRedirect('.')
    
    raise Http404('Request method is not GET or POST.')
        
def home_view(request):
    return render(request, 'api_app/home.html')

def community_view(request):
    return render(request, 'api_app/community.html')


def profile_view(request):
     if request.method == 'GET':
         return render(request, 'api_app/profile.html')
    #画像をフォルダに保存する処理
     if request.method == 'POST':
        # uploaded_filename = request.FILES['file']
        # uploaded_filename.save()
        # fs = FileSystemStorage()
        # filename = fs.save(uploaded_filename.name,uploaded_filename)



    
def test_create_user(request):
    user = User.objects.create_user(username='ozaki', password='muit-hack')
    user.save()
    return HttpResponseRedirect(reverse('result'))

def test_result(request):
    user = authenticate(username='ozaki', password='muit-hack')
    print(user)
    html = '<html><body>fail</body></html>'
    if user is not None:
        html = '<html><body>success</body></html>'
    return HttpResponse(html)

def test_vue(request):
    return render(request, 'api_app/oza_test.html')