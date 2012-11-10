# -*- coding: utf-8 -*-

import yaml
from github import Github
import pystache


def main():

    print "Loading settings...."
    f = open('settings.yaml')
    settings = yaml.load(f)
    f.close()

    gh = Github()

    print "Fetching user information..."
    user = gh.get_user(settings['username'])

    print "Fetching repository information..."
    repos = user.get_repos(settings['username'])

    print "Sorting repositories..."
    repos = sorted(repos, reverse=True, key=lambda a: a.pushed_at)

    # We don't want to bother if the only thing updated was this repo.
    if repos[0].name == settings['reponame']:
        print "No new commits!"
        exit()

    print "Loading template..."
    f = open('index.mustache')
    template = f.read()
    f.close()

    print "Mangling template..."
    context = {
        'username': settings['username'],
        'fullname': user.name,
        'email': user.email,
        'following': str(user.following),
        'followers': str(user.followers),
        'publicrepos': str(user.public_repos),
        'repos': [],
        'ga_code': settings['google_analytics']
    }

    for repo in repos:

        if repo.private:
            continue

        repo_context = {}
        repo_context['url'] = repo.html_url
        repo_context['name'] = repo.name
        repo_context['forks'] = repo.forks
        repo_context['watchers'] = repo.watchers
        repo_context['username'] = settings['username']
        repo_context['has_issues'] = repo.has_issues
        repo_context['has_wiki'] = repo.has_wiki
        repo_context['has_downloads'] = repo.has_downloads
        repo_context['last_push'] = repo.pushed_at.ctime()

        try:
            repo_context['homepage'] = repo.homepage
        except AttributeError:
            repo_context['homepage'] = False

        try:
            repo_context['description'] = repo.description
        except AttributeError:
            repo_context['description'] = False

        context['repos'].append(repo_context)

    template = pystache.render(template, context)

    print "Writing file..."
    f = open('index.html', 'w')
    f.write(template)
    f.close()

    print "Done!"

if __name__ == "__main__":
    main()
