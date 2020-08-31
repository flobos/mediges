from odoo import api, fields, models, _


class demografia(models.Model):
   _name = "mediges.demografia"

   name = fields.Char(string="Diagnostico", required=True)