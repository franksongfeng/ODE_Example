{
    'name': 'Multiuser To-Do',
    'description': 'Extend the To-Do app to multiusesr.',
    'category': 'Test',
    'summary': 'Example in the book ODE',
    'version': '9.0.2.0.1',
    'website': 'www.elico-corp.com',
    'author': 'Frank Song',
    'depends': [
        'todo_app',
    ],
    'data': [
        'todo_view.xml',
        'security/todo_access_rules.xml',
        'todo_data.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}

