from django.urls import path
from app.views import home , edit , profile , delete , add , delete

urlpatterns=[
    path('' ,home , name='home'),
    path('edit/<int:id>' ,edit , name='edit'),
    path('delete' ,delete , name='delete'),
    path('profile/<int:id>' ,profile, name='profile'),
    path('add' , add , name='add'),
    path('delete/<int:id>' , delete , name='delete'),
]