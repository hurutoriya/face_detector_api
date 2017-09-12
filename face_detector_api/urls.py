from django.conf.urls import include, url
from django.contrib import admin
from face_detector.views import detect

urlpatterns = [
    url(r'^face_detection/detect/$', detect),
    # url(r'^$', 'cv_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]