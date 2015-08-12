def pytest_configure():
    from django.conf import settings

    settings.configure(
        DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3',
                               'NAME': ':memory:'}},
        ROOT_URLCONF='tests.urls',
        INSTALLED_APPS=(
            'rest_framework',
            'rest_framework_saasy',
            'tests',
        ),
        REST_FRAMEWORK={'SAAS': {'MODEL': 'tests.models.ClientModel',
                                 'LOOKUP_FIELD': 'name'}}
    )
