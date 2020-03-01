import requests

from logging import getLogger
from .constants import bitbucket_host, github_host
from .exceptions import RemoteServiceError

logger = getLogger('user_profiles.external_requests')


def request_handler(host, route, method):
    # Only includes GETs for brevity
    try:
        if method == 'GET':
            response = requests.get(host + route)
        elif method == 'POST':
            pass
        else:
            raise NotImplementedError('HTTP Method not supported.')
    # Connection error to remote service
    except Exception as e:
        logger.warning('A connection error to host {} has occurred'.format(host))
        raise e

    if response.status_code != 200:
        raise RemoteServiceError(message=response.json(), status_code=response.status_code)

    return response.json()


def get_bitbucket_org_repos(org):
    route = '/2.0/repositories/{}'.format(org)
    response = request_handler(host=bitbucket_host, route=route, method='GET')
    return response['values']


def get_bitbucket_repo_watcher_count(org, repo):
    route = '/2.0/repositories/{}/{}/watchers'.format(org, repo)
    response = request_handler(host=bitbucket_host, route=route, method='GET')
    return response['size']


def get_github_org_repos(org):
    route = '/orgs/{}/repos'.format(org)
    return request_handler(host=github_host, route=route, method='GET')
