## Code of conduct

Please remember to extend the same courtesy to others as you would wish them to extend to you. The [Angular code of conduct][angular-code-of-conduct] and [Django code of conduct][django-code-of-conduct] provide some concise and useful guidelines. 

Keep it clean, constructive and creative. Let's make sure everyone feels welcome.

## Issues, Features, and Questions

Usage questions should be directed to the [discussion group][google-group]. Feature requests, bug reports and other issues should be raised on the GitHub issue tracker.

Don't be bashful though - feel free to create a pull request with your proposed feature/bug fix.

## Development

As for most python projects, create a virtualenv for your local version of the project. To start development, clone the repository and install the requirements:

    git clone git@github.com:juannyG/django-rest-framework-saasy.git
    cd django-rest-framework-saasy
    pip install -r requirements.txt

### Running Tests

To run tests against your version python:

    pip install pytest pytest-django
    py.test tests.py

or, our preference, which checks against the supported versions of python (and is also how our Travis-CI is configured)

    tox

Always run the tests before submitting pull requests. Once you've made a pull request take a look at the Travis build status in the GitHub interface and make sure the tests are running as you'd expect.

If you're unfamiliar with tox or py.test, please check these links out:
- [tox](https://tox.readthedocs.org/en/latest/)
- [py.test](http://pytest.org/latest/)
- [py.test + tox](http://tox.readthedocs.org/en/latest/example/pytest.html)

[angular-code-of-conduct]: https://github.com/angular/code-of-conduct/blob/master/CODE_OF_CONDUCT.md
[django-code-of-conduct]: https://www.djangoproject.com/conduct/
[google-group]: https://groups.google.com/forum/#!forum/django-rest-framework-saas-plugin
