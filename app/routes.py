import logging
import flask
import json

from flask import Response
from .external_requests import get_bitbucket_org_repos, get_github_org_repos, get_bitbucket_repo_watcher_count
from app import app

logger = flask.logging.create_logger(app)
logger.setLevel(logging.INFO)


@app.route("/health-check", methods=["GET"])
def health_check():
    """
    Endpoint to health check API
    """
    app.logger.info("Health Check!")
    return Response("All Good!", status=200)


@app.route("/merge/<organization>", methods=["GET"])
def merge_accounts(organization):
    """
    Endpoint to merge bitbucket/github organization
    """
    repos = []
    repos.extend(get_github_org_repos(org=organization))
    repos.extend(get_bitbucket_org_repos(org=organization))

    # Initialize response data
    forked_repos = 0
    original_repos = 0
    watcher_count = 0
    repo_topics = []
    languages = []

    # Populate relevant data
    for repo in repos:
        # Determine whether or not the repo is a fork
        try:
            # Github dicts contain a 'fork' bool if it's a fork
            if repo['fork']:
                forked_repos += 1
            # Bitbucket dicts contain a 'parent' key but will only be present if it is a fork
            elif repo['parent']:
                forked_repos += 1
        except KeyError:
            original_repos += 1

        # Get watcher/follower count
        # Github repo responses contain watcher data, bitbucket repos don't so we need to dig further
        try:
            watcher_count += repo['watchers']
        except KeyError:
            watcher_count += get_bitbucket_repo_watcher_count(org=organization, repo=repo['name'])

        # Get language
        if repo['language'] is not None and repo['language'].lower() not in languages:
            languages.append(repo['language'].lower())

        # Add repo topic
        repo_topics.append(repo['name'])

    response = {
        'Forked Repos': forked_repos,
        'Original Repos': original_repos,
        'Total Watchers': watcher_count,
        'Repos': {
            'Topics': repo_topics,
            'Count': len(repo_topics)
        },
        'Languages': {
            'Types': languages,
            'Count': len(languages)
        },
    }

    return Response(json.dumps(response), status=200, mimetype='application/json')
