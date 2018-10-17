
from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo import exceptions, _
from dateutil.relativedelta import relativedelta


class pacientes(models.Model):

    _inherit = 'res.partner'
    antecedentes_medicos = fields.Text(string="Antecedentes Medicos")
    fecha_nacimiento = fields.Date(string="Fecha Nacimiento", required=True)
    edad = fields.Integer(string="Edad",  readonly=True , compute='_calcula_edad')
    horasmedicas_id = fields.One2many('mediges.horasmedicas', 'paciente', string='Visitas Medicas')
    visitas_contador = fields.Integer(string="Cantidad de Visitas", readonly=True,store=True ,compute='_calcula_cantidad_visitas')

    @api.depends('horasmedicas_id.historial')
    def _calcula_total_pagos_docs(self):
           v_historial = ''
           for horas in self:
               v_historial = horas.historial

               horas.update({
               'antecedentes_medicos': v_historial
                })

    @api.depends('horasmedicas_id')
    def _calcula_cantidad_visitas(self):
        v_visitas = 0
        for visitas in self:
            v_visitas = len(visitas.horasmedicas_id)

            visitas.update({
                'visitas_contador': v_visitas
            })

    @api.multi
    @api.depends('fecha_nacimiento')
    def _calcula_edad(self):
        hoy = date.today()
        for record in self:
            age = []
            v_fecha = fields.Date.from_string(record.fecha_nacimiento)
            gap = relativedelta(hoy, v_fecha)
            if gap.years > 0:
                record.edad = gap.years