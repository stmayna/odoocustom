# -*- coding: utf-8 -*-
{
    'name': "Prager Dashboard Report",

    'summary': """
        For Maintenance Purpose""",

    'description': """
        Dashboard Report.
    """,

    'author': "twitter.com/thepythoncode",
    'website': "http://www.hitconsulting.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Maintenance',
    'version': '0.1',
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'depends': ['maintenance', 'stock'],

    # always loaded
    # make sure the menu view is on the last
    'data': [
        'security/ir.model.access.csv',
        'views/prager_maintenance_views.xml',
        # 'views/hit_condition_monitoring_views.xml',
    ],
}
