
{
    'name'           : "Total number of Products and Quantity on Invoices",
    'category'       : 'Account',
    'summary'        : """Display total number of Products and Quantity on Invoices""",
    'author':           'Odoo Circle',
    'website':          'https://odoocircle.com',
    'description'    : """""",
    'version'        : '19.0.0.1',
    'depends'        : ['base','account'],
    'data'           : [
                         'security/account_invoice_security.xml',
                         'views/account_invoice_view.xml',
                         'report/account_invoice_report_templates.xml',
                         'views/account_report_view.xml'],
    'images'         : ['static/description/banner.jpg'],
    'license'        : 'AGPL-3',
    'installable'    : True,
    'application'    : True,
    'auto_install'   : False,
}
