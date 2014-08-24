"""SaaS Client Mixin"""


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

    def saas_lookup_field(self, *args, **kwargs):
        """Define the model lookup field to use when querying the database
        for the client record"""
        raise NotImplementedError

    def saas_client_module(self, saas_url_kw, *args, **kwargs):
        """Define module path to client customization"""
        raise NotImplementedError
