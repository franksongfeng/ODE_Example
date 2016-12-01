# -*- coding: utf-8 -*-
#   2016 Elico Corp (https://www.elico-corp.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
from openerp import fields, models


class TodoTask(models.Model):
    _name = 'todo.task'

    name = fields.Char(string='Description', required=True, size=64)
    is_done = fields.Boolean(string='Done?')
    active = fields.Boolean(string='Active?', default=True)
