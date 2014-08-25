Django REST Framework SaaS Plugin
=================================

### Overview

This is a SaaS driven plugin for Django REST Framework. It offers a simple way
to separate client customizations for your core API web services. Currently, this
initial version only supports client API routing via ViewSets in conjunction with
an extension of the Django REST Framework SimpleRouter. Future releases will
have broader coverage of DRF features for custom client routing.

### Install
```pip install djangorestframework-saasy```

### Requirements
- Python (2.7)
- Django (1.4.2+)
- Django rest framework (2.3.14+)

### Example

Define the client model in your django rest framework settings:
```python
REST_SETTINGS = {
    ...
    "SAAS": {
        "MODEL": "path.to.model.ClientModel"
    }
    ...
}
```

Use the saas client mixin provided by the SaaS plugin, and define the required class methods:
```python
from django.db import models
from rest_framework_saasy.client import ClientMixin


class ClientModel(models.Model, ClientMixin):
    """client model"""
    name = models.CharField(max_length=128)

    @staticmethod
    def saas_lookup_field():
        """DRF-SaaS lookup field definition"""
        return 'name'

    def saas_client_module(self, saas_url_kw, *args, **kwargs):
        return 'customizations.{}'.format(self.name)
```

#### ClientMixin methods

- *saas_lookup_field* **[required]**

  This method defines what field in your client model to use when looking up
  the client in the database, to verify they exist.

- *saas_client_module* **[required]**

  Parameters:
  - *saas_url_kw* - [string] - value from URL key word argument - the client
  idenfitication value.

  All client code should be separated from the core and also from each other.
  A good practice to follow is that there is a folder for all client specific code,
  separate from the core, with a folder for each client. That said, you can impose
  any kind of path rules you wish.
  
  ```
  project
  ├── customizations
  │   └── client_name
  │       └── app
  │           └── subpackage
  │               └── module.py
  └── app
      └── subpackage 
          └── module.py
  ```

### ViewSets

The idea is there is a core web service ViewSet, *WebService*, defined 
in **app.subpackage.module** and in **customizations.client_name.app.subpackage.module** 
where there is also a class named *WebService*

**app.subpackage.module**
```python
from rest_framework import viewsets
from rest_framework_saasy import viewsets as saas_viewsets

from .models import WebServiceModel
from .serializers import WebServiceSerializer

class WebService(saas_viewsets.ViewSetMixin, viewsets.ModelViewSet):
    queryset = WebServiceModel.objects.all()
    serializer_class = WebServiceSerializer
```

**customizations.client.app.subpackage.module**
```python
from app.subpackage.module import WebService as CoreWebService

class WebService(CoreWebService):
    # client customizations
```

You can define the module path of client code and you can also define the subpackage
path for the ViewSet mixed with the *saas_viewsets.ViewSetMixin*.

What cannot be customized is the name of the class - the class name *WebService* in the
core must be defined identically in the client custom module.

#### ViewSetMixin methods

- *saas_module* **[optional]**

  By default, viewset will be routed in a similar way as in the diagram above:
  
  ```
  project
  ├── customizations
  │   └── client_name
  │       └── app
  │           └── subpackage
  │               └── module.py
  └── app
      └── subpackage 
          └── module.py
  ```
  
  However, the SaaS viewset has an optional method that can be defined, *saas_module*
  This returns the path that should be used in the client package. **It must be 
  defined with the staticmethod decorator.** Let's slightly alter our *WebService* example above:
  
  ```python
  class WebService(saas_viewsets.ViewSetMixin, viewsets.ModelViewSet):
      ...
      @staticmethod
      def saas_module():
          return 'other.package.name'
  ```
  
  The expected file system package defintion for *WebService* customizations would be:
  
  ```
  project
  ├── customizations
  │   └── client_name
  │       └── other
  │           └── package
  │               └── name.py
  └── app
      └── subpackage 
          └── module.py
  ```

#### ViewSet attributes

*saas_url_kw* is a new attribute made available to the ViewSet instance. 
The value of the valid identifier from the URL key word argument can be 
accessed at any time. If no client specific route was used, *saas_url_kw*
defaults to None.

### SaaS SimpleRouter

You'll register your new SaaSy viewsets in exactly the same way Django
REST Framework defines.

#### app.urls
```python
from rest_framework_saasy import routers
from .views import NoteViewSet


router = routers.SimpleRouter()
router.register(r'notes', NoteViewSet)
```

Client specific routes will be made available immediately:
```
^notes/$ [name='note-list']
^notes/(?P<pk>[^/]+)/$ [name='note-detail']
^(?P<saas_url_kw>.*)/notes/$ [name='note-list']
^(?P<saas_url_kw>.*)/notes/(?P<pk>[^/]+)/$ [name='note-detail']
```

**Note:** If a client key word argument is provided, but the client cannot
be retreived from the database with the given identifier, the
plugin will simply return a 404.

License
=======
The MIT License (MIT)

Copyright (c) 2014 Juan Gutierrez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
