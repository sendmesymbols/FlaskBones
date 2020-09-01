import os


class base_config(object):
    """Default configuration options."""
    SITE_NAME = os.environ.get('APP_NAME', 'Flask Bones')

    SECRET_KEY = os.environ.get('SECRET_KEY', 'secrets')
    SERVER_NAME = os.environ.get('SERVER_NAME', '127.0.0.1:5000')

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'sendmesymbols@gmail.com'
    MAIL_PASSWORD = 'snqrlcaymrzzeahm'
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'sendmesymbols@gmail.com'

    '''
    https://app.redislabs.com/
    
    coror40380@hapremx.com
    97987987HJGKJHGKJHGbmbmnbm,b&&&^    
    '''
    REDIS_HOST = os.environ.get('REDIS_HOST', 'redis-19132.c1.ap-southeast-1-1.ec2.cloud.redislabs.com')
    REDIS_PORT = os.environ.get('REDIS_PORT', 19132)
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '97987987HJGKJHGKJHGbmbmnbm,b&&&^')
    REDIS_DB = os.environ.get('REDIS_DB', 'app2')
    #RQ_REDIS_URL = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)
    RQ_REDIS_URL = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)
    'redis://:password@localhost/0'
    RQ_REDIS_URL = "redis://:FWvKrXFujiUOVcBnM5Veqyl5ZxJgimjB@redis-19132.c1.ap-southeast-1-1.ec2.cloud.redislabs.com:19132/app2"
    'mysql://root:yaKhudaKhair@localhost/app'

    CACHE_HOST = os.environ.get('MEMCACHED_HOST', 'memcached')
    CACHE_PORT = os.environ.get('MEMCACHED_PORT', 11211)

    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 3306)
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'root')
    POSTGRES_PASS = os.environ.get('POSTGRES_PASS', 'yaKhudaKhair')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'app2')

    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (
        POSTGRES_USER,
        POSTGRES_PASS,
        POSTGRES_HOST,
        POSTGRES_PORT,
        POSTGRES_DB
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SUPPORTED_LOCALES = ['en']


class dev_config(base_config):
    """Development configuration options."""
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False


class test_config(base_config):
    """Testing configuration options."""
    TESTING = True
    WTF_CSRF_ENABLED = False
