from openerp.osv import osv, fields
from openerp import tools

class followup_visit(osv.Model):
    _name = "followup.visit"
    _columns = {
    'visit_date':fields.date('Visit Date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'attendvisit':fields.selection([("yes","Yes"),("no","No")],'1. Did participant attend the visit?'),
    'travelling':fields.boolean('i. traveling or out of area'),
    'familyorper':fields.boolean('ii. family or personal issues'),
    'refvisit':fields.boolean('iii.	refused visit'),
    'plannedabs':fields.boolean('iv. planned absence'),
    'workorschl':fields.boolean('v. work or school issues'),
    'transportiss':fields.boolean('vi. transportation issues'),
    'illorhos':fields.boolean('	vii. illness or hospitalized'),
    'incarcerated':fields.boolean('viii. incarcerated'),
    'reloormovd':fields.boolean('ix. relocated or moved'),
    'unabletocon':fields.boolean('x. unknown / unable to contact '),
    'other':fields.char('xi. other, specify:'),
    'clinic':fields.boolean('clinic'),
    'home':fields.boolean('home'),
    'other2':fields.char('other, specify:'),
    'takenhivmed':fields.selection([('yes','Yes'),('no','No')],'3. Since the last visit, has the participant taken HIV medication for post-exposure prophylaxis (PEP) against HIV?'),
	'noofdays':fields.integer('3a	For how many days was medication taken?'),
	'onprep':fields.selection([('yes','Yes'),('no','No')],'3b. Is the participant currently on PrEP?'),
	'scheduled':fields.boolean('Scheduled'),
	'monthpreg':fields.boolean('monthly pregnancy'),
	'interim':fields.boolean('interim'),
	'stopvisit':fields.boolean('stop visit'),
	'compschproc':fields.boolean('i	complete scheduled procedures'),
	'repsocharm':fields.boolean('ii. report social harm'),
	'pillcount':fields.boolean('iii. pill count'),
	'blooddraw':fields.boolean('iv. blood draw for additional testing'),
	'stisymp':fields.boolean('v. STI symptoms'),
	'pckupdrug':fields.boolean('vi. return or pick up study drug'),
	'confrmdpreg':fields.boolean('vii.	suspected or confirmed pregnancy'),
	'completepreg':fields.boolean('viii. Complete Pregnancy Report'),
	'specother':fields.boolean('ix. other, specify:'),
    } 
