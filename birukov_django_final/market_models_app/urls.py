from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('all_products', views.all_products_page, name='all_products_page'),
    path('product/<int:product_id>', views.product_page, name='product_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)