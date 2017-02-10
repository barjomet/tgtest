# -*- coding: utf-8 -*-
"""Pagina model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Text, Integer, Text, DateTime, LargeBinary
from sqlalchemy.orm import relationship, backref

from tgtest.model import DeclarativeBase, metadata, DBSession

__all__ = ['Association', 'Pagina', 'PaginasGroup', 'MassivePagina']


class Association(DeclarativeBase):
    __tablename__ = 'association'
    left_id = Column(Integer, ForeignKey('paginasgroups.uid'), primary_key=True)
    right_id = Column(Integer, ForeignKey('paginas.uid'), primary_key=True)


class Pagina(DeclarativeBase):
    __tablename__ = 'paginas'

    uid = Column(Integer, primary_key=True)
    data = Column(Text(255), nullable=False)



class PaginasGroup(DeclarativeBase):
    __tablename__ = 'paginasgroups'

    uid = Column(Integer, primary_key=True)
    data = Column(Text(255), nullable=False)

    members = relationship("Pagina",
                            secondary=Association.__table__)


class MassivePagina(DeclarativeBase):
    __tablename__ = 'massivepaginas'

    uid = Column(Integer, primary_key=True)
    for i in range(100):
        locals().update({'data%i' % i: Column(Text(255), nullable=False)})
