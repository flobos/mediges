from odoo import api, fields, models, _


class visitas_enfermedades(models.Model):
    _name = "mediges.visitas_enfermedades"

    enfermedades_id = fields.Many2one('mediges.enfermedades', string="Enfermedad", required=True)
    visitas_id = fields.Many2one('mediges.visitas')
    ano = fields.Float(string="Año")
    tratamiento = fields.Char(string="Tratamiento")
    tratamiento_inicio = fields.Datetime(String="Desde cuando")
