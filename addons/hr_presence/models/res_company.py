# -*- coding: utf-8 -*-
# Part of COffice. See LICENSE file for full copyright and licensing details.

from coffice import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    hr_presence_last_compute_date = fields.Datetime()
