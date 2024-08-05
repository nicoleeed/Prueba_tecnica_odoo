# -*- coding: utf-8 -*-
{
    'name': "Personalización de Punto de Venta",

    'summary': """
        Módulo personalizado de Punto de Venta""",

    'author': 'Nicole Durand Zeballos',
	'website': "www.linkedin.com/in/nicole-alexia-durand-zeballos-46b231284",
    
    'license': 'Other proprietary',

    'category': 'Other',
    'version': '17.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'point_of_sale',],

    # always loaded
    'data': [
    ],
    
    'assets': {
        'point_of_sale.assets_prod': [
            'Ajustes_point_of_sale/static/src/overrides/components/partner_list/partner_line/partner_line.xml',
            'Ajustes_point_of_sale/static/src/overrides/components/partner_list/partner_list.xml',
            
            'Ajustes_point_of_sale/static/src/overrides/components/payment_screen/payment_screen.js',
            'Ajustes_point_of_sale/static/src/overrides/components/payment_screen/payment_screen.xml',
            
            'Ajustes_point_of_sale/static/src/overrides/pos_store.js'
        ],
    },

    'application': False,
    'installable': True,
    'auto_install': True,
}

