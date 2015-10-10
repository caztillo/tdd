from django.conf.urls import url, patterns

from lists import views

urlpatterns = patterns('',
                       url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),
                       url(r'^(\d+)/add_item$', 'lists.views.add_item', name='add_item'),
                       url(r'^new$', 'lists.views.new_list', name='new_list'),
                       )