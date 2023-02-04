from django.urls import include, re_path
from django.contrib import admin
from django.contrib.auth import login
from django.contrib.auth.views import logout_then_login
from django.contrib.auth import views as auth_views
import binder.views
admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),

    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^accounts/logout/$', logout_then_login, name='logout'),

    re_path(r'^$', binder.views.home_index, name="index"),
    re_path(r'^server_list/$', binder.views.view_server_list, name="server_list"),

    re_path(r'^info/(?P<dns_server>[a-zA-Z0-9.-]+)/$', binder.views.view_server_zones, name="server_zone_list"),
    re_path(r'^info/(?P<dns_server>[a-zA-Z0-9.-]+)/(?P<zone_name>[a-zA-Z0-9.-]+)/$', binder.views.view_zone_records, name="zone_list"),

    re_path(r'^add_record/(?P<dns_server>[a-zA-Z0-9.-]+)/(?P<zone_name>[a-zA-Z0-9.-]+)/$', binder.views.view_add_record, name="add_record"),
    re_path(r'^add_cname/(?P<dns_server>[a-zA-Z0-9.-]+)/(?P<zone_name>[a-zA-Z0-9.-]+)/(?P<record_name>.*?)/$', binder.views.view_add_cname_record, name="add_cname"),
    re_path(r'^delete_record/(?P<dns_server>[a-zA-Z0-9.-]+)/(?P<zone_name>[a-zA-Z0-9.-]+)/$', binder.views.view_delete_record, name="delete_record"),
    re_path(r'^edit_record/(?P<dns_server>[a-zA-Z0-9.-]+)/(?P<zone_name>[a-zA-Z0-9.-]+)/(?P<record_name>[\S+]+)/(?P<record_data>[\S+]+)/(?P<record_ttl>[\S+]+)/$', binder.views.view_edit_record, name="edit_record"),
]
