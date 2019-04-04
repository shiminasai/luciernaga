"""
Django settings for luciernaga project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from .local_settings import *


# Application definition

INSTALLED_APPS = [
    #'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    #third party
    'taggit',
    'sorl.thumbnail',
    'tinymce',
    'filebrowser',
    #'geoposition',
    'location_field.apps.DefaultConfig',
    'import_export',
    'solo.apps.SoloAppConfig',
    'el_pagination',
    'sitetree',
    'places',
    'embed_video',
     #apps
    'noticias',
    'eventos',
    'videoteca',
    'configuracion',
]

GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyBdQtBr_qwV2fMWrT4FrzBOziYTw2odlVo'
# GEOPOSITION_MAP_OPTIONS = {
#     'minZoom': 3,
#     'maxZoom': 15,
# }

# GEOPOSITION_MARKER_OPTIONS = {
#     'cursor': 'move'
# }

PLACES_MAPS_API_KEY='AIzaSyBdQtBr_qwV2fMWrT4FrzBOziYTw2odlVo'
PLACES_MAP_WIDGET_HEIGHT=480
PLACES_MAP_OPTIONS='{"center": { "lat": 38.971584, "lng": -95.235072 }, "zoom": 10}'
PLACES_MARKER_OPTIONS='{"draggable": true}'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

SITE_ID = 1
ROOT_URLCONF = 'luciernaga.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'luciernaga.context.global_news',
            ],
        },
    },
]

WSGI_APPLICATION = 'luciernaga.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es-ni'

TIME_ZONE = 'America/Managua'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'

STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_media"),
]

LOCATION_FIELD_PATH = STATIC_URL + 'location_field'

LOCATION_FIELD = {
    'map.provider': 'openstreetmap',
    'map.zoom': 13,

    'search.provider': 'nominatim',
    'search.suffix': 'Nicaragua',

    # OpenStreetMap
    'provider.openstreetmap.max_zoom': 18,

    # misc
    'resources.root_path': LOCATION_FIELD_PATH,
    'resources.media': {
        'js': [
            LOCATION_FIELD_PATH + '/js/jquery.livequery.js',
            LOCATION_FIELD_PATH + '/js/form.js',
        ],
    },
}

TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': '75%',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    #'extended_valid_elements': 'blockquote[*]',
    #'extended_valid_elements': 'script[*]',
    #'extended_valid_elements': 'iframe[*]',
    'valid_elements': "*[*]",
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }

#TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True

# JET_DEFAULT_THEME = 'light-gray'
# JET_SIDE_MENU_COMPACT = True
# JET_THEMES = [
#     {
#         'theme': 'default', # theme folder name
#         'color': '#47bac1', # color of the theme's button in user menu
#         'title': 'Default' # theme title
#     },
#     {
#         'theme': 'green',
#         'color': '#44b78b',
#         'title': 'Green'
#     },
#     {
#         'theme': 'light-green',
#         'color': '#2faa60',
#         'title': 'Light Green'
#     },
#     {
#         'theme': 'light-violet',
#         'color': '#a464c4',
#         'title': 'Light Violet'
#     },
#     {
#         'theme': 'light-blue',
#         'color': '#5EADDE',
#         'title': 'Light Blue'
#     },
#     {
#         'theme': 'light-gray',
#         'color': '#222',
#         'title': 'Light Gray'
#     }
# ]


