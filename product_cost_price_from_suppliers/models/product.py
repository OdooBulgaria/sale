from openerp import models, fields, api, _
from openerp.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class product_template_with_cost_price_auto(models.Model):
    _inherit = ['product.template']

    cost_price_from_suppliers = fields.Boolean('Auto cost from suppliers', default=True)
    standard_price = fields.Float('Cost Price', compute='_compute_lowest_supplier_price')
    manual_cost_price = fields.Float('Manual cost price', default=0)

    @api.multi
    @api.depends('cost_price_from_suppliers', 'seller_ids', 'manual_cost_price')
    def _compute_lowest_supplier_price(self):
        for product in self:
            if product.cost_price_from_suppliers == True:
                # Get the lowest price for suppliers
                min_price = 0
                for supp in product.seller_ids:
                    if (min_price == 0 and supp.price > 0) or (supp.state == 'sellable' and supp.price < min_price):
                        min_price = supp.price

                product.standard_price = min_price
                _logger.debug("%s | PT : Price computed regarded supplier (%s)", product.id, product.standard_price)
            else:
                product.standard_price = product.manual_cost_price
                _logger.debug("%s | PT : Price computed manually (%s)", product.id, product.standard_price)

            # Set the flag on the child products
            for variant in product.product_variant_ids:
                variant.write({'standard_price': product.standard_price})
                variant.standard_price = product.standard_price

class product_product_with_cost_price_auto(models.Model):
    _inherit = ['product.product']

    #cost_price_from_suppliers = fields.Boolean('Auto cost from suppliers', related="product_tmpl_id.cost_price_from_suppliers")
    standard_price = fields.Float('Cost Price', compute='_compute_standard_price')
    #manual_cost_price = fields.Float('Manual cost price', related="product_tmpl_id.manual_cost_price") #default=0)

    @api.multi
    @api.depends('product_tmpl_id')
    def _compute_standard_price(self):
        for product in self:
            _logger.debug("%s Compute price for %s", product.name)
            product.standard_price = product.product_tmpl_id.standard_price

    @api.multi
    def open_product_template(self):
        if self.product_tmpl_id:
            return {
                'type': 'ir.actions.act_window',
                'name': 'product.product_template_only_form_view',
                'res_model': 'product.template',
                'res_id': self.product_tmpl_id.id ,
                'view_type': 'form',
                'view_mode': 'form',
                }
