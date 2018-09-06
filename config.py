class Config:
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    TESTING = True

class DevelopmentConfig(Config):
    pass

config  = {
    'testing': TestingConfig,
    'development': DevelopmentConfig
    }
    