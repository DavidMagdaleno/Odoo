# -*- coding: utf-8 -*-
# from odoo import http


# class Devmeet(http.Controller):
#     @http.route('/devmeet/devmeet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/devmeet/devmeet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('devmeet.listing', {
#             'root': '/devmeet/devmeet',
#             'objects': http.request.env['devmeet.devmeet'].search([]),
#         })

#     @http.route('/devmeet/devmeet/objects/<model("devmeet.devmeet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('devmeet.object', {
#             'object': obj
#         })
