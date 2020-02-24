"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from django.contrib import admin
from django.urls import path, include

from project.views import ProjectView, ProjectAPIView
from spaces.views import SpaceAPIView
from board.views import BoardAPIView
from task.views import TaskAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    # path('refresh/', TokenRefreshView.as_view()),
    path('project/', ProjectAPIView.as_view()),
    path('space/', SpaceAPIView.as_view()),
    path('board/', BoardAPIView.as_view()),
    path('task/', TaskAPIView.as_view())
]
