import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    followers = Column(Integer)
    following = Column(Integer)

    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(Usuario)

class Comentarios(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(Post)

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    likes = Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(Post)
# Duda: podría relacionar mi tabla de likes ya generada con comentarios 
# o tendría que crear una tabla para los likes de los comentarios?

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
