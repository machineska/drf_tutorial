from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


class SnippetsConfig(AppConfig):
    name = 'drf_tutorial.snippets'
    verbose_name = _("Snippets")

    def ready(self):
        try:
            import drf_tutorial.snippets.signals  # noqa F401
        except ImportError:
            pass
