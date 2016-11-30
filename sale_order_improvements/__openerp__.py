{
    'name': "Sale order improvements",
    'version': '9.0.1.1.1',
    'depends': ['sale'],
    'author': "AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sale',
    'description': 
    """Sale order improvements.

    - It set the current date to the order date of quotations or sales orders.
    - Invoice Address is alterable after sale order confirmation.
    - New field special condition. Will be included at the end of the quotation report.
    - Attachment field in Quotations and Sale Orders
    - It creates a field 'header_html' that will be used with a WYSIWYG and printed on SO reports
    - It inherits the Quotation/SO report to improve

This module has been developed by AbAKUS it-solution.
    """,
    'data': [
        'views/report_saleorder.xml',
        'views/sale_order_view.xml',
        'security/ir.model.access.csv',
    ],
}
