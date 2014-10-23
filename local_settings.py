__author__ = 'northdacoder'



AWS_ACCESS_KEY_ID = 'AKIAJOHD7RH7G4JBJFFQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'awsnoopdog'

STATICFILES_STORAGE = 'test_aws.s3utils.StaticRootS3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

S3_URL = '//{}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)

MEDIA_URL = S3_URL + "media/"
STATIC_URL = S3_URL + "static/"
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_aws',
    }
}