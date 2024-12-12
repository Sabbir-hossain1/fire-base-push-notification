from django.urls import path
from fcm.views.AdminSDKBased.sdkBased import send_fcm_message

urlpatterns = [
    path(
        "send-notification-using-sdk/",
        send_fcm_message,
        name="send-notification-using-sdk",
    )
]
