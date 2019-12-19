# -*- coding: utf-8 -*-

from coffice import fields, models

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    l10n_sg_unique_entity_number = fields.Char(string='UEN')
