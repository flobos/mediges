from odoo import api, fields, models, _


class signos_vitales(models.Model):
   _name = "mediges.signos_vitales"

   tipo_signo_vital = fields.Many2one('mediges.tipo_signo_vital', string="Signo Vital", required=True)
   valor = fields.Float(string="Valor", required=True)
   visitas_id = fields.Many2one('mediges.visitas', string="Visitas")