# What is it?

This repository is both my personal GitHub page, as well as the generator code
that I use to make it.

# How do I use it?

Clone/fork this repo, set environment variables, then run generator.py

# What environment variables do I need to set?

 - `GITHUB_REPOSITORY_OWNER` - The owner of the repository you want to generate the page for. (i.e. `jmhobbs`)
 - `GITHUB_REPOSITORY` - The repository this GitHub pages is in. (i.e. `jmhobbs/jmhobbs.github.com`)
 - `WEBSITE` - Optional, the URL of your personal website. (not your GitHub pages)

# What do I need to use it?

 - [Python 3](http://www.python.org/)
 - [py-github](http://github.com/dustin/py-github)
 - [pystache](http://github.com/defunkt/pystache)

## Installing

```
$ python -m venv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
Collecting certifi==2022.12.7
  Using cached certifi-2022.12.7-py3-none-any.whl (155 kB)
...
Installing collected packages: wrapt, urllib3, pystache, PyJWT, pycparser, idna, charset-normalizer, certifi, requests, Deprecated, cffi, PyNaCl, cryptography, PyGithub
Successfully installed Deprecated-1.2.13 PyGithub-1.58.1 PyJWT-2.6.0 PyNaCl-1.5.0 certifi-2022.12.7 cffi-1.15.1 charset-normalizer-3.1.0 cryptography-40.0.2 idna-3.4 pycparser-2.21 pystache-0.6.0 requests-2.28.2 urllib3-1.26.15 wrapt-1.15.0

[notice] A new release of pip available: 22.3.1 -> 23.1
[notice] To update, run: pip install --upgrade pip
(env) $ GITHUB_REPOSITORY_OWNER="jmhobbs" GITHUB_REPOSITORY="jmhobbs/jmhobbs.github.com"  python generator.py
Loading settings....
Fetching user information...
Fetching repository information...
Sorting repositories...
Loading template...
Mangling template...
Writing file...
Done!
```

# What does the output look like?

Without any changes, it will look like this: [http://jmhobbs.github.io/](http://jmhobbs.github.io/)
