from django.urls import path
from app.views import home , edit , profile , delete

urlpatterns=[
    path('' ,home , name='home'),
    path('edit' ,edit , name='edit'),
    path('delete' ,delete , name='delete'),
    path('profile' ,profile, name='profile'),
]