from sqlalchemy import create_engine ,String,Integer,Column
from streamlit import exception
from database import Base,engine



class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key =True,autoincrement=True)
    first_name = Column(String,nullable=False)
    last_name =Column(String,nullable=False)
    phone = Column(String,nullable=True)
    user_email = Column(String, index=True,unique=True)
    hashed_password = Column(String(255), nullable=False)



try:
    Base.metadata.create_all(engine)

    print("Tables created successfully!")
except exception as e:
    print(e)
