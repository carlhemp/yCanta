# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, UnicodeText, DateTime
from sqlalchemy.ext.declarative import declared_attr
#from sqlalchemy.orm import relation, backref

from ycanta.model import DeclarativeBase, metadata, DBSession
from ycanta.model.auth import User

class LastModifiedMixin(object):
  @declared_attr
  def last_modified_who(cls):
    return Column(ForeignKey(User.user_id))
  last_modified_ts  = Column(DateTime, default=func.now())

class Book(LastModifiedMixin, DeclarativeBase):
  __tablename__ = 'book'
  
  id            = Column(Integer, primary_key=True)
  title         = Column(Unicode(), nullable=False, unique=True)
  content       = Column(UnicodeText(), nullable=False)
  configuration = Column(UnicodeText(), nullable=True)
  
  def repr(self):
    return '<Book: id=%s title=%s>' % (repr(self.id), repr(self.title))


class BookHistory(LastModifiedMixin, DeclarativeBase):
  __tablename__ = 'book_history'

  id      = Column(Integer, primary_key=True)
  book_id = Column(ForeignKey(Book.id))
  content = Column(UnicodeText(), nullable=False)


class Song(LastModifiedMixin, DeclarativeBase):
  __tablename__ = 'song'

  id           = Column(Integer, primary_key=True)
  title        = Column(Unicode(), nullable=False)
  author       = Column(Unicode(), nullable=False)
  scripture    = Column(Unicode(), nullable=True)
  introduction = Column(Unicode(), nullable=True)
  key          = Column(Unicode(), nullable=True)
  categories   = Column(Unicode(), nullable=True)
  ccli         = Column(Boolean(), nullable=False)
  copyright    = Column(Unicode(), nullable=True)
  content      = Column(UnicodeText(), nullable=False)
  
  def repr(self):
    return '<Song: id=%s title=%s author=%s>' % (repr(self.id), repr(self.title), repr(self.author))


class SongHistory(LastModifiedMixin, DeclarativeBase):
  __tablename__ = 'song_history'

  id      = Column(Integer, primary_key=True)
  song_id = Column(ForeignKey(Song.id))
  content = Column(UnicodeText(), nullable=False)


