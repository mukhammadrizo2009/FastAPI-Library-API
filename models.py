import enum 
from datetime import datetime
from sqlalchemy import (
    Column ,
    Integer ,
    String ,
    Text , 
    DateTime ,
    CheckConstraint , 
    Enum
)
from database import Base

class Genre(str , enum.Enum):
    roman = "Roman"
    story = "Hikoya"
    drama = "Drama"
    
class Book(Base):
    __tablename__ = "books"
    
    book_id = Column("id", Integer , primary_key=True , index=True , nullable=False)
    title = Column(String(length=30), nullable=False)
    author = Column(String(length=30) , nullable=False)
    description = Column(Text)
    pages = Column(Integer, CheckConstraint("pages >=1") , nullable=False)
    genre = Column(Enum(Genre), nullable=False)
    
    created_at =  Column('created_at', DateTime, default=datetime.now)
    updated_at =  Column("updared_at", DateTime , default=datetime.now)