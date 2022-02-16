# -*- coding: utf-8 -*-

from odoo import models, fields, api
import secrets
#excepcion  warning
#from odoo import _
#falta una ----------------------------------------
#para log
import logging
_logger= logging.getLogger(__name__)

class student(models.Model):
     _name = 'school.student'
     _description = 'school.student'

     name = fields.Char(string="Nombre", readonly=False, required=True,help='Este es el nombre')
     birth_year=fields.Integer()
     #campos calculados se calculara con un metodo
     password =fields.Char(compute="_get_password", store=True)#store solo para se calcule una vez

     description =fields.Text()
     inscription_date=fields.Date()
     last_login=fields.Datetime()
     is_student=fields.Boolean()
     photo =fields.Image(max_width=200, max_height=200)
     classroom=fields.Many2one("school.classroom", ondelete='set null', help='Clase a la que pertenece')
     teachers=fields.Many2many("school.teacher",related="classroom.teachers", readonly=True)
     #coordinador de clase
     
     
     @api.depends("name")#solo cuando cambie el nombre se genera una nueva pass
     #@api.one para que envie un elemento si no envia una lista
     def _get_password(self):
          for student in self:
               student.password= secrets.token_urlsafe(12)
               #truco para saber pruebas
               #print('\033[94m',student,'\033[0m')
               #para lanzar un warning
               #raise Warning(_("Se ha producido un warning"))
               #para crear un log -- es el bueno
               _logger.debug('\033[94m'+str(student)+'\033[0m')#warning



class classroom(models.Model):
     _name='school.classroom'
     _description='Las Clases' #Las Clases

     name=fields.Char()
     students=fields.One2many(string='Alumnos', comodel_name="school.student",inverse_name='classroom')
     teachers=fields.Many2many(comodel_name="school.teacher", relation="teachers_classroom", column1="classroom_id", column2="teacher_id")
     #mas campos calculados
     all_teachers=fields.Many2many("school.teacher",compute="_get_allteachers")
     
     #coordinador de clase (1clase->1Pr, 1PR->*clases)
     coordinador= Many2one("school.teacher", compute="_get_coordinador")

     def _get_coordinador(self):
          #llega una lista clases
          for classroom in self:
               if len(classroom.teachers)>0:
                    classroom.coordinador=classroom.teachers[0].id
     
     def _get_allteachers(self):
          for classroom in self:
               if len(classroom.teachers)>0:
                    classroom.all_teachers=classroom.teachers + classroom.teachers_last_year


class teacher(models.Model):
     _name='school.teacher'
     _description='Los Profesores' #Las Clases

     name=fields.Char()
     classrooms=fields.Many2many(comodel_name="school.classroom",relation="teachers_classroom",column1="teacher_id", column2="classroom_id")

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
