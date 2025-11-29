from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('', views.listtweet, name='listtweet'), #abc.com/tweetapp/
    path('addtweet/', views.addtweet, name='addtweet'), #abc.com/tweetapp/addtweet
    path('addtweetbyform/', views.addtweetbyform, name='addtweetbyform'), #abc.com/tweetapp/addtweetbyform
    path('addtweetbymodelform/', views.addtweetbymodelform, name='addtweetbymodelform'), #abc.com/tweetapp/addtweetbymodelform
]