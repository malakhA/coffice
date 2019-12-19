# -*- coding: utf-8 -*-
# Part of COffice. See LICENSE file for full copyright and licensing details.

from coffice import fields, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    invoice_reference_model = fields.Selection(selection_add=[('no', 'Norway')])
