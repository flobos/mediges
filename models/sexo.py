from odoo import api, fields, models, _



class formas_de_pagos(models.Model):
    _name = "mediges.sexo"

    name = fields.Char(string="Sexo", required=True)
