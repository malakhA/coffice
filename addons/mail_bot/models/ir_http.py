# -*- coding: utf-8 -*-
# Part of COffice. See LICENSE file for full copyright and licensing details.

from coffice import models


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(Http, self).session_info()
        if self.env.user.has_group('base.group_user'):
            res['cofficebot_initialized'] = self.env.user.cofficebot_state != 'not_initialized'
        return res
