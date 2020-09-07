# -*- coding: utf-8 -*-
{
    'name': "Mediges",

    'summary': """
        Gestion Medica""",

    'description': """
        Gestion Medica
    """,

    'author': "Fernando Lobos",
    'website': "http://www.tig.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','sale'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product.xml',
        'views/partner.xml',
        'views/horasmedicas.xml',
        'views/formas_de_pagos.xml',
        'views/visitas.xml',
        'views/demografia.xml',
        'views/signos_vitales.xml',
        'views/tipo_signo_vital.xml',
        'views/tipo_anticoncepcion.xml',
        'views/anticoncepcion.xml',
        'views/enfermedades.xml',
        'views/visitas_enfermedades.xml',
        'views/menus.xml',
        'data/product.category.xml',
        'data/ir.sequence.xml',
        'data/ir.default.xml',
        'data/res.country.state.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}