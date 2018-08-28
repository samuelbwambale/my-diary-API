class Config:
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    TESTING = True

class DevelopmentConfig(Config):
    pass

class ProductionConfig(Config):
    DEBUG = False


config  = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}