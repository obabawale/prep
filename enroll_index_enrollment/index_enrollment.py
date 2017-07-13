from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_indexenrollment(osv.Model):
	_name = 'enrollment.indexenrollment'
	_columns = {
	'visitdate' : fields.date('Visit Date'),
	'partner_id' : fields.many2one('res.partner', 'Sceening ID', ondelete='cascade'),
	'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
	'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
	'eligibility_criteria':fields.selection([('yes','Yes'),('no','No')],'1. Did the participant meet all eligibility criteria according to the Index Screening Eligibility Criteria'),
	'designee_name':fields.char('a. Investigator / Designee'),
	'date_signed':fields.date('Date signed'),
	'meeteligibility': fields.selection([('no','No'),('yes', 'Yes')],'2. Did the participant provide independent, written, informed consent for enrollment?'),
	"signdate": fields.date('2a. When was the informed consent for enrollment marked or signed?'),
	'protocolversion':fields.char('2b. consented under protocol version'),
	'specimen':fields.selection([('no','No'),('yes', 'Yes')],'3. Did the participant provide independent, written, informed consent for specimen storage?'),
	'storagedate':fields.date('3a. When was the informed consent for specimen storage marked or signed?'),
	'iddate':fields.date('4. Date participant ID assigned:'),
	'pregnant': fields.char('5. Is the participant currently pregnant?'),
	'arvtoday' :fields.selection([('no','No'),('yes', 'Yes')],'6. Is the participant eligible for ARVs today under current national guidelines?'),
	'partofferedarvatenrollment' : fields.selection([
		('1. ARVs offered on site','1. ARVs offered on site'),
		('2. participant referred to offsite','2. participant referred to offsite'),
		('3. not offered or referred','3. not offered or referred, explain')
		],'a. Is the participant being offered ARVs at enrollment?'),
	'explain_why_not_offered':fields.text('Please provide explanation and goto 7'),
	'acceptonsite':fields.boolean('1. accepted on site'),
	'deconsite':fields.boolean('2. declined on site'),
	'accref':fields.boolean('4. accepted referral'),
	'decrefer':fields.boolean('5. declined referral'),
	'others':fields.boolean('3. Others'),
	'descp':fields.char('7. comments'),
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