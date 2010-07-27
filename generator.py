# -*- coding: utf-8 -*-

import time
from datetime import datetime

import yaml
import github.github as github
import pystache

def repo_date_to_epoch ( date ):
	epoch = time.mktime(
		time.strptime(
			date[0:-6],
			"%Y-%m-%dT%H:%M:%S"
		)
	)
	return int( epoch )

def main ():

	print "Loading settings...."
	f = open( 'settings.yaml' )
	settings = yaml.load( f )
	f.close()

	gh = github.GitHub()

	print "Fetching user information..."
	user = gh.users.show( settings['username'] )

	print "Fetching repository information..."
	repos = gh.repos.forUser( settings['username'] )

	print "Sorting repositories..."
	repos = sorted( repos, cmp=lambda a, b: repo_date_to_epoch( b.pushed_at ) - repo_date_to_epoch( a.pushed_at ) )

	print "Loading template..."
	f = open( 'index.mustache' )
	template = f.read()
	f.close()

	print "Mangling template..."
	context = {
		'username': settings['username'],
		'fullname': user.name,
		'email': user.email,
		'following': str( user.following_count ),
		'followers': str( user.followers_count ),
		'publicrepos': str( user.public_repo_count ),
		'repos': [],
		'ga_code': settings['google_analytics']
	}

	for repo in repos:

		if repo.private:
			continue

		repo_context = {}
		repo_context['url'] = repo.url
		repo_context['name'] = repo.name
		repo_context['forks'] = repo.forks
		repo_context['watchers'] = repo.watchers
		repo_context['username'] = settings['username']
		repo_context['has_issues'] = repo.has_issues
		repo_context['has_wiki'] = repo.has_wiki
		repo_context['has_downloads'] = repo.has_downloads
		repo_context['last_push'] = datetime.fromtimestamp( repo_date_to_epoch( repo.pushed_at ) ).ctime()

		try:
			repo_context['homepage'] = repo.homepage
		except AttributeError:
			repo_context['homepage'] = False

		try:
			repo_context['description'] = repo.description
		except AttributeError:
			repo_context['description'] = False

		context['repos'].append( repo_context )

	template = pystache.render( template, context )

	print "Writing file..."
	f = open( 'index.html', 'w' )
	f.write( template )
	f.close()

	print "Done!"

if __name__ == "__main__":
	main()