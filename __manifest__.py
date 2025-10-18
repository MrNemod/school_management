{
    'name': 'School Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'School management',
    'author': 'Luis Garcia',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}