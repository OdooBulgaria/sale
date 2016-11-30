{
    'name': "Confirmation date on Sale Order",
    'version': '9.0.1.0.0',
    'depends': ['sale'],
    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sale',
    'description': """
It adds a date field on Sale Orders that is set with the date of the order confirmation.

It should be already present from Odoo original, but not working for us

This module has been developed by Valentin THIRION @ AbAKUS it-solutions""",
    'data': [
        'views/sale_order_view.xml',
    ],
}