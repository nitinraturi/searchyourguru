if DEBUG:
    ALLOWED_HOSTS = ['*','127.0.0.1','localhost']
else:
    ALLOWED_HOSTS = ['127.0.0.1','localhost'] # set this to your domain.in,ip,etc


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

X_FRAME_OPTIONS = 'DENY'
