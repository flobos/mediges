from odoo import api, fields, models, _


class indicadores_fisicos(models.Model):
   _name = "mediges.indicadores_fisicos"

   name = fields.Char(string="Nombre", required=True)