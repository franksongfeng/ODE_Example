# -*- coding: utf-8 -*-
# @ 2016 Elico Corp (https://www.elico-corp.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
from openerp import fields, models, api
from openerp.exceptions import ValidationError

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
    child_ids = fields.One2many(
        comodel_name='todo.task.tag',
        inverse_name='parent_id',
        string='Child Tags')

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
    stage_state = fields.Selection(
        related='stage_id.state',
        string='Stage State')
    stage_fold = fields.Boolean(
        'Stage Folded?',
        compute='_compute_stage_fold',
        search='_search_stage_fold',
        inverse='_write_stage_fold')

    # Referencing fields
    refers_to = fields.Reference(
        [('res.user', 'User'), ('res.partner', 'Partner')],
        'Refers to')

    # Smart buttons
    user_todo_count = fields.Integer(
        'User To-Do Count',
        compute='compute_user_todo_count')

    @api.one
    def compute_user_todo_count(self):
        import pdb
        pdb.set_trace()
        self.user_todo_count = self.search_count(
            [('user_id', '=', self.user_id.id)])

    @api.one
    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        self.stage_fold = self.stage_id.fold

    def _search_stage_fold(self, operator, value):
        return [('stage_id.fold', operator, value)]

    def _write_stage_fold(self):
        self.stage_id.fold = self.stage_fold

    @api.one
    @api.constrains('name')
    def _check_name_size(self):
        import pdb
        pdb.set_trace()
        if len(self.name) < 5:
            raise ValidationError('Must have 5 chars!')

    _sql_constraints = [
        (
            'todo_task_name_uniq',
            'UNIQUE (name, user_id, active)',
            'Task title must be unique!'
        )
    ]
