django-xml-backend-demo
=======================

Django with XML backend (a trivial demo, no models involved)

To get started:
* https://docs.djangoproject.com/en/1.5/
* https://github.com/tomchristie/django-serializers
* http://stackoverflow.com/questions/3055650/django-custom-serialization-options
* http://stackoverflow.com/questions/757022/how-do-you-serialize-a-model-instance-in-django
* https://docs.djangoproject.com/en/1.5/misc/design-philosophies/
* https://docs.djangoproject.com/en/1.5/ref/contrib/flatpages/
* https://docs.djangoproject.com/en/1.5/ref/contrib/databrowse/
* https://docs.djangoproject.com/en/1.5/topics/serialization
* https://docs.djangoproject.com/en/1.5/ref/templates/api/

On the OS, install 
* python-django
* python-lxml 
* python-webtest (for tests, see http://codeinthehole.com/writing/prefer-webtest-to-djangos-test-client-for-functional-tests/)

To get the webapp running:
      python manage.py runserver

To test the application
      python manage.py test xmlview

