from odoo import api, fields, models, _


class visitas(models.Model):
    _name = "mediges.visitas"
    _inherit = ['mail.thread']

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
    numero_paciente = fields.Char(string="Numero Paciente", related='paciente.numero_paciente' , readonly=True)
    demografia = fields.Many2one('mediges.demografia', string="Demografia", related='paciente.demografia_id'
                                 , readonly=True)
    fecha_nacimiento = fields.Date(string="Fecha Nacimiento", related='paciente.fecha_nacimiento', readonly=True)
    edad = fields.Integer(string="Edad",  readonly=True, related='paciente.edad')
    sexo = fields.Many2one('mediges.sexo', string="Sexo", related='paciente.sexo_id', readonly=True)

    consentimiento = fields.Selection([('true','Si'),('false','No')]
                                      ,'Se realiza proceso de Consentimiento informado, anexo 1')
    consentimiento_desde = fields.Datetime(string="Inicio")
    consentimiento_hasta = fields.Datetime(string="Termino")
    criterios_exclusion = fields.Selection([('true', 'Si'), ('false', 'No')]
                                            ,'Se revisa Criterios de inclusión/exclusión para screening, anexo 2')
    #Examen Fisico
    estatura = fields.Integer(string="Estatura")
    peso = fields.Integer(string="Peso" )
    imc = fields.Integer(string="IMC", readonly=True, compute='_calcula_icm')
    #Signos Vitales
    signos_vitales_id = fields.One2many('mediges.signos_vitales', 'visitas_id', string='Signos Vitales')
    #Antecedentes medico
    covid = fields.Selection([('true', 'Si'), ('false', 'No')], 'Tuvo COVID',)
    examen_covid = fields.Selection([('true', 'Si'), ('false', 'No')]
                                    , 'Muestra de sangre para anticuerpos anti-SARSCoV-2')

    #Riesgo de embarazo
    prueba_embaraso = fields.Selection([('true', 'Si'), ('false', 'No')], 'Prueba de embarazo en orina')
    edad_fertil = fields.Selection([('true', 'Si'), ('false', 'No')], 'Edad Fertil',)
    riesgo_de_embarazo = fields.Selection([('true', 'Si'), ('false', 'No')]
                                          ,'Tiene riesgo de embarazo? (si es hombre piense en su pareja)')
    anticoncepcion_id = fields.One2many('mediges.anticoncepcion', 'visitas_id', string='Anticoncepcion')
    #Historial Medico
    enfermedades_id = fields.One2many('mediges.visitas_enfermedades', 'visitas_id', string='Historial Medico')
    tipo_visita = fields.Selection([
        ('SCRENNING', "SCRENNING"),
        ('RANDOMIZACION', "RANDOMIZACION"),
        ('VISITA3', "VISITA 3"),
        ('VISITA4', "VISITA 4"),
        ('VISITA5', "VISITA 5"),
        ('VISITA6', "VISITA 6"),
        ('VISITA7', "VISITA 7"),
        ('VISITA8', "VISITA 8"),
        ('VISITA_RETIRO', "VISITA DE RETIRO TEMPRANO"),
    ], default='SCRENNING', string="Tipo Visita", track_visibility='onchange')
    visitas_indicadores_id = fields.One2many('mediges.visitas_indicadores_fisicos', 'visitas_id', string='Examen Fisico')

    #Rando
    muestra_sangre_arnsec = fields.Selection([('true', 'Si'), ('false', 'No')]
                            ,'Muestra de sangre para biomarcador de ARNsec (tubos PAXgene, sangre entera), ml.')
    cuestionario_de_mru = fields.Selection([('true', 'Si'), ('false', 'No')]
                            , 'Se realiza Cuestionario de MRU (versión inicial) ')
    síntomas_previos = fields.Selection([('true', 'Si'), ('false', 'No')]
                                           , 'Se evalúa si el paciente tiene Síntomas previos a la vacunación'
                                             ', que pudieran ser excluyentes para la vacunación. ')



    @api.multi
    @api.depends('peso', 'estatura')
    def _calcula_icm(self):
      for record in self:
        if record.peso and record.estatura:
            record.imc = record.peso / ((record.estatura / 100)**2)



