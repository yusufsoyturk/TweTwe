from django.shortcuts import render, redirect
from . import models
from django.urls import reverse , reverse_lazy
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.
def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets" : all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        message = request.POST["message"]
        # models.Tweet.objects.create(nickname=nickname, message=message)
        tweet1 = models.Tweet(username=request.user, message=message)
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

@login_required
def deletetweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect('tweetapp:listtweet')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
