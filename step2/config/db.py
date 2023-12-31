from sqlalchemy import create_engine, MetaData


meta = MetaData()

engine = create_engine("mysql+pymysql://root@localhost:3307/test", echo=True)

conn =engine.connect()

meta.create_all(engine)