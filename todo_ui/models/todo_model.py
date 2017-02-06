# -*- coding: utf-8 -*-
# @ 2016 Elico Corp (https://www.elico-corp.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
from openerp import fields, models, api


class Tag(models.Model):
    _name = 'todo.task.tag'
    _parent_store = True

    name = fields.Char(string='Name', size=40, tanslate=True)
    task_ids = fields.Many2many(
        comodel_name='todo.task',
        string='Tasks')
    parent_id = fields.Many2one(
        comodel_name='todo.task.tag',
        string='Parent Tag',
        ondelete='restrict')
    parent_left = fields.Integer(
        string='Parent Left',
        index=True)
    parent_right = fields.Integer(
        string='Parent Right',
        index=True)


class Stage(models.Model):
    _name = 'todo.task.stage'
    _order = 'sequence, name'

    # String fields:
    name = fields.Char(string='Name', size=40, translate=True)
    desc = fields.Text(string='Description')
    state = fields.Selection(
        [('draft', 'New'), ('open', 'Started'), ('done', 'Closed')],
        'State',
        default='draft')
    docs = fields.Html(string='Documentation')

    # Numeric fields:
    sequence = fields.Integer(string='Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))  # float precision - (total, decimals)

    #Date fields:
    date_effective = fields.Date(string='Effective Date')
    date_changed = fields.Date(string='Last Changed')

    #Other fields:
    fold = fields.Boolean(string='Folded?')
    image = fields.Binary(string='Image')

    # Stage class relateion with Tasks:
    tasks = fields.One2many(
        comodel_name='todo.task', #related model
        inverse_name='stage_id',  #field for "this" on related model
        string='Tasks in this stage')


class TodoTask(models.Model):
    _inherit = 'todo.task'

    stage_id = fields.Many2one(
        comodel_name='todo.task.stage',
        string='Stage')
    tag_ids = fields.Many2many(
        comodel_name='todo.task.tag',
        string='Tags')