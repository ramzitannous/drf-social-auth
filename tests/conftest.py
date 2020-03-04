import pytest
from django.conf import settings
def pytest_configure():

    settings.configure(
        DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3',
                               'NAME': ':memory:'}},
        DEBUG=False,
        SITE_ID=1,
        SECRET_KEY='not very secret in tests',
        USE_I18N=True,
        USE_L10N=True,
        STATIC_URL='/static/',
        TEMPLATE_LOADERS=(
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ),
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ),
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',

            'rest_framework',
            'rest_framework.authtoken',
            'tests',

            'social_django',
            'drf_social'

        ),
        PASSWORD_HASHERS=(
            'django.contrib.auth.hashers.SHA1PasswordHasher',
            'django.contrib.auth.hashers.PBKDF2PasswordHasher',
            'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
            'django.contrib.auth.hashers.BCryptPasswordHasher',
            'django.contrib.auth.hashers.MD5PasswordHasher',
            'django.contrib.auth.hashers.CryptPasswordHasher',
        ),

        ANONYMOUS_USER_ID=-1,
        AUTHENTICATION_BACKENDS=(
            'django.contrib.auth.backends.ModelBackend',
            'social_core.backends.google.GoogleOAuth2',
            'social_core.backends.facebook.FacebookOAuth2',
        )

    )
    try:
        import django
        django.setup()

    except AttributeError:
        pass





@pytest.fixture(scope='session', autouse=True)
def setup_db(django_db_blocker):
    from drf_social.models import AuthProvider, Providers
    with django_db_blocker.unblock():
        provider = AuthProvider()
        provider.name = "test provider"
        provider.provider = Providers.FACEBOOK
        provider.client_id = "394616437866286"
        provider.client_secret = "933fd9b288f3b1a936350bce76261806"
        provider.scopes = ['email']
        provider.save()