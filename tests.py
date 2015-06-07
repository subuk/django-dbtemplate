import sys
import django
from django.conf import settings
from django.test.utils import get_runner

settings.configure(
    DEBUG=True,
    TEST_RUNNER='django.test.runner.DiscoverRunner',
    ROOT_URLCONF='domains.tests.urls',
    DBTEMPLATE_MAGIC_COOKIE='Iknow',
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'dbtemplate',
        'dbtemplate.tests.app',
    ),
    TEMPLATE_LOADERS=(
        'dbtemplate.loader.DatabaseLoader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ),
    MIDDLEWARE_CLASSES=(
    ),
    CACHES=({
        'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'},
    })
)


def main():
    if hasattr(django, 'setup'):
        django.setup()
    runner = get_runner(settings)(verbosity=2)
    sys.exit(runner.run_tests(["dbtemplate"]))


if __name__ == '__main__':
    main()
