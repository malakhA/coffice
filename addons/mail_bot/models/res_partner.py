# -*- coding: utf-8 -*-
# Part of COffice. See LICENSE file for full copyright and licensing details.
from coffice import api, models


class Partner(models.Model):
    _inherit = 'res.partner'

    def _compute_im_status(self):
        #we asume that mail_bot _compute_im_status will be executed after bus _compute_im_status
        super(Partner, self)._compute_im_status()
        cofficebot_id = self.env['ir.model.data'].xmlid_to_res_id("base.partner_root")
        for partner in self:
            if partner.id == cofficebot_id:
                partner.im_status = 'bot'

    @api.model
    def get_mention_suggestions(self, search, limit=8):
        #add cofficebot in mention suggestion when pinging in mail_thread
        [users, partners] = super(Partner, self).get_mention_suggestions(search, limit=limit)
        if len(partners) + len(users) < limit and "cofficebot".startswith(search.lower()):
            cofficebot = self.env.ref("base.partner_root")
            if not any([elem['id'] == cofficebot.id for elem in partners]):
                if cofficebot:
                    partners.append({'id': cofficebot.id, 'name': cofficebot.name, 'email': cofficebot.email})
        return [users, partners]

