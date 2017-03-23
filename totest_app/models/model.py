# -*- coding: utf-8 -*-
from openerp import models, fields, api


class TotestTask(models.Model):
    _name = 'totest.task'
    _description = 'To-Test-Task'
    name = fields.Char(string='Description', required=True, size=64)
    is_done = fields.Boolean(string='Done?')
    active = fields.Boolean(string='Active?', default=True)
    number = fields.Integer(string='No.')

    @api.one
    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True

    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True
