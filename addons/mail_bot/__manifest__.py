# -*- coding: utf-8 -*-
# Part of COffice. See LICENSE file for full copyright and licensing details.

{
    'name': 'COfficeBot',
    'version': '1.0',
    'category': 'Discuss',
    'summary': 'Add COfficeBot in discussions',
    'description': "",
    'website': 'https://www.coffice.com/page/discuss',
    'depends': ['mail'],
    'installable': True,
    'application': False,
    'auto_install': True,
    'data': [
        'views/assets.xml',
        'views/res_users_views.xml',
        'data/mailbot_data.xml',
    ],
    'demo': [
        'data/mailbot_demo.xml',
    ],
    'qweb': [
        'views/discuss.xml',
    ],
}
