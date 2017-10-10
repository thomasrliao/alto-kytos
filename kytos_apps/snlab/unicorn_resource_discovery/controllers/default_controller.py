import connexion
from napps.snlab.unicorn_resource_discovery.models.error_response import ErrorResponse
from napps.snlab.unicorn_resource_discovery.models.path_query_response import PathQueryResponse
from napps.snlab.unicorn_resource_discovery.models.query_requests import QueryRequests
from napps.snlab.unicorn_resource_discovery.models.resource_query_response import ResourceQueryResponse
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from kytos.core import log

def query_path_post(query_set):
    """
    query_path_post
    query the ingress point of the next domain
    :param query_set: a set of path queries
    :type query_set: dict | bytes

    :rtype: PathQueryResponse
    """
    if connexion.request.is_json:
        query_set = QueryRequests.from_dict(connexion.request.get_json())
    log.info(query_set)
    return connexion.request.get_json()
    #return 'do some magic!'


def query_resource_post(query_set):
    """
    query_resource_post
    query the resource availability of the current domain for a given set of flows
    :param query_set: a set of resource queries
    :type query_set: dict | bytes

    :rtype: ResourceQueryResponse
    """
    if connexion.request.is_json:
        query_set = QueryRequests.from_dict(connexion.request.get_json())
    return 'do some magic!'
