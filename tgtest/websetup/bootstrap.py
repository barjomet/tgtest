# -*- coding: utf-8 -*-
"""Setup the tgtest application"""
from __future__ import print_function, unicode_literals
import logging
import transaction
from tgtest import model
from random import getrandbits, sample
from zope.sqlalchemy import mark_changed

log = logging.getLogger(__name__)

def randstring(n=255):
    return u'%0x' % getrandbits(n * 4)

def bootstrap(command, conf, vars):

    counter = xrange(100000)

    log.info("Generation of random paginas is comming")
    log.info("Generation of Paginas")
    model.DBSession.bulk_insert_mappings(model.Pagina,
                                        [dict(data=randstring())
                                         for i in counter])
    mark_changed(model.DBSession())
    transaction.commit()

    log.info("Generation of PaginasGroups")
    model.DBSession.bulk_insert_mappings(model.PaginasGroup,
                                        [dict(data=randstring())
                                        for i in counter])

    model.DBSession.bulk_insert_mappings(model.Association,
                                         [dict(left_id=g+1,
                                               right_id=p+1)
                                          for g in counter
                                          for p in sample(counter, 10)])

    mark_changed(model.DBSession())
    transaction.commit()

    log.info("Generation of MassivePaginas")
    for i in xrange(100):
        model.DBSession.bulk_insert_mappings(model.MassivePagina,
                                            [dict(('data%i' % i,
                                                   randstring())
                                                  for i in xrange(100))
                                             for j in xrange(1000)])
        mark_changed(model.DBSession())
        transaction.commit()
        log.info('%i%%' % i)

    log.info('Done')

