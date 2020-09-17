from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogger/<int:pk>', views.BlogListbyAuthorView.as_view(), name='blogs-by-author'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blog/<int:pk>/comment/', views.BlogCommentCreate.as_view(), name='blog_comment'),
    url(r'^blog/create/$', views.BlogCreate.as_view(), name='blog_create'),
    url(r'^blog/(?P<pk>\d+)/update/$', views.BlogUpdate.as_view(), name='blog_update'),
    url(r'^blog/(?P<pk>\d+)/delete/$', views.BlogDelete.as_view(), name='blog_delete'),
]