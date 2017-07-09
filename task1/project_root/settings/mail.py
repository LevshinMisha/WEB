EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'mishalevshin123@gmail.com'
EMAIL_HOST_PASSWORD = 'Misha123456'
EMAIL_USE_SSL = True

EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_FILE_PATH = '/tmp/app-messages'