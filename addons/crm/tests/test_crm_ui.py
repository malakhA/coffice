# Part of COffice. See LICENSE file for full copyright and licensing details.

import coffice.tests


@coffice.tests.tagged('post_install','-at_install')
class TestUi(coffice.tests.HttpCase):

    def test_01_crm_tour(self):
        self.start_tour("/web", 'crm_tour', login="admin")
