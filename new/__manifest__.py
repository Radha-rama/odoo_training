{
    'name': 'RealEstate',
    'version': '1.0',
    'category' : 'Estate',
    'summary': 'Estate',
    'depends': ['base','account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/estate_security.xml',
        'views/estate_menus.xml',
        'wizard/create_sold_invoice_views.xml',
        'views/estate_property_views.xml',
        'views/property_Type_views.xml',
        'views/estate_template.xml',
        'data/data.xml',
    ],
    'depends':
     [
        'website'
     ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license' : 'LGPL-3', 
}