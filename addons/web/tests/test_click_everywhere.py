# Part of Coffice. See LICENSE file for full copyright and licensing details.

import logging
import coffice.tests

_logger = logging.getLogger(__name__)


@coffice.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusAdmin(coffice.tests.HttpCase):

    def test_01_click_everywhere_as_admin(self):
        menus = self.env['ir.ui.menu'].load_menus(False)
        for app in menus['children']:
                with self.subTest(app=app['name']):
                    _logger.log(25, 'Testing %s', app['name'])
                    self.browser_js("/web", "coffice.__DEBUG__.services['web.clickEverywhere'](%d);" % app['id'], "coffice.isReady === true", login="admin", timeout=300)
                    self.terminate_browser()


@coffice.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusDemo(coffice.tests.HttpCase):

    def test_01_click_everywhere_as_demo(self):
        menus = self.env['ir.ui.menu'].load_menus(False)
        for app in menus['children']:
                with self.subTest(app=app['name']):
                    _logger.log(25, 'Testing %s', app['name'])
                    self.browser_js("/web", "coffice.__DEBUG__.services['web.clickEverywhere'](%d);" % app['id'], "coffice.isReady === true", login="demo", timeout=300)
                    self.terminate_browser()
