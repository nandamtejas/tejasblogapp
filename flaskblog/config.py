class Config():
    SECRET_KEY = 'b549f797b61418c135dc2a50d112cc4a'
    SQLALCHEMY_DATABASE_URI = 'postgres://hnzpctnpifrwva:06e9854f0d6da12b0ebbeb45ea3849f711a0fe28bc30fefae61374a3242f3054@ec2-52-21-247-176.compute-1.amazonaws.com:5432/deriu8cufs5gts'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tejastesting1306@gmail.com'
    MAIL_PASSWORD = 'nandamtejas1306'
    SQLALCHEMY_TRACK_MODIFICATIONS = True