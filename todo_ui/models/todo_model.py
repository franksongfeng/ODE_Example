# -*- coding: utf-8 -*-
# @ 2016 Elico Corp (https://www.elico-corp.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
from openerp import fields, models, api


class Tag(models.Model):
    _name = 'todo.task.tag'

    name = fields.Char(string='Name', size=40, tanslate=True)


class Stage(models.Model):
    _name = 'todo.task.stage'
    _order = 'sequence, name'
    _rec_name = 'name'  # the default
    _table = 'todo_task_stage'  # the default

    name = fields.Char(string='Name', size=40, translate=True)
    sequence = fields.Integer(string='Sequence')
