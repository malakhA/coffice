# Part of Coffice. See LICENSE file for full copyright and licensing details.
from coffice.tests import common
from coffice.exceptions import ValidationError


class TestRUCStructure(common.TransactionCase):

    def test_peru_ruc_format(self):
        """Only values that has the length of 11 will be checked as RUC, that's what we are proving. The second part
        will check for a valid ruc and there will be no problem at all.
        """
        partner = self.env['res.partner'].create({'name': "Dummy partner", 'country_id': self.env.ref('base.pe').id})

        with self.assertRaises(ValidationError):
            partner.vat = '11111111111'
        partner.vat = '20507822470'
