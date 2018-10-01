
from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo import exceptions, _


class pacientes(models.Model):

    _inherit = 'res.partner'
    antecedentes_medicos = fields.Text(string="Antecedentes Medicos")
    rut = fields.Char(String="Rut", required=True)
    numero_celular = fields.Char(string="Celular", required=True )
    fecha_nacimiento = fields.Date(string="Fecha Nacimiento")


