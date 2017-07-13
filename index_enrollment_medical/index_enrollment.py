from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class eligibility_indexenrollmentmedical(osv.Model):
    _name = "eligibility.indexenrollmentmedical"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True), 
        'stage1' : fields.selection([('yes','YES'),('no','NO')],'a. Stage 1'),
        'stage2' : fields.selection([('yes','YES'),('no','NO')],'b. Stage 2'),
        'stage3' : fields.selection([('yes','YES'),('no','NO'),('ineligible','Ineligible')],'c. Stage 3'),
        'stage4' : fields.selection([('yes','YES'),('no','NO'),('ineligible','Ineligible')],'d. Stage 4'),
        'positive' : fields.date('2. Date of first known positive test for HIV'),
        'participant' : fields.selection([('yes','YES'),('no','NO')],'3. Is the participant followed in an HIV care program?'),
        'toosick' : fields.selection([('yes','YES'),('no','NO(If no go to 5)')],'4. In the last month, has the participant been too sick to work or do daily activities?'),
        'daysmissed' : fields.integer('a. Number of days missed'),
        'bednet' : fields.selection([('yes','YES'),('no','NO')],'5. In the past week, has the participant used a bednet?'),
        'takenARVs' : fields.selection([('yes','YES'),('no','NO(If no go to 6d)')],'a. Has the participant ever taken ARVs for treatment?'),
        'PMTCT' : fields.selection([('yes','YES'),('no','NO(If no go to 6d)')],'b. Has the participant ever taken ARVs for PMTCT?'),
        'thengo' : fields.text('List ARVs taken, then go to item 7'),

        'eligible' : fields.selection([('yes','YES'),('no','NO')],'not eligible for ARVs'),
        'count' : fields.selection([('yes','YES'),('no','NO')],'repeat CD4 count > 350 or clinic said wasnt eligible'),
        'stigma' : fields.selection([('yes','YES'),('no','NO')],'Stigma'),
        'adherence' : fields.selection([('yes','YES'),('no','NO')],'adherence was too difficult'),
        'healthy' : fields.selection([('yes','YES'),('no','NO')],'Feeling healthy'),
        'processing' : fields.selection([('yes','YES'),('no','NO')],'pre-treatment processing(in queue at ART center)'),
        'badside' : fields.selection([('yes','YES'),('no','NO')],'fears / has experienced bad side effects'),
        'supportive' : fields.selection([('yes','YES'),('no','NO')],'clinic was not supportive'),
        'clinic' : fields.selection([('yes','YES'),('no','NO')],'no ART slots at the clinic'),
        'transportation' : fields.selection([('yes','YES'),('no','NO')],'transportation costs'),
        'newly' : fields.selection([('yes','YES'),('no','NO')],'Newly diagnosed'),
        'others' : fields.char('Others'),

        'cotrimoxazole' : fields.selection([
            ('yes','YES'),
            ('no','NO')
            ],'7. Is the participant currently taking cotrimoxazole?'),

        'prophylaxis': fields.boolean('prophylaxis'),
        'toxoplasmosis' : fields.boolean('toxoplasmosis treatment'),
        'pcp_treatment' : fields.boolean('PCP treatment'),
        'other_reasons': fields.char('Others(specify)'),

        'isoniazid' : fields.selection([('yes','YES'),('no','NO')],'8. Is the participant currently taking isoniazid or another medication as prophylaxis for TB?'),
        'theparticipant' : fields.selection([('yes','YES'),('no','NO(If no, go to 10)')],'9. Has the participant been treated for TB before?'),
        'treated' : fields.selection([('yes','YES(for how long)'),('no','NO')],'9a. Is the participant currently being treated for TB?'),
        'yyyyy' : fields.integer('9b. yyyyy'),
        'verbally' : fields.selection([('yes','YES(If yes complete social harms form)'),('no','NO')],'10. In the past three months, has the participant been verbally, physically, or economically abused by his or her study partner?'),
        'participantcurrently' : fields.selection([('yes','YES(If yes complete pregnancy report)'),('no','NO')],'11. Female only: Is the participant currently pregnant?'),        
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