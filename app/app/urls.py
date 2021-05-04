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

from paConfig.views import (
    FetchClientsApiView, 
    FetchStudyGroupApiView,
    ClientBindingsAPIView,
    MatrixBindingAPIView,
    FeaturesBindingAPIView
    )

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('pa/client', FetchClientsApiView.as_view()),
    path('pa/study-group', FetchStudyGroupApiView.as_view()),
    path('pa/client-binding', ClientBindingsAPIView.as_view()),
    path('pa/feature-binding', FeaturesBindingAPIView.as_view()),
    path('pa/matrix-binding', MatrixBindingAPIView.as_view()),
]
