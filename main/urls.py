from django.urls import path

from main.views import (
    BBLoginView,
    BBLogoutView,
    PasswordEditView,
    ProfileEditView,
    RegisterDoneView,
    RegisterView,
    index,
    other_page,
    profile,
    user_activate,
)

app_name = "main"
urlpatterns = [
    path("accounts/activate/<str:sign>", user_activate, name="activate"),
    path("accounts/login/", BBLoginView.as_view(), name="login"),
    path("accounts/profile/", profile, name="profile"),
    path("accounts/logout/", BBLogoutView.as_view(), name="logout"),
    path("accounts/profile/edit/", ProfileEditView.as_view(), name="profile_edit"),
    path("accounts/password/edit/", PasswordEditView.as_view(), name="password_edit"),
    path("accounts/register/done/", RegisterDoneView.as_view(), name="register_done"),
    path("accounts/register/", RegisterView.as_view(), name="register"),
    path("<str:page>/", other_page, name="other"),
    path("", index, name="index"),
]
