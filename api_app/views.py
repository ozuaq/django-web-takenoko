from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

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

def test(request):
    if request.GET.get('account_id'):
        request.session['account_id'] = request.GET.get('account_id')
    return render(request, 'api_app/test.html')

def test2(request):
    if request.GET.get('account_id'):
        request.session['account_id'] = request.GET.get('account_id')