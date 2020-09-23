from odoo import api, fields, models, _

class sitio_vacunacion(models.Model):
    _name = "mediges.sitio_vacunacion"

    name = fields.Char(string="Sitio Vacunacion", required=True)