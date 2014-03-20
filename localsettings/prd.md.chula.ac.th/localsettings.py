DEBUG = True
DATABASES = {
        'default': {
        'NAME': 'FASSQL',
        'ENGINE': 'sqlserver_ado',
        'HOST': '127.0.0.1',
        'PORT': '30001',
        'USER': 'chrimatostech',
        'PASSWORD': 'chrimatos',
        'OPTIONS' :
            {'provider': 'SQLOLEDB'}
            },
    }