import sys
import django
from django.conf import settings
from django.test.utils import get_runner

settings.configure(
    DEBUG=True,
    TEST_RUNNER='django.test.runner.DiscoverRunner',
    ROOT_URLCONF='domains.tests.urls',
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    INSTALLED_APPS=(
        'dbtemplate',
        'dbtemplate.tests.app',
    ),
    TEMPLATE_LOADERS=(
        'dbtemplate.loader.DatabaseLoader',
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
