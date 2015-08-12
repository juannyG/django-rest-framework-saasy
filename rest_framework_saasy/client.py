"""SaaS Client Mixin"""

from .utils import classproperty

__all__ = ['ClientMixin']


class ClientMixin(object):
    """
    To be mixed with the relevant model associated with a "customer" of
    your platform/service(s) - the settings value of:
    REST_SETTINGS = {
        ...
        "SAAS": {
            "MODEL": "app.client.Model",
            "LOOKUP_FIELD": "fieldname"
        }
        ...
    }

    The ClientMixin class dictates the implementation rules. There
    is no functionality defined here.
    """
    def saas_client_module(self, saas_url_kw, *args, **kwargs):
        """Define module path to client customization"""
        raise NotImplementedError
