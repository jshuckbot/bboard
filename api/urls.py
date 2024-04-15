from django.urls import path

from api.views import BbDetailView, bbs, comments

urlpatterns = [
    path("bbs/<int:pk>/comments/", comments),
    path("bbs/<int:pk>/", BbDetailView.as_view()),
    path("bbs/", bbs),
]
