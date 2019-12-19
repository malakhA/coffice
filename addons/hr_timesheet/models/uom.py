# -*- coding: utf-8 -*-
# Part of COffice. See LICENSE file for full copyright and licensing details.

from coffice import fields, models


class Uom(models.Model):
    _inherit = 'uom.uom'

    timesheet_widget = fields.Char("Widget", help="Widget used in the webclient when this unit is the one used to encode timesheets.")
