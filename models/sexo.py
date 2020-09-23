from odoo import api, fields, models, _

class sexo(models.Model):
    _name = "mediges.sexo"

    name = fields.Char(string="Sexo", required=True)
