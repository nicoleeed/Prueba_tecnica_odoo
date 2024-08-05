# -*- coding: utf-8 -*-
{
    'name': "Personalización de Facturación",

    'summary': """
        Módulo personalizado de Facturación""",

    'author': 'Nicole Durand Zeballos',
	'website': "www.linkedin.com/in/nicole-alexia-durand-zeballos-46b231284",
    
    'license': 'Other proprietary',

    'category': 'Other',
    'version': '17.0',
    # any module necessary for this one to work correctly
    'depends': ['base',
                'account',
                'sale',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sale_channel_data.xml',
        'views/account_move_views.xml',
        'views/invoice_report.xml',
    ],

    'application': False,
    'installable': True,
    'auto_install': True,
}

