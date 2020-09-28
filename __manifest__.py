# -*- coding: utf-8 -*-
{
    'name': "Hostel",

    'summary': """
        Manage your hostel the easier and smarter way""",

    'description': """
        This business application enables hostel wardens to 
        -Identify and keep students records in the hostel
        -Sort out students who have paid and those who have not paid 
        hostel residence fees
        - manage hostel hygiene and maintainance 
    """,

    'author': "Kaiza Ilomo",
    'company': "Kunonu Technologies Co.Ltd",
    'website': "https://www.kunonu.tech",
    'support': "Kunonu Technologies Co.Ltd",
    'maintainer': "Kunonu Technologies Co.Ltd",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'CRM',
    'version': '13.0.1.0.0',
    'sequence': 1,
    'license': 'GPL-2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/templates.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],

    'images': [],

    'application': True,
    'installable': True,
    'auto_install': False,
}
