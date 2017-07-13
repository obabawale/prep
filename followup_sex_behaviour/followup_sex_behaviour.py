from openerp.osv import osv, fields
from openerp import tools

class followup_sexbehaviour(osv.Model):
    _name = "followup.sexbehaviour"
    _columns = {
        'visit_date':fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
	    '1':fields.selection([('yes','Yes'),('no','No')],'1. Are you and your study partner still together as a couple?'),
	    '2':fields.selection([('partner_died','partner died'),('broke_up','broke up/divorced'),('others','Others')],'2. Why are you no longer a couple?'),
	    '2a':fields.selection([('yes','Yes'),('no','No')],'2a. Do you currently have a sexual partner?'),
	    '2b':fields.date('2b. When did you first have sex with this partner?'),
	    '3':fields.selection([('yes','Yes'),('no','No')],'3. Have you had sexual intercourse with your study partner in the last 3 months?'),
	    '3a':fields.selection([('Days_ago','Days ago'),('Weeks_ago','Weeks ago'),('Months_ago','Months ago')],'3a. When did you last have sexual intercourse with your study partner?'),
	    '3b':fields.selection([('yes','Yes'),('no','No')],'3b. Did you use a condom the last time you had sexual intercourse with your study partner?'),
	    '4':fields.integer('4. In the past month, how many times did you have sexual intercourse with your study partner?'),	    
	    '4a':fields.char('4a. How many times was a condom used?'),
	    '4b':fields.char('4b. How long has it been since you last had sex with your study partner?'),
	    '4c':fields.selection([('yes','Yes'),('no','No')],'4c. During this most recent encounter, was a condom used?'),
	    '5':fields.char('5. Besides your study partner, how many individuals have you had sex with in the past month?'),
	    '5a':fields.integer('5a. Of these individuals, how many are new sexual partners?'),
	    '5b':fields.boolean('5b. In the past month, how many times did you have sexual intercourse with someone other than your study partner?'),
	    '5c':fields.integer('5c. How many times was a condom used?'),
	    '6':fields.selection([('yes','Yes'),('no','No')],'6. In the past month, did you have anal sex?'),
	    '7':fields.selection([('yes','Yes'),('no','No')],'7. Are you using any of the following birth control methods? Mark all that apply'),
	    'Oral':fields.boolean('Oral'),
	    'Implant':fields.boolean('Implant'),
	    'Post-menopausal':fields.boolean('Post-menopausal'),
	    'IUD':fields.boolean('IUD'),
	    'tubal_ligation':fields.boolean('tubal ligation / hysterectomy'),
	    'Pregnant':fields.boolean('Pregnant'),
	    'Injectable':fields.boolean('Injectable'),
	    'Condom':fields.boolean('Condom'),
	    'other':fields.boolean('Other'),
	    '8':fields.selection([('yes','Yes'),('no','No')],'8. Since the last visit, has the participant been verbally, physically, or economically abused by his or her study partner?'),
    } 
