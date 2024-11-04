from django.urls import path
from .views import ArticleListView, ArticleDeleteView, ArticleUpdateView, ArticleDetailView, ArticleCreateView, CommentDeleteView, CommentEditView

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"), 
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_update"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("comment/<int:pk>/edit/", CommentEditView.as_view(), name="comment_edit"), 
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
]