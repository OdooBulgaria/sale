from openerp import models, fields

class sale_order_special_condition(models.Model):
    _name = 'sale.order.special.condition'

    name = fields.Char(string="Name")