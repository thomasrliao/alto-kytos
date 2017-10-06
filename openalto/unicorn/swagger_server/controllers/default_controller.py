import connexion
from swagger_server.models.error import Error
from swagger_server.models.path_query_request import PathQueryRequest
from swagger_server.models.path_query_response import PathQueryResponse
from swagger_server.models.resource_query_request import ResourceQueryRequest
from swagger_server.models.resource_query_response import ResourceQueryResponse
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def ext_query_path_post(queries):
    """
    ext_query_path_post
    Make a recursive path query
    :param queries: 
    :type queries: dict | bytes

    :rtype: PathQueryResponse
    """
    if connexion.request.is_json:
        queries = PathQueryRequest.from_dict(connexion.request.get_json())
    return 'do some magic!'


def ext_query_resource_post(flows):
    """
    ext_query_resource_post
    Returns resource state abstraction in simple mode
    :param flows: 
    :type flows: dict | bytes

    :rtype: ResourceQueryResponse
    """
    if connexion.request.is_json:
        flows = ResourceQueryRequest.from_dict(connexion.request.get_json())
    return 'do some magic!'
