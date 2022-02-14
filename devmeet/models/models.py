# -*- coding: utf-8 -*-

from odoo import models, fields, api

#impor excepcion warning


class desarrollador(models.Model):
     _name = 'devmeet.desarrollador'
     _description = 'devmeet.desarrollador'

     dni = fields.Char(string="DNI",readonly=False, required=True,help='Este es el DNI')
     name = fields.Char(string="Nombre",readonly=False, required=True,help='Este es el nombre')
     surname = fields.Char(string="Apellidos",readonly=False, required=True,help='Estos son los apellidos')
     age=fields.Integer()
     photo =fields.Image(max_width=200, max_height=200)


class tecnologia(models.Model):
     _name = 'devmeet.tecnologia'
     _description = 'Las Tecnologias'

     name = fields.Char(string="Nombre Tecnologia",readonly=False, required=True,help='Este es el nombre de la tecnologia')
     web = fields.Char(string="Web Oficial",readonly=False, required=True,help='Esta es la web oficial')
     logo =fields.Image(max_width=200, max_height=200)

class evento(models.Model):
     _name = 'devmeet.evento'
     _description = 'Los Eventos'

     ponente = fields.Char(string="Ponente",readonly=False, required=True,help='Este es el nombre del ponente')
#     tecnologias
     fecha_inicio=fields.Date()
     fecha_fin=fields.Date() #funcion para que tenga que ser mayor que la de inicio
#     modalidades

#     compute="_value_fecha"
#     @api.depends('fecha_inicio')
#     def _value_fecha(self):
#         if fecha_fin<fecha_inicio:
#                raise Warning("La fecha de fin es mayor o igual que la fecha de inicio")

