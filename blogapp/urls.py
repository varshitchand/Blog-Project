from django.urls import path, include
from .views import Index, DetailArticleView, LikeArticle, Featured, DeleteArticleView, CreateArticleView, UpdateArticleView

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
    path('featured/', Featured.as_view(), name='featured'),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article'),
    path('<int:pk>/update', UpdateArticleView.as_view(), name='update_article'),
    path('create/', CreateArticleView.as_view(), name='create_article'),  # New URL pattern for creating a new article
]
