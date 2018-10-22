
from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError, AccessError
from odoo import exceptions, _
from dateutil.relativedelta import relativedelta
from itertools import cycle


class pacientes(models.Model):

    _inherit = 'res.partner'


    antecedentes_medicos = fields.Text(string="Antecedentes Medicos")
    fecha_nacimiento = fields.Date(string="Fecha Nacimiento", required=True)
    edad = fields.Integer(string="Edad",  readonly=True , compute='_calcula_edad')
    horasmedicas_id = fields.One2many('mediges.horasmedicas', 'paciente', string='Visitas Medicas')
    visitas_contador = fields.Integer(string="Cantidad de Visitas", readonly=True,store=True ,compute='_calcula_cantidad_visitas')
    rut = fields.Char(string="Rut", required=True)

    _sql_constraints = [
        ('rut_unico', 'unique(rut)', 'Este RUT ya esta registrado ... !'),
    ]


    @api.multi
    @api.onchange('rut')
    def validarRut(self):
      if self.rut != False:
            rut = self.rut
            rut = rut.upper();
            rut = rut.replace("-", "")
            rut = rut.replace(".", "")
            aux = rut[:-1]
            dv = rut[-1:]

            revertido = map(int, reversed(str(aux)))
            factors = cycle(range(2, 8))
            s = sum(d * f for d, f in zip(revertido, factors))
            res = (-s) % 11

            if str(res) == dv:
               True
            elif dv == "K" and res == 10:
                True
            else:
                raise ValidationError(_('Rut Invalido'))




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