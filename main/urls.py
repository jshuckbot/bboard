from django.urls import path

from main.views import BBLoginView, index, other_page, profile

app_name = "main"
urlpatterns = [
    path("accounts/login/", BBLoginView.as_view(), name="login"),
    path("accounts/profile/", profile, name="profile"),
    path("<str:page>/", other_page, name="other"),
    path("", index, name="index"),
]
