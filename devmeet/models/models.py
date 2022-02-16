# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re



class desarrollador(models.Model):
     _name = 'devmeet.desarrollador'
     _description = 'devmeet.desarrollador'

     dni = fields.Char(string="DNI",readonly=False, required=True,help='Este es el DNI')
     name = fields.Char(string="Nombre",readonly=False, required=True,help='Este es el nombre')
     surname = fields.Char(string="Apellidos",readonly=False, required=True,help='Estos son los apellidos')
     age=fields.Integer()
     photo =fields.Image(max_width=200, max_height=200)
     tecnologias_trabajadas=fields.Many2many(comodel_name="devmeet.tecnologia", relation="tecnologias_desarrollador", column1="desarrollador_id", column2="tecnologia_id")
     tecnologias_interes=fields.Many2many(comodel_name="devmeet.tecnologia", relation="tecnologias_desarrollador", column1="desarrollador_id", column2="tecnologia_id")
     eventos=fields.Many2many(comodel_name="devmeet.evento", relation="desarrolladores_evento", column1="desarrollador_id", column2="evento_id")

     @api.constrains('dni')
     def _check_dni(self):
          regex=re.compile('[0-9]{8}[a-z]\Z',re.I)
          for desarrollador in self:
               if regex.match(desarrollador.dni):
                    _logger.info('El DNI fue correcto')
               else:
                    raise ValidationError("El formato de DNI no es correcto")

     _sql_constraints=[('dni_uniq', 'unique('dni')', 'DNI can´t be repeated')]

class tecnologia(models.Model):
     _name = 'devmeet.tecnologia'
     _description = 'Las Tecnologias'

     name = fields.Char(string="Nombre Tecnologia",readonly=False, required=True,help='Este es el nombre de la tecnologia')
     web = fields.Char(string="Web Oficial",readonly=False, required=True,help='Esta es la web oficial')
     logo =fields.Image(max_width=200, max_height=200)
     eventos=fields.Many2many(comodel_name="devmeet.evento", relation="tecnologias_evento", column1="tecnologia_id", column2="evento_id")
     desarrolladores=fields.Many2many(comodel_name="devmeet.desarrollador", relation="tecnologias_desarrollador", column1="tecnologia_id", column2="desarrollador_id")

class evento(models.Model):
     _name = 'devmeet.evento'
     _description = 'Los Eventos'

     name = fields.Char(string="Ponente",readonly=False, required=True,help='Este es el nombre del ponente')
     tecnologias=fields.Many2many(comodel_name="devmeet.tecnologia", relation="tecnologias_evento", column1="evento_id", column2="tecnologia_id")
     desarrolladores=fields.Many2many(comodel_name="devmeet.desarrollador", relation="desarrolladores_evento", column1="evento_id", column2="desarrollador_id")
     fecha_inicio=fields.Date()
     fecha_fin=fields.Date() #funcion para que tenga que ser mayor que la de inicio
#     modalidades

     @api.constrains('fecha_fin')
     def _check_fechafin(self):
          for evento in self:
               if evento.fecha_fin<evento.fecha_inicio:
                    raise ValidationError("El fin del evento no puede ser anterior a su inicio")
               else:
                    pass


