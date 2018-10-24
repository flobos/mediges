from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo import exceptions, _

class prescricion(models.Model):
    _name = "mediges.prescricion"
    _order = 'id'

    medicamento_id = fields.Many2one('product.product', string="Medicamento", required=True)
    cantidad = fields.Integer(string="Cantidad", required=True)
    tipo_unidad = fields.Many2one('product.uom', string="Tipo unidad", required=True)
    periodo = fields.Many2one('mediges.periodo', string="Cada", required=True)
    hora_medica_id = fields.Many2one('mediges.horasmedicas', string="Hora Medica")
    observacion = fields.Char(string="Observacion")




class periodo(models.Model):
    _name = "mediges.periodo"
    _order = 'id'

    name = fields.Char(string="Nombre", required=True)
