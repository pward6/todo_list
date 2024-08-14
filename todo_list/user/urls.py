from django.urls import path
from .views import signup, signin, user_profile, logout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout', logout, name='logout'),
    path('profile/', user_profile, name='profile'),
]
