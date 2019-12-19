# -*- coding: utf-8 -*-
import ipaddress

from coffice import _, SUPERUSER_ID
from coffice.http import request
from coffice.addons.web.controllers import main as web

def _admin_password_warn(uid):
    """ Admin still has `admin` password, flash a message via chatter.

    Uses a private mail.channel from the system (/ cofficebot) to the user, as
    using a more generic mail.thread could send an email which is undesirable

    Uses mail.channel directly because using mail.thread might send an email instead.
    """
    if request.params['password'] != 'admin':
        return
    if ipaddress.ip_address(request.httprequest.remote_addr).is_private:
        return
    admin = request.env.ref('base.partner_admin')
    if uid not in admin.user_ids.ids:
        return

    user = request.env(user=uid)['res.users']
    MailChannel = request.env(user=SUPERUSER_ID, context=user.context_get(), su=True)['mail.channel']
    MailChannel.browse(MailChannel.channel_get([admin.id])['id'])\
        .message_post(
            body=_("Your password is the default (admin)! If this system is exposed to untrusted users it is important to change it immediately for security reasons. I will keep nagging you about it!"),
            message_type='comment',
            subtype='mail.mt_comment'
        )

class Home(web.Home):
    def _login_redirect(self, uid, redirect=None):
        if request.params.get('login_success'):
            _admin_password_warn(uid)

        return super()._login_redirect(uid, redirect)
