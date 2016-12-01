from openerp import models, fields

class sale_order_improvements(models.Model):
    _inherit = 'sale.order'
    
    partner_invoice_id = fields.Many2one('res.partner', readonly=False)
    attachments_ids = fields.Many2many('ir.attachment', string="Attachments")
    header_text = fields.Html(string="Optional header text")
    note = fields.Html("Terms and conditions")