from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('', views.listtweet, name='listtweet'), #abc.com/
    path('addtweet/', views.addtweet, name='addtweet'), #abc.com/addtweet
    path('addtweetbyform/', views.addtweetbyform, name='addtweetbyform'), #abc.com/addtweetbyform
    path('addtweetbymodelform/', views.addtweetbymodelform, name='addtweetbymodelform'), #abc.com/addtweetbymodelform
    path('signup/', views.SignUpView.as_view(), name="signup"), # abc.com/signup
    path('deletetweet/<int:id>', views.deletetweet, name="deletetweet") #
]