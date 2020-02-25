# Package Management in Python (PIP)
* You can install, upgrade, and remove packages using a program called pip. 
* By default pip will install packages from the Python Package Index, [https://pypi.org](https://pypi.org)
* Similar to linux repository(YUM, APT), NPM for Node.js, etc
* Python actually has another, more primitive, package manager called `easy_install`, which is installed automatically when you install Python itself. 
* `pip` is vastly superior to easy_install for lots of reasons, and so should generally be used instead.

## The Basics

### Search Packages
* You can browse the Python Package Index by going to it in your web browser, or you can use pip’s limited search feature:


```python
pip search django
```

    django-bagou (0.1.0)              - Django Websocket for Django
    django-maro (0.0.2)               - `django-maro` is utility for django.
    django-ide (0.0.5)                - A Django app to develop Django apps
    django-hooked (0.2.6)             - WebHooks for Django and Django Rest Framework.
    django-six (1.0.4)                - Django-six &#8212;&#8212; Django Compatibility Library
    django-jackal (2.1.1)             - Boilerplate for Django and Django REST Framework
    django-umanage (1.1.1)            - Django user management app for django
    django-mailwhimp (0.1)            - django-mailwhimp integrates mailchimp into Django
    django-nadmin (0.1.0)             - django nadmin support django version 1.8 based on django-xadmin
    django-templatecomponents (0.03)  - django-templatecomponents
    django-cepfield (0.3.0)           - Django CepField
    django-apscheduler (0.3.0)        - APScheduler for Django
    django-pinba (1.3.0)              - django pinba
    django-crudviewset (0.1.2)        - Django CRUDViewSet
    django-listings (0.1)             - django-listings
    django-optionsfield (0.2)         - django-optionsfield
    django-user (0.2.1)               - Django User
    django-uuidfield (0.5.0)          - UUIDField in Django
    django-utils (0.0.2)              - Utilities for Django
    Django-Util (0.0.3)               - Django Utililies
    django-acserv (0.6.1)             - acserv for django
    django-pagination (1.0.7)         - django-pagination
    django-chess (0.2.1)              - Django Chess
    django-handlebars (0.1)           - Handlebars for Django
    django-funserver (1.0)            - FUNserver for Django
    django-concepts (0.7.2)           - django-concepts
    django-events (0.1)               - django-events
    django-vouchers (0.6)             - Vouchers in Django
    django-freebase (0.1dev)          - Freebasing in Django.
    django-collage (1.0.1)            - django collages
    django-stachoutils (3.1.2)        - Commons for Django
    django-intenumfield (1.4.0)       - An IntEnumField for Django
    django-djikiki (1.1)              - A django wiki
    django-wysiwyg (0.8.0)            - django-wysiwyg
    django-bitfield (1.9.6)           - BitField in Django
    django-userproperty (1.0.8)       - django userproperty
    django-plugins (0.3.0)            - django-plugins.
    django-formfield (0.4)            - django-formfield
    django-unixdatetimefield (1.2.0)  - UnixDateTimeField in Django
    django-microblogging (0.1.2)      - django-microblogging
    django-paginate (0.3.1)           - Django Paginate
    sense-django (0.2.20)             - sense django
    django-nextpage (1.0.2)           - django-nextpage
    django-mako (0.1.3)               - Django Mako
    django-coffee (0.0.4)             - Django Coffee
    django-pipstatus (0.1.3)          - Django pipstatus
    django-more (0.2.6)               - Django with more
    django-icons (1.1.1)              - Icons for Django
    django-extensions (2.2.6)         - Extensions for Django
    django-subcommands (2019.4.13)    - Django subcommands
    django-restframework (0.0.1)      - django-restframework
    django-mailformer (0.0.1)         - Django Mailformer
    django-alerts (0.5.1)             - Django alerts
    diy-django (1.3.1)                - diy-django
    django-datahooks (0.0.1)          - Django datahooks
    django-shares (0.0.1)             - Sharing for django
    django-thumbnail (11.13)          - Thumbnailing in Django
    django-stopwatch (0.2)            - Django Stopwatch
    django-moat (0.1.1)               - django-moat
    django-masquerade (1.3)           - django-masquerade
    django-projectname (1.0.0)        - django projectname
    django-narrative (0.5.9)          - Django narrative
    django-jsonschema2 (0.2.1)        - Django JSONSchema
    django-docviewer (0.4)            - documentcloud for django
    django-profiling (0.1)            - Django Profiling
    django-humans (0.1)               - Django Humans
    django-keychain (0.0.1)           - Django Keychain
    django-purls (0.3)                - django-purls
    django-edumetadata (0.7)          - django-edumetadata
    django-sendgrid (1.0.1)           - django-sendgrid
    django-pagebase (0.4.1)           - Pages for Django
    django-mesh (0.1.0)               - A Django blog.
    django-glitter (0.2.10)           - Glitter for Django
    django-tcms (0.1.11)              - Django tCMS.
    django-mariposa (0.1)             - django-mariposa
    django-esutils (0.3)              - Django Esutils.
    django-alive (1.1.0)              - Healtchecks for Django
    django-alipay2 (0.13.3)           - alipay for django
    django-flow (1.0.3)               - Django flow
    django-paypal2 (1.0.2)            - paypal for django
    django-progress (1.0.4)           - Django Progress
    django-polyfield (0.1.0)          - Django Polyfield
    django-poll (0.3.1)               - Django Poll
    django-sekizai (1.0.0)            - Django Sekizai
    django-localcrawler (0.1.1)       - django-localcrawler
    django-sections (0.1)             - django-sections
    django-groot (0.1.1)              - Django Groot
    django-sendcloud2 (0.2.1)         - sendcloud2 for django
    django-sape (0.2.4)               - Django + sape.ru.
    django-micro (1.8.0)              - Django as a microframework
    django-callback (0.6.1)           - Django Callback
    django-sae (0.2.1)                - for django in sae
    django-uri (1.0.5)                - Django URI
    django-requestlogs (0.2.0)        - Audit logging for Django and Django Rest Framework
    django-brevisurl (2.0.3)          - django-brevisurl is django app for shortening urls
    django-pybrowscap (1.0.0)         - django-pybrowscap is django middleware with support for pybrowscap
    django-eth (0.2.6)                - Ethereum utilities for Django and Django Rest projects
    django-scrapyd (0.2)              - Django scrapyd is a Django app to manage scrapyd
    django-perm (2.5.0)               - Class based Django permissions for Django models.
    django-postit (0.3)               - django-postit is a scrumboard application for django projects
    Note: you may need to restart the kernel to use updated packages.


### Install Packages
* Install the latest version of a package by specifying a package’s name:


```python
pip install requests
```

    Requirement already satisfied: requests in d:\applications\winpython-3.8\python-3.8.1.amd64\lib\site-packages (2.22.0)
    Requirement already satisfied: urllib3 in d:\applications\winpython-3.8\python-3.8.1.amd64\lib\site-packages (from requests) (1.25.7)
    Requirement already satisfied: idna in d:\applications\winpython-3.8\python-3.8.1.amd64\lib\site-packages (from requests) (2.8)
    Requirement already satisfied: chardet in d:\applications\winpython-3.8\python-3.8.1.amd64\lib\site-packages (from requests) (3.0.4)
    Requirement already satisfied: certifi in d:\applications\winpython-3.8\python-3.8.1.amd64\lib\site-packages (from requests) (2019.11.28)
    Note: you may need to restart the kernel to use updated packages.


#### Specify version


```python
pip install requests==2.6.0
```

    Collecting requests==2.6.0
      Using cached https://files.pythonhosted.org/packages/73/63/b0729be549494a3e31316437053bc4e0a8bb71a07a6ee6059434b8f1cd5f/requests-2.6.0-py2.py3-none-any.whl
    Installing collected packages: requests
      Found existing installation: requests 2.22.0
        Uninstalling requests-2.22.0:
          Successfully uninstalled requests-2.22.0
    Successfully installed requests-2.6.0
    Note: you may need to restart the kernel to use updated packages.


    ERROR: twine 3.1.1 has requirement requests>=2.20, but you'll have requests 2.6.0 which is incompatible.
    ERROR: moviepy 1.0.1 has requirement requests<3.0,>=2.8.1, but you'll have requests 2.6.0 which is incompatible.


### Upgrade Packages
* You can run `pip install --upgrade` to upgrade the package to the latest version:


```python
pip install --upgrade requests
```

    Collecting requests
      Using cached https://files.pythonhosted.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl
    Requirement already satisfied, skipping upgrade: certifi>=2017.4.17 in d:\applications\winpython-3.8\python-3.8.1.amd64\lib\site-packages (from requests) (2019.11.28)
    Requirement already satisfied, skipping upgrade: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in d:\applications\winpython-3.8\python-3.8.1.amd64\lib\site-packages (from requests) (1.25.7)
    Requirement already satisfied, skipping upgrade: chardet<3.1.0,>=3.0.2 in d:\applications\winpython-3.8\python-3.8.1.amd64\lib\site-packages (from requests) (3.0.4)
    Requirement already satisfied, skipping upgrade: idna<2.9,>=2.5 in d:\applications\winpython-3.8\python-3.8.1.amd64\lib\site-packages (from requests) (2.8)
    Installing collected packages: requests
      Found existing installation: requests 2.6.0
        Uninstalling requests-2.6.0:
          Successfully uninstalled requests-2.6.0
    Successfully installed requests-2.22.0
    Note: you may need to restart the kernel to use updated packages.


### Remove Packages
* `pip uninstall` followed by one or more package names will remove the packages

### Display Package information
* `pip show` will display information about a particular package:


```python
pip show requests
```

    Name: requests
    Version: 2.22.0
    Summary: Python HTTP for Humans.
    Home-page: http://python-requests.org
    Author: Kenneth Reitz
    Author-email: me@kennethreitz.org
    License: Apache 2.0
    Location: d:\applications\winpython-3.8\python-3.8.1.amd64\lib\site-packages
    Requires: certifi, idna, chardet, urllib3
    Required-by: twine, Sphinx, requests-toolbelt, quantecon, pyepsg, papermill, pandas-datareader, moviepy, intake
    Note: you may need to restart the kernel to use updated packages.


### List Packages
* `pip list` will display all of the packages installed in the virtual environment


```python
pip list
```

    Package                       Version     
    ----------------------------- ------------
    adodbapi                      2.6.1.3     
    affine                        2.3.0       
    aiofiles                      0.4.0       
    aiosqlite                     0.11.0      
    alabaster                     0.7.12      
    altair                        4.0.0    
    ...


### Freeze Packages
* `pip freeze` will produce a similar list of the installed packages, but the output uses the format that pip install expects.


```python
pip freeze
```

    adodbapi==2.6.1.3
    affine==2.3.0
    aiofiles==0.4.0
    aiosqlite==0.11.0
    alabaster==0.7.12
    altair==4.0.0
    ...

```python
pip freeze > requirements.txt
```

    Note: you may need to restart the kernel to use updated packages.

```python
f = open('requirements.txt')
print(f.read())
f.close()
```

    adodbapi==2.6.1.3
    affine==2.3.0
    aiofiles==0.4.0
    aiosqlite==0.11.0
    alabaster==0.7.12
    altair==4.0.0
    ...


```python
print(f.read())
```


    ---------------------------------------------------------------------------
    
    ValueError                                Traceback (most recent call last)
    
    <ipython-input-19-315c20b774c2> in <module>
    ----> 1 print(f.read())


    ValueError: I/O operation on closed file.

