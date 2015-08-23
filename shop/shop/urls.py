from django.conf.urls import include, url
from django.contrib import admin
from .views import HomeView


urlpatterns = [
    # Examples:
    # url(r'^$', 'shop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),
]

# REST API
from rest_framework import routers
from .api import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns += [
    # REST documentation
    url(r'^api/docs/', include('rest_framework_swagger.urls')),

    # REST urls
    url(r'^api/', include(router.urls)),
]

# Media and Static files for development
from django.conf import settings
if settings.DEBUG:
    # Static files
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

    # Media files
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
