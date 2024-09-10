from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    # Serve media and static files
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    
    # Admin and other URL patterns
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('home.urls', namespace='home')),
    path('', include('products.urls', namespace='products')),
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('orders.urls', namespace='orders')),
    path('', include('categories.urls', namespace='categories')),
    path('', include('suppliers.urls', namespace='suppliers')),
    path('', include('supplier_panel.urls', namespace='supplier_dashboard')),
    path('', include('newsletters.urls', namespace='newsletters')),
    path('', include('blog.urls', namespace='blog')),
    path('', include('contact.urls', namespace='contact')),
    path('', include('pages.urls', namespace='pages')),
    path('currencies/', include('currencies.urls')),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
