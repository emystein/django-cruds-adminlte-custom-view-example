from django.conf.urls import url, include
from django.contrib import admin
from cruds_adminlte.urls import crud_for_app
from cruds.views import KnowledgeBaseView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include(KnowledgeBaseView().get_urls()))
]

urlpatterns += crud_for_app('cruds', login_required=False, check_perms=False)
