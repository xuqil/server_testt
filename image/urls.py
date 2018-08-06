from django.conf.urls import url
from image import views


app_name = 'image'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.PosetDetailView.as_view(),name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^search/$', views.search, name='search'),



    #其他网页url
    url(r'^about/$', views.about,name='about'),
    url(r'^codes/$', views.about, name='codes'),
    url(r'^contact/$', views.about, name='contact'),
    url(r'^muisc/$', views.about, name='muisc'),
    url(r'^features/$', views.about, name='features'),
    url(r'^fashion/$', views.about, name='fashion'),
    url(r'^singlepage/$', views.about,name='singlepage'),


]