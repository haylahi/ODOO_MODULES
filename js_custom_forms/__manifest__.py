{
    "name": "JS Custom Forms",
    "summary": "Cambios genéricos en plantilla Clarico y otras personalizaciones",
    "version": "1.0",
    "license": "AGPL-3",
    "author": "Jim Sports",
    "category": "Uncategorized",
    "website": "https://jimsports.com",
    'data': [
        'data/ir_model_data.xml',
        'views/shop_address.xml',
        'views/default_contact_form.xml',
        'views/web_product.xml',
        'views/custom_generic_css.xml',
        'views/clarico_product_compare.xml',
        'views/clarico_wishlist.xml',
        'views/filter_sort_by.xml',
        'views/cart.xml',
        'views/res_partner_form.xml',
        'views/web_shop.xml',
        # 'views/devoluciones.xml',
    ],
    'category': 'Website',
    'depends': ['website', 'website_sale', 'clarico_product',  'clarico_compare',  'clarico_shop'],
}
