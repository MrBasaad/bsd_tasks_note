{
    'name': 'Tasks',
    'version': '19.0.1.0.0',
    'summary': 'This Model for daily tasks recorder',
    'description': 'This app will create and update and delete your tasks and make it more easy to management you goals ',
    'category': 'Services',
    'author': 'Basaad.co',
    'website': 'https://github.com/MrBasaad',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/bsd_base_view.xml',
        'views/bsd_list_view.xml',
        'views/bsd_form_view.xml',
        
    ],
    # 'demo': [],
    # 'assets':{
    #     'web.assets_frontend':[],
    # },
    'installable': True,
    'application': True,
    'auto_install': False,
}