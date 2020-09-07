from odoo import api, fields, models, _


class enfermedades(models.Model):
   _name = "mediges.enfermedades"

   name = fields.Char(string="Nombre", required=True)