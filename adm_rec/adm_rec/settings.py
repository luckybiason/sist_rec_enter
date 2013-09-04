#-*- coding: utf-8 -*-
# Django settings for adm_rec project.

# - Pasta do projeto
import os
PASTA_PROJETO = os.path.dirname(__file__)

# - Debug ou produção
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# - Administradores do sistema
ADMINS = (
    ('Lucas Biason', 'biasonlucky10@gmail.com'), # Programação e Processos
    #('Robson Moraes',     ''), # Programação
    #('Alfredo Stanquini', ''), # Programação
    #('Miguel Freitas',    ''), # Testes
    #('Priscila Rossoni',  ''), # Documentação dos processos e Validaçao/Verificação
)
MANAGERS = ADMINS

# - Profile do usuario
#AUTH_PROFILE_MODULE = 'ui_theme_profile.PerfilUser'

# - Configuração de e-mail
EMAIL_USE_TLS        = True
EMAIL_HOST           = 'smtp.gmail.com'
EMAIL_HOST_USER      = 'biasonlucky10@gmail.com'
EMAIL_HOST_PASSWORD  = ''
EMAIL_PORT = 587

# - Configuração de Banco de dados
DATABASES = {
    'default': {
        'ENGINE':    'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.     
        'NAME':      os.path.join(PASTA_PROJETO, 'banco.db'),
        'USER':     '',     
        'PASSWORD': '', 
        'HOST':     '',     
        'PORT':     '',     
    }
}

SITE_ID = 1

# - Configuração de time-zones, localização e internacionalização
TIME_ZONE          = 'America/Chicago'
LANGUAGE_CODE      = 'pt-BR'
USE_I18N           = True
USE_L10N           = True
USE_TZ             = True
FORMAT_MODULE_PATH = 'formats'

# - Configurações de media e arquivos estáticos
MEDIA_ROOT          = os.path.join(PASTA_PROJETO,'media')
MEDIA_URL           = '/media/'
ADMIN_MEDIA_PREFIX  = '/media_admin/'
STATIC_URL          = '/static/'
STATICFILES_DIRS    = (
    os.path.join(PASTA_PROJETO, '../static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8qg72rnv1&amp;xa#96vfrc3d#0^5)$-m$z@#lt$6#*-07bp!zlqc%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'adm_rec.middleware.tools.LoginEnforce',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'adm_rec.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'adm_rec.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PASTA_PROJETO, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Componentes externos
    'adm_rec',           # Projeto
    'alerts_e_messages', # Sistema de alertas e mensagens
    'basiccrud',         # Componente de CRUD básico
    'captchas',          # Componente de captchas
    'debug_toolbar',     # Barra de Debug Template do django
    'py_aumenu',         # Componente de Menu 
    # Modelos de dados
    'lojas',
    'usuario',
    'televisores',
    'clientes',
    'propagandas',
    # Portal
    'portal',            # App base do portal
    'busca' ,            # App com mecanismo de busca de produtos
    # 'recomendacoes'    # Motor do sistema de recomendação
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    #
    'django.core.context_processors.request',
    'py_aumenu.contrib.menu_maker',           # CP para Componente de Menu (Pronto)
    'captchas.contrib.client_captcha',        # CP para Componente de captchas parametrizados 
    'adm_rec.contrib.user_logado',            # CP para imprimir dados do Usuário (Para o sist. ADM)
    'clientes.context_processors.id_cliente', # CP para injetar o id co cliente logado nos templates.
) 

#####################################################################################
# Configuração para o login
LOGIN_URL          = "/adm/login/"
LOGOUT_URL         = "/adm/logout/"
LOGIN_REDIRECT_URL = "/adm/"

PUBLIC_URLS = (
    r'/adm/login/',
    r'/adm/logout/',
    r'/adm/$',
)
#####################################################################################

#####################################################################################
# Configurações da DjangoDebugToolbar - https://pypi.python.org/pypi/django-debug-toolbar
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': (lambda request: True or False),
    'INTERCEPT_REDIRECTS'  : False,
}
#####################################################################################

#####################################################################################
# Configuração para o Captcha utilizado no sistema
CAPTCHA_TYPE = ['reorder','ebword','reorder','motion'][-1]
#####################################################################################
