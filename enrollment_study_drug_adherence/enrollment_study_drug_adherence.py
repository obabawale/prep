from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_adherence(osv.Model):
    _name = "enrollment.adherence"
    _columns = {
    "visitdate":fields.date('Visit Date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
    'studypill':fields.date('1. When was the last time you took study pills?'),
    'taketablet':fields.selection([('yes','Yes'),('no','No')],'2. During the last month, did you take the tablet every day?'),
	'hwmanydays':fields.integer('2a	How many days did you miss to take a study tablet?'),
	'noofdays':fields.integer('2b. What is the most number of days in a row that you did not take a study tablet?'),
	'studytablets':fields.selection([
		('Very_poor','Very poor'),
		('Poor','Poor'),
		('fair','Fair'),
		('Good','Good'),
		('Very_good','Very good'),
		('excellent','Excellent')
		],'3. Please tell me how well you have taken your study tablets as directed since the last visit.'),
	'nonofthe':fields.selection([
		('None_of_the_time','None of the time'),
		('A_little_of_the_time','A little of the time'),
		('Some_of_the_time','Some of the time'),
		('A_good_bit_of_the_time','A good bit of the time'),
		('Most_of_the_time','Most of the time'),
		('all_of_the_time','All of the time')
		],'4. In general, how often do you take your study tablets?'),						
	'nothin':fields.boolean('Nothing'),	
	'watch':fields.boolean('Watch/clock'),
	'alarm':fields.boolean('Alarm'),
	'pillbox':fields.boolean('Pill box'),	
	'studypart':fields.boolean('Study partner/family members'),	
	'radio':fields.boolean('Radio'),	
	'dailyacti':fields.boolean('Associates it with daily activity'),
	'otherspec':fields.char('Other, specify'),
	'forgot':fields.boolean('Forgot'),
	'alcuse':fields.boolean('alcohol use'),
	'changeinrout':fields.boolean('Change in routine'),
	'beforafter':fields.boolean('prefer to take just before or after sex'),
	'illness':fields.boolean('Illness'),
	'nothavinsex':fields.boolean('Not having sex'),
	'losttablets':fields.boolean('lost tablets'),
	'misavisit':fields.boolean('missed a visit and had no tablets'),
	'dntavfood':fields.boolean('Do not have food'),
	'travelled':fields.boolean('travelled'),
	'stigma':fields.boolean('Confidentiality/stigma'),
	'sharedtab':fields.boolean('shared tablets with someone else'),
	'tabstolen':fields.boolean('Tablet stolen'),
	'sideeffe':fields.boolean('thought tablets caused side effects'),
	'other':fields.boolean('Others'),
	'not_available':fields.boolean('NA'),
	'notaketab':fields.selection([('yes','Yes'),('no','No'),('missedno','Missed no tablet')],'7. Did you decide not to have sex because you did not take your study tablets that day?'),
	'otherused':fields.selection([('yes','Yes'),('no','No'),('notsure','Not sure')], '8. For a variety of reasons, other persons may want to use your studymedication. Do you think that someone other than you has used any of your study tablet?'),
	'studypartused':fields.selection([('yes','Yes'),('no','No'),('notsure','Not sure')], 'a. Do you think your study partner has used any of your tablets?'),
	'someoneelse':fields.selection([('yes','Yes'),('no','No(go to item 8c)'),('notsure','Not sure(go to item 8c)')], 'b. Do you think someone else has used any of your study tablets?'),
	'who':fields.char('bi.	Who?'),	
	'nooftabs':fields.integer('c. Estimate how many tablets were used by someone other than you:'),
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

