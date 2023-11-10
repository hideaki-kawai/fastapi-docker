from sqlalchemy import create_engine

from api.models.task import Base

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
# echo=Trueで実行されるSQLコマンドをコンソールに出力できるオプション
engine = create_engine(DB_URL, echo=True)


def reset_datebase():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_datebase()
