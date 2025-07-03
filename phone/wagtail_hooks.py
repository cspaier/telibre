from wagtail import hooks

from .views import phone_viewset, application_viewset


@hooks.register("register_admin_viewset")
def register_phone_viewset():
    return phone_viewset

@hooks.register("register_admin_viewset")
def register_viewset():
    return application_viewset
