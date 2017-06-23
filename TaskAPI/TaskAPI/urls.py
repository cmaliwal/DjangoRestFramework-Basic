from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from TaskApp import views

#router = routers.DefaultRouter()
router = routers.SimpleRouter()

router.register(r'task', views.TaskViewSet)
router.register(r'due_task', views.DueTaskViewSet)
router.register(r'completed_task', views.CompletedTaskViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'TaskAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
