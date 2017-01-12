# -*- coding: utf-8 -*-
# @ 2016 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']

    user_id =fields.Many2one(
        comodel_name='res.users',
        string='Responsible'
    )
    date_deadline=fields.Date(
        string='Deadline'
    )
    name = fields.Char(
        help="What needs to be done?"
    )

    @api.multi
    def do_clear_done(self):
        import pdb
        pdb.set_trace()
        domain = [
            '&',
            ('is_done', '=', True),
            '|',
            ('user_id', '=', self.env.uid),
            ('user_id', '=', False)
        ]
        done_recs = self.search(domain)
        if done_recs:
            done_recs.write({'active': False})
            return True
        else:
            return False

    @api.one
    def do_toggle_done(self):
        if self.user_id != self.env.user:
            raise Exception('Only the responsible can do this!')
        else:
            return super(TodoTask, self).do_toggle_done()