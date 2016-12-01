{
    'name': "Sale order improvements",
    'version': '9.0.1.1.1',
    'depends': ['sale'],
    'author': "AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sale',
    'description': 
    """Sale order improvements.

    - Invoice Address is alterable after sale order confirmation.
    - Attachment field in Quotations and Sale Orders
    - It creates a field 'header_html' that will be used with a WYSIWYG and printed on SO reports
    - It inherits the Quotation/SO report to improve

This module has been developed by AbAKUS it-solution.
    """,
    'data': [
        'views/sale_order_view.xml',
        'reports/sale_order_report.xml',
    ],
}
