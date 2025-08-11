from django.shortcuts import render, redirect
from .form import TweetForm
from .models import tweet
from django.shortcuts import get_object_or_404

# Create your views here.


def hello(request):
    return render(request, "index.html")


def tweetList(request):
    tweets = tweet.objects.all().order_by("-created_at")
    return render(request, "tweetList.html", {"tweets": tweets})


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


def tweet_edit(request, tweet_id):
    tweets = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweets = form.save(commit=False)
            tweets.user = request.user
            tweets.save()
            return redirect("tweetList")
    else:
        form = TweetForm(instance=tweet)
    return render(request, "tweet_form.html", {"form": form})


def tweet_delete(request, tweet_id):
    tweets = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweets.delete()
        return redirect("tweetList")
    return render(request, "tweet_confirm_delete.html", {"tweet": tweets})
