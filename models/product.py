
from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo import exceptions, _


class produtos_medicos(models.Model):

    _inherit = 'product.product'
    es_tipo_medico = fields.Binary(string="Tipo Medico")


