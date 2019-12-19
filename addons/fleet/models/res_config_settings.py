# -*- coding: utf-8 -*-
# Part of Coffice. See LICENSE file for full copyright and licensing details.

from coffice import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    delay_alert_contract = fields.Integer(string='Delay alert contract outdated', default=30, config_parameter='hr_fleet.delay_alert_contract')
