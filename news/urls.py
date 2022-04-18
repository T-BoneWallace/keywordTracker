from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name="index"),
    path('displaysimple', views.oneOrgOneKey, name='displaysimple'),
    path('sampledouble', views.sampleDouble),
    path('sampletriple', views.sampleMany),
    path('samplelist', views.samplelist),
    path('keywordadmin', views.admin, name='admin'),
    path('archive', views.archive, name='archive')
]