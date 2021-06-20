from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI, UsersAPI
from knox import views as knox_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('accounts/users', UsersAPI, basename='users')
k = router.urls
k.append(path('accounts/auth', include('knox.urls')))
k.append(path('accounts/register', RegisterAPI.as_view()))
k.append( path('accounts/login', LoginAPI.as_view()))
k.append(path('accounts/user', UserAPI.as_view()))
k.append(path('accounts/logout', knox_views.LogoutView.as_view()))


urlpatterns =k