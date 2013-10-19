from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'experiment_report_online.views.home', name='home'),
    # url(r'^experiment_report_online/', include('experiment_report_online.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'logins.views.index'),
	url(r'^login/$', 'logins.views.user_login'),
)
