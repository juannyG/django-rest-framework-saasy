"""
SaaS Router customizations
"""
from rest_framework import routers
from rest_framework_saasy.settings import CLIENT_MODEL

CLIENT_URL_PARAM = CLIENT_MODEL._meta.saas_url_param if CLIENT_MODEL else None
CLIENT_URL_REGEX = '(?P<{}>.*)'.format(CLIENT_URL_PARAM) \
    if CLIENT_URL_PARAM else None

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
            url=r'^{0}/{{prefix}}{{trailing_slash}}$'.format(CLIENT_URL_REGEX),
            **LIST_ROUTE_ARGS
        ),
        routers.Route(
            url=r'^{0}/{{prefix}}/{{lookup}}{{trailing_slash}}$'.format(CLIENT_URL_REGEX),
            **DETAIL_ROUTE_ARGS
        ),
        routers.Route(
            url=r'^{0}/{{prefix}}/{{lookup}}/{{methodname}}{{trailing_slash}}$'.format(CLIENT_URL_REGEX),
            **METHOD_ROUTE_ARGS
        )
    ]
