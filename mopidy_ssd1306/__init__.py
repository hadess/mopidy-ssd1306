from __future__ import unicode_literals

import logging
import os

from mopidy import config, ext

__version__ = '1.0.0'


logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = 'Mopidy-Ssd1306'
    ext_name = 'ssd1306'
    version = __version__

    def get_font_path(self):
        return os.path.join(os.path.dirname(__file__), 'pf_ronda_seven.ttf')

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['boolexample'] = config.Boolean()
        schema['intexample'] = config.Integer()
        return schema

    def setup(self, registry):

        from .frontend import Ssd1306
        registry.add('frontend', Ssd1306)
