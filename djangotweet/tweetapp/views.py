from django.shortcuts import render, redirect
from . import models
from django.urls import reverse
from . import forms

# Create your views here.
def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets" : all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

def addtweet(request):
    if request.POST:
        nickname = request.POST["nickname"]
        message = request.POST["message"]
        # models.Tweet.objects.create(nickname=nickname, message=message)
        tweet1 = models.Tweet(nickname=nickname, message=message)
        tweet1.save()
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request, 'tweetapp/addtweet.html')
    
def addtweetbyform(request):
    if request.POST:
        form = forms.AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname=nickname, message = message)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            return render(request, 'tweetapp/addtweetbyform.html', context={"form":form})
    else:
        form = forms.AddTweetForm()
        return render(request, 'tweetapp/addtweetbyform.html', context={"form":form})
    
def addtweetbymodelform(request):
    if request.POST:
        form = forms.AddTweetModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname, message = message)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            return render(request, 'tweetapp/addtweetbymodelform.html', context={"form":form})
    else:
        form = forms.AddTweetModelForm()
        return render(request, 'tweetapp/addtweetbymodelform.html', context={"form":form})