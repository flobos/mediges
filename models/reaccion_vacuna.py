from odoo import api, fields, models, _

class reaccion_vacunacion(models.Model):
    _name = "mediges.reaccion_vacunacion"

    name = fields.Char(string="reacciones adversas", required=True)