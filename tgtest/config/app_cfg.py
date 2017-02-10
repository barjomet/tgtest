# -*- coding: utf-8 -*-
"""
Global configuration file for TG2-specific settings in tgtest.

This file complements development/deployment.ini.

"""
from tg.configuration import AppConfig

import tgtest
from tgtest import model, lib

base_config = AppConfig()
base_config.renderers = []

# True to prevent dispatcher from striping extensions
# For example /socket.io would be served by "socket_io"
# method instead of "socket".
base_config.disable_request_extensions = False

# Set None to disable escaping punctuation characters to "_"
# when dispatching methods.
# Set to a function to provide custom escaping.
base_config.dispatch_path_translator = True

base_config.prefer_toscawidgets2 = True

base_config.package = tgtest

# Enable json in expose
base_config.renderers.append('json')

# Set the default renderer
base_config.renderers.append('kajiki')
base_config['templating.kajiki.strip_text'] = False  # Change this in setup.py too for i18n to work.

base_config.default_renderer = 'kajiki'


# Configure Sessions, store data as JSON to avoid pickle security issues
base_config['session.enabled'] = True
base_config['session.data_serializer'] = 'json'
# Configure the base SQLALchemy Setup
base_config.use_sqlalchemy = True
base_config.model = tgtest.model
base_config.DBSession = tgtest.model.DBSession
try:
    # Enable DebugBar if available, install tgext.debugbar to turn it on
    from tgext.debugbar import enable_debugbar
    enable_debugbar(base_config)
except ImportError:
    pass
