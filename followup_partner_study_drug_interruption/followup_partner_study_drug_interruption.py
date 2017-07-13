from openerp.osv import osv, fields
from openerp import tools

class followup_interruption(osv.Model):
    _name = "followup.interruption"
    _columns = {
    'visit_date':fields.date('Visit Date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
	'meddiscont':fields.date('1. Date study medication discontinued:'),
	'beenonarv':fields.selection([('yes','Yes'),('no','No')],'3. PrEP Stop: Index partner has been on ARVs for over six months'),
	'seroconverter':fields.selection([('yes','Yes'),('no','No')],'4. Participant is a possible HIV seroconverter.'),	
	'renaltox':fields.selection([('yes','Yes'),('no','No')],'5. Renal toxicity'),
	'advevent':fields.text('7. Adverse Event (other than renal toxicity or RAE), describe:'),
	'refusedstudy':fields.text('8. Participant refused study medication'),
	'positpreg':fields.selection([('yes','Yes'),('no','No')],'a. Participant has had a positive pregnancy test (women only)'),
	'partbreast':fields.selection([('yes','Yes'),('no','No')],'b.	Participant is breastfeeding (women only)'),
	'invesdecision':fields.char('c. Investigator decision, specify:'),	
	'otherreasons':fields.text('Other reasons, specify:'),
	'studymeddate':fields.date('9. Date study medication re-established:'),
	'commentsss':fields.text('Comments'), 
    } 
