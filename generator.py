# -*- coding: utf-8 -*-

import github.github as github
import yaml

print "Loading settings...."
f = open( 'settings.yaml' )
settings = yaml.load( f )
f.close()

gh = github.GitHub()
print "Fetching user information..."
user = gh.users.show( settings['username'] )
print "Fetching repository information..."
repos = gh.repos.forUser( settings['username'] )

print "Loading template..."
f = open( 'index.html.tpl' )
template = f.read()
f.close()

print "Mangling template..."
template = template.replace( '<% username %>', settings['username'] )
template = template.replace( '<% fullname %>', user.name )
template = template.replace( '<% email %>', user.email )
template = template.replace( '<% following %>', str( user.following_count ) )
template = template.replace( '<% followers %>', str( user.followers_count ) )
template = template.replace( '<% publicrepos %>', str( user.public_repo_count ) )

repo_string = ''

for repo in repos:
	if repo.private:
		continue

	repo_string = repo_string + '<div class="repo"><h3><a href="' + repo.url + '">' + repo.name + '</a>'
	
	try:
		repo_string = repo_string + ' - <span class="small"><a href="' + repo.homepage + '">' + repo.homepage + '</a></span>'
	except AttributeError:
		pass
	
	repo_string = repo_string + '</h3>'
	
	repo_string = repo_string + "Forks: " + str( repo.forks ) + " - Watchers: " + str( repo.watchers ) + ' | '
	
	if repo.has_issues:
		repo_string = repo_string + ' <a href="' + repo.url + '/issues">Issues</a> |'
	
	if repo.has_wiki:
		repo_string = repo_string + ' <a href="http://wiki.github.com/' + settings['username'] + '/' + repo.name + '">Wiki</a> |'
	
	if repo.has_downloads:
		repo_string = repo_string + ' <a href="' + repo.url + '/downloads">Downloads</a> |'
	
	
	try:
		repo_string = repo_string + '<pre>' + repo.description + '</pre>'
	except AttributeError:
		repo_string = repo_string + '<br/><br/>'
		pass
		
	repo_string = repo_string + "</div><!--// .repo //-->\n"

template = template.replace( '<% repos %>', repo_string )

ga = """
<script type="text/javascript">
	var _gaq = _gaq || [];
	_gaq.push(['_setAccount', '<% ga_code %>']);
	_gaq.push(['_trackPageview']);
	(function() {
		var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
		ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
		var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
	})();
</script>
"""

if False != settings['google_analytics']:
	template = template.replace( '<% google_analytics %>', ga )
	template = template.replace( '<% ga_code %>', settings['google_analytics'] )
else:
	template = template.replace( '<% google_analytics %>', '' )

print "Writing file..."
f = open( 'index.html', 'w' )
f.write( template )
f.close()

print "Done!"