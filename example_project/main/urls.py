from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$',
            views.IndexView.as_view(),
            name='index'),

    re_path(r'^(?P<pk>[-\w]+)/$',
            views.PageDetailView.as_view(),
            name='page_detail'),
]
