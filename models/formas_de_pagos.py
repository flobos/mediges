from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo import exceptions, _


class formas_de_pagos(models.Model):
    _name = "mediges.formas_de_pagos"

    name = fields.Char(string="Forma de Pago", required=True)