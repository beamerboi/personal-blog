from django.contrib import admin
from django.urls import path
import blog.views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/<slug:id_blog>/', blog.views.blog_detail, name="blogDetail"),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

