"""
SaaS Router customizations
"""
from rest_framework import routers

SAAS_URL_KW = "saas_url_kw"
_SAAS_URL_REGEX = "(?P<{}>.*)".format(SAAS_URL_KW)

LIST_ROUTE_ARGS = {
    'mapping': {'get': 'list', 'post': 'create'},
    'name': '{basename}-list',
    'initkwargs': {'suffix': 'List'}
}

DETAIL_ROUTE_ARGS = {
    'mapping': {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    },
    'name': '{basename}-detail',
    'initkwargs': {'suffix': 'Instance'}
}

METHOD_ROUTE_ARGS = {
    'mapping': {'{httpmethod}': '{methodname}'},
    'name': '{basename}-{methodnamehyphen}',
    'initkwargs': {}
}


class SimpleRouter(routers.SimpleRouter):
    """
    SimpleRouter for SaaS
    """
    routes = [
        # Default routes
        routers.Route(
            url=r'^{prefix}{trailing_slash}$',
            **LIST_ROUTE_ARGS
        ),
        routers.Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            **DETAIL_ROUTE_ARGS
        ),
        routers.Route(
            url=r'^{prefix}/{lookup}/{methodname}{trailing_slash}$',
            **METHOD_ROUTE_ARGS
        ),
        # Client specific routes...
        routers.Route(
            url=r'^{0}/{{prefix}}{{trailing_slash}}$'.format(_SAAS_URL_REGEX),
            **LIST_ROUTE_ARGS
        ),
        routers.Route(
            url=r'^{0}/{{prefix}}/{{lookup}}{{trailing_slash}}$'.format(_SAAS_URL_REGEX),
            **DETAIL_ROUTE_ARGS
        ),
        routers.Route(
            url=r'^{0}/{{prefix}}/{{lookup}}/{{methodname}}{{trailing_slash}}$'.format(_SAAS_URL_REGEX),
            **METHOD_ROUTE_ARGS
        )
    ]
