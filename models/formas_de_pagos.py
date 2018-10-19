from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo import exceptions, _


class formas_de_pagos(models.Model):
    _name = "mediges.formas_de_pagos"
    _order = 'company_id, name'

    company_id = fields.Many2one('res.company', string="Doctor o Lab.", required=True, readonly=True,
                              default=lambda self: self.env['res.company']._company_default_get('account.invoice'))
    tipo_prestacion = fields.Many2one('product.product', string="Prestación", required=True)
    name = fields.Char(string="Forma de Pago", required=True)
    valor = fields.Integer(string="Valor", required=True)


