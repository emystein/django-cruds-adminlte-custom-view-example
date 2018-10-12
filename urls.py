from django.conf.urls import url, include
from django.contrib import admin
from cruds_adminlte.urls import crud_for_app
from cruds.views import KnowledgeBaseView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Override default detail view for KnowledgeBase with the custom one.
    # Note that the override must be defined before all default CRUD URLs definition below.
    url('', include(KnowledgeBaseView().get_urls()))
]

# Default CRUD URLs definition
urlpatterns += crud_for_app('cruds', login_required=False, check_perms=False)
