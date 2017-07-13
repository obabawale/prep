from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_whostaging(osv.Model):
    _name = "enrollment.whostaging"
    _columns = {
    'visit_date':fields.date('Visit Date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
    'asymptotic': fields.boolean('Asymptomatic HIV infection'),
    'lymphadenopathy':fields.boolean('Persistent Generalized Lymphadenopathy (PGL)'),
    'weightloss':fields.boolean("Moderate weight loss (<10% of presumed or measured body weight)"),
    'mucocutaneous':fields.boolean('Minor mucocutaneous manifestations (seborrheic dermatitis, prurigo, fungal nail infection, recurrent oral ulcerations, angular cheilitis)'),
  	"herpes":fields.boolean('Herpes zoster'),
  	'upperrespiratory':fields.boolean('Recurrent or chronic upper respiratory tract infections (bacterial sinusitis, bronchitis, otitis media pharyngitis)'),
  	'presumedloss':fields.boolean("Severe weight loss ( > 10% of presumed or measured body weight)"),
  	'bacterialinfections':fields.boolean('Severe bacterial infections (e.g., pneumonia, pyomyositis, empyema, bone or joint infections)'),
  	'chronicdiarrhea':fields.boolean('Unexplained chronic diarrhea > 1 month'),
  	'ptb':fields.boolean('Pulmonary tuberculosis (PTB)'),
  	'prolongedfever':fields.boolean('Unexplained prolonged fever > 1 month'),
  	'ohl':fields.boolean('Oral hairy leukoplakia (OHL)'),
  	'thrush':fields.boolean('Oral candidiasis (Thrush)'),
  	'stomatitis':fields.boolean('Necrotizing ulcerative stomatitis, gingivitis, or periodontitis'),
  	'unexplainedanemia':fields.boolean('Unexplained anemia, neutropenia, or thrombocytopenia'),
  	'severeweightloss':fields.boolean('HIV wasting syndrome (Severe weight loss and either unexplained chronic diarrhea or unexplained prolonged fever > 1 month)'),
  	'chronicorolabial':fields.boolean('Chronic orolabial, genital or ano-rectal herpes simplex virus infection > 1 month'),
  	'encephalopathy':fields.boolean('HIV encephalopathy'),
  	'cervicalcarcinoma':fields.boolean('Invasive cervical carcinoma'),
  	'CNSlymphoma':fields.boolean('Primary CNS lymphoma or B cell non-Hodgkin\'s Lymphoma'),
  	'endemicmycosis':fields.boolean('Any disseminated endemic mycosis (e.g. histoplasmosis)'),
  	'leukoencephalopathy':fields.boolean('Progressive multifocal leukoencephalopathy (PML)'),
  	'candidiasis':fields.boolean('Candidiasis of the esophagus or airways'),
  	'cryptosporidiosis':fields.boolean('Cryptosporidiosis or isosporiasis with diarrhea > 1 month'),
  	'cytomegalovirus':fields.boolean('Cytomegalovirus (CMV) retinitis or disease of other organs'),
  	'mycobacterialinfection':fields.boolean('Disseminated non-tuberculous mycobacterial infection'),
  	'toxoplasmosis':fields.boolean('Toxoplasmosis of the brain'),
  	'cardiomyopathy':fields.boolean('Symptomatic HIV nephropathy or cardiomyopathy'),
  	'cryptococcosis':fields.boolean('Cryptococcal meningitis, cryptococcosis'),
  	'severebacterial':fields.boolean('Recurrent severe bacterial pneumonia (more than 2 episodes within 1 year)'),
  	'septicaemia':fields.boolean('Recurrent septicaemia (including non-typhoidal Salmonella)'),
  	'pneumocystis':fields.boolean('Pneumocystis carinii pneumonia'),
  	'eptb':fields.boolean('Extra-pulmonary tuberculosis (EPTB)'),
  	'Kaposissarcoma':fields.boolean('Kaposi\'s sarcoma'),
  	'leishmaniasis':fields.boolean('Atypical disseminated leishmaniasis'),
    }

    @api.one
    @api.depends('partner_id.couple', 'partner_id.ips')
    def _compute_enrollment_id(self):
      if not (self.partner_id.couple and self.partner_id.ips):
        raise exceptions.ValidationError('Please update the couple and I/P fields!')
      #else
      if self.partner_id.ips == 'I' or self.partner_id.ips == 'i':
        self.enrollment_id = '000' + str(self.partner_id.couple) + 'A'
      if self.partner_id.ips == 'P' or self.partner_id.ips == 'p':
        self.enrollment_id = '000' + str(self.partner_id.couple) + 'B'

