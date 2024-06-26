
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 

from django.conf import settings
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name ='home'),
    path('blog/', include('blog.urls')), #goto urls.py file in blog folder
    
]

urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
