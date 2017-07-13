from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_partnerenrollment(osv.Model):
    _name = "enrollment.partnerenrollment"
    _columns = {
        'visitdate' : fields.date('Visit date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
    	'collectiondate':fields.date('1. Specimen collection date'),
		'HIVstatus': fields.selection([('negative','Negative'),('positive', 'Positive(Participant is ineligible.)'),('indeterminate', 'Indeterminate(Participant is ineligible.)')],'2. HIV status by national algorithm'),
		"menstrualperiod": fields.date('A. Date of last menstrual period'),
        'dont_know_period_date': fields.boolean('Don\'t Know'),
		'pregnancyspecimen':fields.date('4. Pregnancy specimen (urine) collection date'),
        'dont_know_specimen_date': fields.boolean('Don\'t Know'),
		'pregnancytest': fields.selection([('negative','Negative'),('positive', 'Positive(Participant is ineligible.)')],'5. Pregnancy test result'),
		'provideindependent':fields.selection([('no','No'),('yes', 'Yes')],'6. Did the participant provide independent, written, informed consent for specimen storage?'),
		'designee_name':fields.char('A. Investigator / Designee'),
        'date_signed': fields.date('Date signed'),
		'didthe' :fields.selection([('no','No'),('yes', 'Yes')],'7. Did the participant provide independent, written, informed consent for enrollment?'),
		'informedconsent':fields.date('A. When was the informed consent for enrollment marked or signed?'),
		'protocol_version':fields.char('B. Consented under protocol version #:'),
		'theparticipant':fields.selection([('no','No(Go to 9)'),('yes', 'Yes')],'8. Did the participant provide independent, written, informed consent for specimen storage?'),
        'specimenstorage':fields.date('A. When was the informed consent for specimen storage marked or signed?'),
        'participantid':fields.date('9. Date Participant ID assigned'),
		'atenrollment':fields.selection([('no','No'),('yes', 'Yes')],'10. Did the participant accept PrEP at Enrollment?'),
		'comm': fields.text('11. Comments:'),
	}

    @api.multi
    @api.depends('partner_id.couple','partner_id.ips')
    def _compute_enrollment_id(self): 
        self.ensure_one()
        if not (self.partner_id.couple and self.partner_id.ips):
            raise exceptions.ValidationError('Please update the couple and I/P fields!')
    	#else
        if self.partner_id.ips == 'I' or self.partner_id.ips == 'i':
            self.enrollment_id = '000' + str(self.partner_id.couple) + 'A'
        #else
        if self.partner_id.ips == 'P' or self.partner_id.ips == 'p':
            self.enrollment_id = '000' + str(self.partner_id.couple) + 'B'

		