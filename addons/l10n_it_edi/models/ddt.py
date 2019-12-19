# -*- coding:utf-8 -*-
# Part of Coffice. See LICENSE file for full copyright and licensing details.

from coffice import fields, models, api

class L10nItDdt(models.Model):
    _name = 'l10n_it.ddt'
    _description = 'Transport Document'

    invoice_id = fields.One2many('account.move', 'l10n_it_ddt_id', string='Invoice Reference', ondelete='cascade')
    name = fields.Char(string="Numero DDT", size=20, help="Transport document number", required=True)
    date = fields.Date(string="Data DDT", help="Transport document date", required=True)

    def name_get(self):
        res = []
        for ddt in self:
            res.append((ddt.id, ("%s (%s)") % (ddt.name, ddt.date)))
        return res