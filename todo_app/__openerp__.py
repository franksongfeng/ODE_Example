# -*- coding: utf-8 -*-
#   2016 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'To-Do Application',
    'category': 'Test',
    'summary': 'Todo-Application',
    'version': '6.1.8',
    'website': 'www.elico-corp.com',
    'author': 'Frank Song',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'views/todo_view.xml',
        'security/ir.model.access.csv',
    ],
    'images': [],
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
}
