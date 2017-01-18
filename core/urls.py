from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'core'
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^home/$', views.home, name="home"),
	url(r'^login/$', views.login_view, name="login_view"),
	url(r'^register/$', views.register, name="register"),
	url(r'^logout/$', views.logout_view, name="logout_view"),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
