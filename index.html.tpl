<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<title><% username %> @ GitHub</title>
		<style type="text/css">
			body {
				margin-top: 1.0em;
				background-color: #ffffff;
				font-family: "Helvetica,Arial,FreeSans";
				color: #000000;
			}
			#container {
				margin: 0 auto;
				width: 700px;
			}
			h1 { font-size: 3.8em; color: #000000; margin-bottom: 3px; }
			h1 .small { font-size: 0.4em; color: #444; }
			h1 a { text-decoration: none }
			h2 { font-size: 1.5em; color: #000000; }
			h3 { color: #000000; }
			h3 .small { font-size: 0.2em; font-weight: normal; }
			a { color: #000000; }
			.description { font-size: 1.2em; margin-bottom: 30px; margin-top: 30px; font-style: italic;}
			.download { float: right; }
			pre { background: #000; color: #fff; padding: 15px;}
			hr { border: 0; width: 80%; border-bottom: 1px solid #aaa}
			.footer { text-align:center; padding-top:30px; font-style: italic; }
			.repo { padding: 0 10px; border: 1px solid #777; margin: 5px 0; }
		</style>
	</head>
	<body>
		<a href="http://github.com/<% username %>"><img style="position: absolute; top: 0; right: 0; border: 0;" src="http://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png" alt="Fork me on GitHub" /></a>
		<div id="container">
			<h1>
				<a href="http://github.com/<% username %>"><% username %></a>
				<span class="small">is <% fullname %></span>
			</h1>

			<div class="description">
				Following: <% following %> - Followers: <% followers %> - Public Repositories: <% publicrepos %>
			</div>
			
			<h2>Public Repositories</h2>
			
			<% repos %>
			
			<div class="footer">
				contact via <% email %> or on <a href="http://github.com/<% username %>">GitHub</a>
			</div>

		</div><!--// #container //-->
		
		<% google_analytics %>
	</body>
</html>