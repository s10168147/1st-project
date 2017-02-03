from django.conf.urls import url

from blog import views

urlpatterns= [
    url(r'^article/(\d+)/', views.viewArticle, name ='article'),
    url(r'^$', views.post_list),
]
