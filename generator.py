# -*- coding: utf-8 -*-

from github import Github
import pystache
import os

def main():
    print("Loading settings....")
    settings = {
            'username': os.environ['GITHUB_REPOSITORY_OWNER'],
            'reponame': os.environ['GITHUB_REPOSITORY'].split('/')[-1],
            }

    gh = Github()

    print("Fetching user information...")
    user = gh.get_user(settings['username'])

    print("Fetching repository information...")
    repos = user.get_repos(settings['username'])

    print("Sorting repositories...")
    repos = sorted(repos, reverse=True, key=lambda a: a.pushed_at)

    # We don't want to bother if the only thing updated was this repo.
    if repos[0].name == settings['reponame']:
        print("No new commits!")
        exit()

    # Same for GitHub README page
    if repos[0].name == settings['username']:
        print("No new commits!")
        exit()

    print("Loading template...")
    f = open('index.mustache')
    template = f.read()
    f.close()

    print("Mangling template...")
    context = {
            'username': settings['username'],
            'fullname': user.name,
            'email': user.email,
            'following': str(user.following),
            'followers': str(user.followers),
            'publicrepos': str(user.public_repos),
            'repos': []
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

    print("Writing file...")
    f = open('index.html', 'wb')
    f.write(template.encode('utf8'))
    f.close()

    print("Done!")

if __name__ == "__main__":
    main()
