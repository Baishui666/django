from django.conf.urls import url
import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^user_exists/$', views.user_exists),
    url(r'^login/$', views.login),
    url(r'^login_handel/$', views.login_handel),
    url(r'^logout/$', views.logout),
    url(r'^info/$', views.info),
    url(r'^order/$', views.order),
    url(r'^site/$', views.site),

]

