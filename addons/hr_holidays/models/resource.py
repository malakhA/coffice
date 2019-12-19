# -*- coding: utf-8 -*-
# Part of Coffice. See LICENSE file for full copyright and licensing details.

from coffice import fields, models


class CalendarLeaves(models.Model):
    _inherit = "resource.calendar.leaves"

    holiday_id = fields.Many2one("hr.leave", string='Leave Request')