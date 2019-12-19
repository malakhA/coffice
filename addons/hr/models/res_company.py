# -*- coding: utf-8 -*-
# Part of Coffice. See LICENSE file for full copyright and licensing details.

from coffice import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    hr_presence_control_email_amount = fields.Integer(string="# emails to send")
    hr_presence_control_ip_list = fields.Char(string="Valid IP addresses")
