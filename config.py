
class Development:
    DEBUG = True
    TESTING = False

class Testing:
    DEBUG = True
    TESTING = True


config  = {
    'development': Development,
    'testing': Testing
}