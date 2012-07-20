class Default(object):
    DEBUG = False
    TESTING = False

class Debug(Default):
    # TODO: register this email address
    ADMINS = ['forivall@gmail.com']
    DEBUG = True
    SECRET_KEY = '\xc0 \x188\x9a\xe4\x98\xb5qS\x82\x86,\xb7\xe6\xe7\x8aH+wK\xbe%\x82'

class Release(Default):
    import secret_keys
    ADMINS = ['admin@istf2up.com']
    SECRET_KEY = secret_keys.SESSION_KEY

