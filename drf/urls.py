from .views import *
from django.urls import path

urlpatterns = [
    
# path('',index),
# path('article/',article_list),
path('article/',ArticleAPI.as_view()),
# path('detail/<int:pk>/',article_detail),
path('detail/<int:id>/',ArticleDetails.as_view()),
]
