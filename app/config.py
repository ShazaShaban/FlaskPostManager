class Config:
    @staticmethod
    def init__app():
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.sqlite' #specity the databse engine for sqlalchemy


class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI = 'postgresql://flask:iti@localhost:5432/flask_mvt_pymans1' #'engine://username:password@localhost:5432/dbname'
    


projectConfig = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig
}

#lw b3tlk dev return el development config kazalek el prd rg3ly production config