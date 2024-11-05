import contextlib
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name = 'Accounts'
    
    def ready(self):
        with contextlib.suppress(ImportError):
           import accounts.signals