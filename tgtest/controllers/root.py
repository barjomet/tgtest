# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tgtest.model import DBSession

from tgtest.lib.base import BaseController
from tgtest.controllers.error import ErrorController
from tgtest.controllers.pagina import PaginaController

__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the tgtest application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """

    error = ErrorController()
    pagina = PaginaController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "tgtest"

    @expose('tgtest.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')
