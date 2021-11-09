"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views as views_blog
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.conf import settings
from django.conf.urls.static import static
from funzioniiot import views  as views_app_iot
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'titoli2', views_app_iot.Titoli2View, 'todos')


sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('iot/',     include('funzioniiot.urls', namespace='funzioniiot')),
    path('utilitaazioni/', include('utilitaazioni.urls')),
    path('contattaci', views_app_iot.hellocontattaci),
    path('snippet/', include('snippets.urls')),
    path('api/', include(router.urls)),
    path('polls/', include('polls.urls')),

    # funzioni Iot
    path('httpResponse', views_app_iot.http_response), 
    path('chiamataRequestGet', views_app_iot.chiamata_request_get),  
    path('chiamataRequestPayload', views_app_iot.chiamata_request_payload),
    path('risposta_endpoint', views_app_iot.risposta_endpoint),   
    path('lanciaclasse', views_app_iot.lanciaclass),   
    path('websocketclient', views_app_iot.websocketclient), 
    path('mqttClient', views_app_iot.mqttclient), 
    path('djangoRestFramework', include('snippets.urls')),
    path('rpccallpi400', views_app_iot.rpgcallpi400),
    path('comandivocali', views_app_iot.comandivocali),
    path('redis_tutorial', views_app_iot.redis_tutorial),
    path('scrittura_ThingSpeak', views_app_iot.scrittura_ThingSpeak),
    path('scrittura_Aws_Iot_Mqtt_curl', views_app_iot.scrittura_Aws_Iot_Mqtt_curl),
    path('scrittura_Aws_Iot_Mqtt_python', views_app_iot.scrittura_Aws_Iot_Mqtt_python),
    #
    path('', views_blog.home, name='home'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    #
    path('emp', views_blog.emp),  
    path('show',views_blog.show),  
    path('edit/<int:id>', views_blog.edit),  
    path('update/<int:id>', views_blog.update),  
    path('delete/<int:id>', views_blog.destroy),  
    
    path('account/', include('account.urls')),
    
    path('drf', include('snippets.urls')),

    path('social-auth/',include('social_django.urls', namespace='social')),
    #url(r'^$', homepage, name='home'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)