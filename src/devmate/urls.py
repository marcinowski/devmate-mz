from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.i18n import set_language

from mezzanine.conf import settings


admin.autodiscover()

urlpatterns = i18n_patterns(
    url("^admin/", include(admin.site.urls)),  # fixme: can be changed for another endpoint for security
)

if settings.USE_MODELTRANSLATION:
    urlpatterns += [
        url('^i18n/$', set_language, name='set_language'),
    ]

urlpatterns += i18n_patterns(
    url("^$", TemplateView.as_view(template_name="index.html"), name="home"),
    url("^o-mnie/$", TemplateView.as_view(template_name="index.html"), name="about"),
    url("^projekty/$", TemplateView.as_view(template_name="index.html"), name="projects"),
    url("^ref/$", TemplateView.as_view(template_name="main.html"), name="ref"),
    url("^", include("mezzanine.urls")),
)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
