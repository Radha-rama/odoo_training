{
'name' : 'LeaseProperty',
    'version': '1.0',
    'category': 'Sales/Lease',
    'summary': 'Lease property',
    'depends': [
        'Estate',
    ],
    'data': [
      'security/ir.model.access.csv',
      'views/lease_views.xml', 
    ],
    'installable': False,
    'application': True,
    'auto_install': False,
    'license' : 'LGPL-3', 
}