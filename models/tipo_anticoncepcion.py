from odoo import api, fields, models, _


class tipo_anticoncepcion(models.Model):
   _name = "mediges.tipo_anticoncepcion"

   name = fields.Char(string="Nombre", required=True)