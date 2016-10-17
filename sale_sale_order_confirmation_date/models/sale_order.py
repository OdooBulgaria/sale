# -*- coding: utf-8 -*-

from openerp import models, fields, api

class sale_order_confirmation_date(models.Model):
    _inherit = 'sale.order'

    # basically copy of Odoo's original 'sale' module
    confirmation_date = fields.Datetime(string='Confirmation Date', readonly=True, index=True, help="Date on which the sale order is confirmed.", oldname="date_confirm")

    # basically copy of Odoo's original 'sale' module
    @api.multi
    def action_confirm(self):
        for order in self:
            order.state = 'sale'
            order.confirmation_date = fields.Datetime.now()
            if self.env.context.get('send_email'):
                self.force_quotation_send()
            order.order_line._action_procurement_create()
        if self.env['ir.values'].get_default('sale.config.settings', 'auto_done_setting'):
            self.action_done()
        return True
