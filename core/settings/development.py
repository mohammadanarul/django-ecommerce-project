from .base import *

#debuging deplopment times
DEBUG = True

#hosr allow
ALLOWED_HOSTS = ['127.0.0.1']

# Database connection
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

'''
jar jibone kew nei sei boje na thakar jontro na ta kto dur.
r jar ase se o boje thakatar ktota jontro na.
kosto duikhanei ase. na pawar jemon jontro na thik pawar o same jontro na.
tahole akhon kora jabe?
'''