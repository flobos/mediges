from odoo import api, fields, models, _


class tipo_visitas(models.Model):
    _name = "mediges.tipo_visita"
    _order = 'id'

    name = fields.Char(string="Tipo Vista", required=True)