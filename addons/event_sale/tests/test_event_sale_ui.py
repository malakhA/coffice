import coffice.tests
# Part of Coffice. See LICENSE file for full copyright and licensing details.


@coffice.tests.tagged('post_install', '-at_install')
class TestUi(coffice.tests.HttpCase):
    def test_01_event_configurator(self):
        self.start_tour("/web", 'event_configurator_tour', login="admin")
