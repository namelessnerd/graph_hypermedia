from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'mdh.views.home', name='home'),
                       url(r'^get/products$', 'mdh.views.get_products',
                           name='home'),
                       url(r'^get/capabilities$', 'mdh.views.get_capabilities',
                           name='home'),
                       url(r'^get/capabilities/network$',
                           'mdh.views.get_network',
                           name='home'),
                       )
