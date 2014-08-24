django-rest-framework-saasy
===========================

#### Overview

This is a SaaS driven plugin for Django REST Framework. It offers a simple way
to separate client customizations for your core API web services. Currently, this
initial version only supports client API routing via ViewSets in conjunction with
an extension of the Django REST Framework SimpleRouter. 

#### Install
```pip install djangorestframework-saasy```

#### How to use

```python
class ClientMixin(object):
    """
    To be mixed with the relevant model associated with a "customer" of
    your platform/service(s) - the settings value of:
    
    REST_SETTINGS = {
        ...
        "SAAS": {
            "MODEL": "app.client.Model"
        }
        ...
    }

    The ClientMixin class dictates the implementation rules. There
    is no functionality defined here.
    """

    def saas_lookup_field(self, *args, **kwargs):
        """Define the model lookup field to use when querying the database
        for the client record"""
        raise NotImplementedError

    def saas_client_module(self, saas_url_kw, *args, **kwargs):
        """Optional method to define client module path"""
        pass
```

```
project
├── customizations
│   └──client
│       └── app
│           └── subpackage
│               └── module.py
└── app
    └── subpackage 
        └── module.py
```

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
