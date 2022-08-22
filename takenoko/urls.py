"""takenoko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api_app.views import UserViewSet
from api_app.views import AccountViewSet
from api_app.views import CommunityViewSet
from api_app.views import IssueViewSet
from api_app.views import QuestionViewSet
from api_app.views import MessageViewSet
from api_app.views import TagViewSet
from api_app.views import WebpageViewSet

defaultRouter = routers.DefaultRouter()
defaultRouter.register('user', UserViewSet)
defaultRouter.register('account', AccountViewSet)
defaultRouter.register('community', CommunityViewSet)
defaultRouter.register('issue', IssueViewSet)
defaultRouter.register('question', QuestionViewSet)
defaultRouter.register('message', MessageViewSet)
defaultRouter.register('tag', TagViewSet)
defaultRouter.register('webpage', WebpageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api_app.urls')),
    path('api/', include(defaultRouter.urls)),
]
