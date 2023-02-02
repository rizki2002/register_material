# -*- coding: utf-8 -*-
from odoo import http

# class Testing(http.Controller):
#     @http.route('/testing/testing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testing/testing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testing.listing', {
#             'root': '/testing/testing',
#             'objects': http.request.env['testing.testing'].search([]),
#         })

#     @http.route('/testing/testing/objects/<model("testing.testing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testing.object', {
#             'object': obj
#         })