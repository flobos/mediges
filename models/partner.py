
from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo import exceptions, _


class pacientes(models.Model):

    _inherit = 'res.partner'
    antecedentes_medicos = fields.Text(string="Antecedentes Medicos")
    fecha_nacimiento = fields.Date(string="Fecha Nacimiento", required=True)
    edad = fields.Integer(string="Edad",  readonly=True )
    horasmedicas_id = fields.One2many('mediges.horasmedicas', 'paciente', string='Visitas Medicas')

    @api.depends('horasmedicas_id.historial')
    def _calcula_total_pagos_docs(self):
           v_historial = ''
           for horas in self:
               v_historial = horas.historial

               horas.update({
               'antecedentes_medicos': v_historial
                })

    @api.onchange('fecha_nacimiento')
    def calculate_age(self):
        today = date.today()
        nacio = fields.Datetime.from_string(self.fecha_nacimiento)
        v_fecha =  today.year - nacio.year - ((today.month, today.day) < (nacio.month, nacio.day))
        self.edad = v_fecha