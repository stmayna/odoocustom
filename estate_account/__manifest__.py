# -*- coding: utf-8 -*-
{
    'name': "Real Estate Accounting",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Yumi",
    'website': "https://twitter.com/thepythoncode",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Real Estate/Brokerage',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'estate',
        'account',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/estate_account.xml',
        # 'views/views_type.xml',
        # 'views/views_tags.xml',
        # 'views/views_offer.xml',
        # "views/views_res_users.xml",
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'application': True,
    'license': "LGPL-3",
}
