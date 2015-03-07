from __future__ import unicode_literals

import unittest

from mopidy_ssd1306 import Extension


class ExtensionTest(unittest.TestCase):

    def test_get_default_config(self):
        ext = Extension()
        config = ext.get_default_config()
        # ext = frontend.TtsGpio(config, mock.sentinel.core)
        self.assertIn('[ssd1306]', config)
        self.assertIn('enabled = true', config)

    def test_get_config_schema(self):
        ext = Extension()
        schema = ext.get_config_schema()
        # self.assertIn('intexample', schema)
        #
