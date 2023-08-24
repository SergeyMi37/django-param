from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from appmsw import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='home'),
    path('params/add', views.add_param_page, name='param-add'),
    path('params/list', views.params_page, name='param-list'),
    path('params/my', views.params_page,{'my':True}, name='param-my'),
    path('param/<int:param_id>/', views.param_detail, name='param-detail'),
    path('param/<int:param_id>/delete', views.param_delete, name='param-delete'),
    path('comment/add', views.comment_add, name="comment_add"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.registration, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
