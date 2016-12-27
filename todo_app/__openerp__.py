# -*- coding: utf-8 -*-
#   2016 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'To-Do Application',
    'category': 'Test',
    'summary': 'Example in the book ODE',
    'version': '9.0.1.0.0',
    'website': 'www.elico-corp.com',
    'author': 'Frank Song',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'views/todo_view.xml',
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
    ],
    'images': [],
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
}
