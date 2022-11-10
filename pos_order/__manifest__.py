{
    'name': "new order add",
    'author': "Htet Arkar Kyaw",
    'maintainer': "Htet Arkar Kyaw",
    'category': 'Point of Sale',
    'version': '15.0.1.0.0',
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'web.assets_backend': [
            'pos_order/static/src/js/button.js',
        ],
        'web.assets_qweb': [
            'pos_order/static/src/xml/order.xml', 
           # 'pos_order/static/src/xml/history.xml',
            #'pos_order/static/src/js/inher_button.js',
        ],

        'point_of_sale.assets': ['pos_order/static/src/css/pos.css']
    },
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,

}
