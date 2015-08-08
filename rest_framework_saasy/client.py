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
            "MODEL": "app.client.Model"
        }
        ...
    }

    The ClientMixin class dictates the implementation rules. There
    is no functionality defined here.
    """
    @classproperty
    @classmethod
    def saas_lookup_field(cls):
        """Define the model lookup field to use when querying the database
        for the client record"""
        raise NotImplementedError

    def saas_client_module(self, saas_url_kw, *args, **kwargs):
        """Define module path to client customization"""
        raise NotImplementedError
