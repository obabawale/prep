from openerp.osv import osv, fields
from openerp import api, exceptions
from openerp import tools

class enrollment_demographics(osv.Model):
    _name = "enrollment.demographics"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID',ondelete='cascade'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'enrollment_id': fields.char(string="Enrollment ID", compute='_compute_enrollment_id', store=True),
        'dateofbirth' : fields.date('1. Date of Birth'),
        'gender_respondent' : fields.selection([('male','Male'),('female','Female')],'2. Gender of respondent'),
        'marriedtostudypart' : fields.selection([('yes','YES'),('no','NO')],'3. Is the respondent married to the study partner?'),
        'howlong' : fields.char('4. How long has the respondent been married tothe study partner?'),

        'rank' : fields.selection([
            ('nocowife','No co-wife'),
            ('firstwife','First wife'),
            ('secondwife','Second wife'),
            ('thirdwifeormore','Third wife or more')
            ],'5. What is the rank of the wife'),

        'areyoumarried' : fields.selection([('yes', "Yes"),('no','No')],'6. Are you and your study partner married?'),
        'livetogether' : fields.selection([('yes','Yes'),('no','No')],'7. Do you and your study partner live together?'),
        'howlongtogeda' : fields.char('8. How long have you been living together?'),
        'livingchildren' : fields.char('9a. How many living children does the respondent have?'),
        'deadchildren' : fields.char('B. How many children that the respondent had died?'),
        'howmanyliving' : fields.char('C. How many living children does the respondent have with the study partner?'),
        'wantmorechildren' : fields.selection([('no','No'),('yes', 'Yes')],'10. Does the respondent want more children with study partner?'),
        'firstsex' : fields.date('11. When did you first have sex with your study partner?'),
        'knowhowlong' : fields.date('12. How long have you known that your partners HIV status was different from your own?'),
        'ethnic' : fields.char('13. What is the respondents ethnic group or tribe'),
        'educationlevel' : fields.selection([('noeducation','No education'),('primary','Primary level'),('tertorhigher','Tertiary or higher level'),('koranic','Koranic education'),('secondary','Secondary level')],'13. What is your highest education level attained?'),
        'monthly_income' : fields.char('15. What is the respondent monthly income(average over the last 3 months)?'),
        'is_there_electricity' : fields.selection([('yes','Yes'),('no','No')],'a. Is there electricity?'),
        'is_there_television' : fields.selection([('yes','Yes'),('no','No')],'b. Is there television?'),
        'is_there_refrigerator' : fields.selection([('yes','Yes'),('no','No')],'c. Is there refrigerator?'),
        'is_there_runningwater' : fields.selection([('yes','Yes'),('no','No')],'d. Is there running water?'),
        'is_there_concrete_or_cement' : fields.selection([('yes','Yes'),('no','No')],'e. Is there concrete/cement floor and walls?'),
        'do_you_sleep_on_mattress' : fields.selection([('yes','Yes'),('no','No')],'f. Do you sleep on a mattress?'),
        'does_household_haveacar' : fields.selection([('yes','Yes'),('no','No')],'g. Does your household have a car?'),
        'do_you_have_mobilephone': fields.selection([('yes','Yes'),('no','No')],'h. Do you have a personal mobile phone?'),
        'no_of_roomsinthehouse' : fields.char("i. How many rooms are in the house?"),
        'no_of_peopleinthehouse' : fields.char('j. How many people live in the house?'),
        'occupation' : fields.selection([
            ('not_working','Not working'),
            ('skilledmanual','Skilled manual'),
            ('trades','Trades/Sales'),
            ('student', 'Student'),
            ('professinal','Professional'),
            ('farmer','Farmer, animal raising, fishermen'),
            ('services','Services')],'17. What is your main occupation?'), 
        'other': fields.char('Other: specify'),
        'who_makes_healthdecisions': fields.selection([('myself','Myself'),('my_partner','My partner'),('someonelse',' Someone else')],'18. Who usually makes decisions regarding your health?'),
        'do_you_need_permission_to_goout':fields.selection([('no','No'),('yes','Yes'),('itdepends','It depends where I go')],'19. If you want to go out, do you need the permission of your partner?'),       
        'noofdrink': fields.char('20. How many bottles of drink does the respondent consume per week?'),
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
