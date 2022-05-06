
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register_page,name='register'),
    path('add_cart/<pizza_uid>/',views.add_card,name='addcart'),
    path('cart/',views.cart,name='cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
