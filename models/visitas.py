from odoo import api, fields, models, _


class visitas(models.Model):
    _name = "mediges.visitas"

    @api.model
    def default_get(self, fields):
        res = super(visitas, self).default_get(fields)
        lista_signos_vitales = []
        record_signos_vitales = self.env['mediges.tipo_signo_vital'].search([])
        print(record_signos_vitales)
        for record in record_signos_vitales:
            lista = (0 ,0 ,{
                'tipo_signo_vital': record.id,
                'valor': 0
            })
            lista_signos_vitales.append(lista)
        res.update({
            'signos_vitales_id': lista_signos_vitales
        })
        return res



    paciente = fields.Many2one('res.partner', string="Paciente", required=True)
    consentimiento = fields.Selection([('true','Si'),('false','No')]
                                      ,'Se realiza proceso de Consentimiento informado, anexo 1',required=True)
    consentimiento_desde = fields.Datetime(String="Inicio", required=True)
    consentimiento_hasta = fields.Datetime(String="Termino", required=True)
    criterios_exclusion = fields.Selection([('true', 'Si'), ('false', 'No')]
                                            ,'Se revisa Criterios de inclusión/exclusión para screening, anexo 2', required=True)
    demografia_id = fields.Many2one('mediges.demografia', string="Demografia", required=True)
    #Examen Fisico
    estatura = fields.Integer(string="Estatura", required=True)
    peso = fields.Integer(string="Peso", required=True, )
    imc = fields.Integer(string="IMC", readonly=True, compute='_calcula_icm')
    #Signos Vitales
    signos_vitales_id = fields.One2many('mediges.signos_vitales', 'visitas_id', string='Signos Vitales')
    #Antecedentes medico
    covid = fields.Selection([('true', 'Si'), ('false', 'No')], 'Tuvo COVID', required=True)
    tratamiento_covid = fields.Char(string="Tratamiento COVID")
    examen_covid = fields.Selection([('true', 'Si'), ('false', 'No')]
                                    , 'Muestra de sangre para anticuerpos anti-SARSCoV-2', required=True)

    #Riesgo de embarazo
    prueba_embaraso = fields.Selection([('true', 'Si'), ('false', 'No')], 'Prueba de embarazo en orina', required=True)
    edad_fertil = fields.Selection([('true', 'Si'), ('false', 'No')], 'Edad Fertil', required=True)
    riesgo_de_embarazo = fields.Selection([('true', 'Si'), ('false', 'No')]
                                          ,'Tiene riesgo de embarazo? (si es hombre piense en su pareja)', required=True)
    anticoncepcion_id = fields.One2many('mediges.anticoncepcion', 'visitas_id', string='Anticoncepcion')
    #Historial Medico
    enfermedades_id = fields.One2many('mediges.visitas_enfermedades', 'visitas_id', string='Historial Medico')





    @api.multi
    @api.depends('peso', 'estatura')
    def _calcula_icm(self):
      for record in self:
        if record.peso and record.estatura:
            record.imc = record.peso / ((record.estatura / 100)**2)



