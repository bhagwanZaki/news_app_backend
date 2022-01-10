from django.conf.urls import url
from .views import *
from django.urls import path
from rest_framework import routers

router  = routers.DefaultRouter()
router.register("adminNews",newsAdminApi,"adminNews")

urlpatterns = [
    path("news",newsApi.as_view()),
    path("latestnews",latestNewsApi.as_view())
]

urlpatterns += router.urls
