from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweetList, name="TweetList"),
    path("create/", views.tweet_create, name="tweet_create"),
    path("<int:tweet_id>/edit/", views.tweet_edit, name="tweet_edit"),
    path("<int:tweet_id>/delete/", views.tweet_delete, name="tweet_delete"),
]
