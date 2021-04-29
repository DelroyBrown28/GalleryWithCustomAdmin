from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    
    path('admin/', admin.site.urls),
    
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
    
    path('accounts/', include('allauth.urls')),
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('staff/', include('staff.urls', namespace='staff')),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
