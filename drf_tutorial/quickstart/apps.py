from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QuickstartConfig(AppConfig):
    name = 'drf_tutorial.quickstart'
    verbose_name = _("Quickstart")

    def ready(self):
        try:
            import drf_tutorial.quickstart.signals  # noqa F401
        except ImportError:
            pass
