from odoo import api, fields, models, _


class tipo_signo_vital(models.Model):
   _name = "mediges.tipo_signo_vital"

   name = fields.Char(string="Nombre", required=True)
