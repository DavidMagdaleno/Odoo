# -*- coding: utf-8 -*-

from odoo import models, fields, api

class student(models.Model):
     _name = 'school.student'
     _description = 'school.student'

     name = fields.Char(string="Nombre", readonly=False, required=True,help='Este es el nombre')
     birth_year=fields.Integer()
     description =fields.Text()
     inscription_date=fields.Date()
     last_login=fields.Datetime()
     is_student=fields.Boolean()
     photo =fields.Image(max_width=200, max_height=200)
     classroom=fields.Many2one("school.classroom")

class classroom(models.Model):
     _name='school.classroom'
     _description='school.classroom' #Las Clases

     name=fields.Char()
     students=fields.One2many("school.student",'classroom')

# class school(models.Model):
#     _name = 'school.school'
#     _description = 'school.school'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
