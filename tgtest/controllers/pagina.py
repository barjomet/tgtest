# -*- coding: utf-8 -*-
"""Pagina controller module"""

from tg import expose, redirect, validate, flash, url
from tg import request, redirect, tmpl_context, render_template
from tg.decorators import paginate, with_trailing_slash
from tw2.bootstrap.forms import DataGrid
# from tg.i18n import ugettext as _
# from tg import predicates

from tgtest.lib.base import BaseController
from tgtest.model import DBSession, Pagina, MassivePagina, PaginasGroup


class ProperDataGrid(DataGrid):
    css_class="grid table table-hover table-stripped"
    resources=[]

regular_grid = ProperDataGrid(fields=[('ID', 'uid'), ('Data', 'data')])
massive_grid = ProperDataGrid(
    css_class="grid table table-hover table-stripped massive",
    fields = [('ID', 'uid')] + \
                           [('Data%s' % i, 'data%s' % i) for i in xrange(100)]
)
group_grid = ProperDataGrid(
    css_class="grid table table-hover table-stripped massive",
    fields=[('ID', 'uid'),('Data', 'data'),
            ('Members UIDs',
             lambda g: ' '.join([str(g.members[i].uid) for i in xrange(10)])),
            ('Member0 Data', lambda g: g.members[0].data),
            ('Member1 Data', lambda g: g.members[1].data),
            ('Member2 Data', lambda g: g.members[2].data),
            ('Member3 Data', lambda g: g.members[3].data),
            ('Member4 Data', lambda g: g.members[4].data),
            ('Member5 Data', lambda g: g.members[5].data),
            ('Member6 Data', lambda g: g.members[6].data),
            ('Member7 Data', lambda g: g.members[7].data),
            ('Member8 Data', lambda g: g.members[8].data),
            ('Member9 Data', lambda g: g.members[9].data)
    ]
)


class PaginaController(BaseController):

    def _before(self, *args, **kw):
        tmpl_context.project_name = "tgtest"

    @with_trailing_slash
    @expose('tgtest.templates.pagina')
    def index(self, **kw):
        return dict(page='pagina')

    @expose(content_type='text/html')
    def regular(self, **kw):
        pager = paginate("data", items_per_page=kw.get('items') or 10)
        pager.before_validate(None, kw)
        data = DBSession.query(Pagina)
        content = dict(page='pagina', title='Regular Paginas',
                       data=data, grid=regular_grid)
        pager.before_render(None, kw, content)
        return render_template(content, 'kajiki', 'tgtest.templates.list')

    @expose(content_type='text/html')
    def massive(self, **kw):
        pager = paginate("data", items_per_page=kw.get('items') or 10)
        pager.before_validate(None, kw)
        data = DBSession.query(MassivePagina)
        content = dict(page='pagina', title='Massive Paginas',
                       data=data, grid=massive_grid)
        pager.before_render(None, kw, content)
        return render_template(content, 'kajiki', 'tgtest.templates.list')


    @expose(content_type='text/html')
    def grouped(self, **kw):
        pager = paginate("data", items_per_page=kw.get('items') or 10)
        pager.before_validate(None, kw)
        data = DBSession.query(PaginasGroup)
        content = dict(page='pagina', title='Grouped Paginas',
                       data=data, grid=group_grid)
        pager.before_render(None, kw, content)
        return render_template(content, 'kajiki', 'tgtest.templates.list')


