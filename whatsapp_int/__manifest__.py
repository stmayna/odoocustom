# -*- coding: utf-8 -*-
{
    'name': "Whatsapp Integration",

    'summary': """
        Testing whatsapp integration purpose.
        """,

    'description': """
        Development stage.
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
        'base',
        'web',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/whatsapp_int.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'application': True,
    'license': "LGPL-3",
    'images': ['statics/whatsapp.png'],
}
