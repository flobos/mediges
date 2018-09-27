# -*- coding: utf-8 -*-
from odoo import http

# class Mediges(http.Controller):
#     @http.route('/mediges/mediges/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mediges/mediges/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mediges.listing', {
#             'root': '/mediges/mediges',
#             'objects': http.request.env['mediges.mediges'].search([]),
#         })

#     @http.route('/mediges/mediges/objects/<model("mediges.mediges"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mediges.object', {
#             'object': obj
#         })