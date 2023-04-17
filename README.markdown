# What is it?

This repository is both my personal GitHub page, as well as the generator code
that I use to make it.

# How do I use it?

Clone/fork this repo, then copy settings.yaml.tpl to settings.yaml. Edit to match
your needs, then run generator.py

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
Collecting cffi==1.15.1
  Using cached cffi-1.15.1-cp311-cp311-macosx_11_0_arm64.whl (174 kB)
Collecting charset-normalizer==3.1.0
  Using cached charset_normalizer-3.1.0-cp311-cp311-macosx_11_0_arm64.whl (121 kB)
Collecting cryptography==40.0.2
  Using cached cryptography-40.0.2-cp36-abi3-macosx_10_12_universal2.whl (5.1 MB)
Collecting Deprecated==1.2.13
  Using cached Deprecated-1.2.13-py2.py3-none-any.whl (9.6 kB)
Collecting idna==3.4
  Using cached idna-3.4-py3-none-any.whl (61 kB)
Collecting pycparser==2.21
  Using cached pycparser-2.21-py2.py3-none-any.whl (118 kB)
Collecting PyGithub==1.58.1
  Using cached PyGithub-1.58.1-py3-none-any.whl (312 kB)
Collecting PyJWT==2.6.0
  Using cached PyJWT-2.6.0-py3-none-any.whl (20 kB)
Collecting PyNaCl==1.5.0
  Using cached PyNaCl-1.5.0-cp36-abi3-macosx_10_10_universal2.whl (349 kB)
Collecting pystache==0.6.0
  Using cached pystache-0.6.0-py3-none-any.whl
Collecting requests==2.28.2
  Using cached requests-2.28.2-py3-none-any.whl (62 kB)
Collecting urllib3==1.26.15
  Using cached urllib3-1.26.15-py2.py3-none-any.whl (140 kB)
Collecting wrapt==1.15.0
  Using cached wrapt-1.15.0-cp311-cp311-macosx_11_0_arm64.whl (36 kB)
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
