from django.shortcuts import render, redirect
from .form import TweetForm
from .models import tweet
from django.shortcuts import get_object_or_404

# Create your views here.


def hello(request):
    return render(request, "index.html")


def tweetList(request):
    tweets = tweet.objects.all().order_by("-created_at")
    return render(request, "tweetList.html", {"tweet": tweets})


def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweetList")
    else:
        form = TweetForm()
        return render(request, "tweet_form.html", {"form": form})
