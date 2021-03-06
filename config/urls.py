from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = i18n_patterns(
    path('accounts/', include('auth.urls')),
    path('products/', include('product.urls', namespace='products')),
    path('admin/', admin.site.urls),
    path('order/', include('order.urls', namespace='orders')),
    path('', include('pages.urls', namespace='pages')),
    path('Blog/', include('blog.urls', namespace='blogs')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('profile/', include('client.urls', namespace='profile'))
)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


