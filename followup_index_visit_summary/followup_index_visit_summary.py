from openerp.osv import osv, fields
from openerp import tools

class followupindex_visitsummary(osv.Model):
    _name = "followupindex.visitsummary"
    _columns = {
    'visit_date':fields.date('Visit date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'attend_visit':fields.selection([('yes','Yes'),('no','No')],'1. Did the participant attend the visit?'),
    'outtaarea':fields.boolean('i. travelling or out of area'),
    'famissue':fields.boolean('ii. family or personal issues'),
    'refusdvist':fields.boolean('iii. refused visit'),
    'plandabsence':fields.boolean('iv. planned absence'),
    'workorschl':fields.boolean('v. work or school issues'),
    'transportissue':fields.boolean('vi. transportation issues'),
    'illness':fields.boolean('vii. illness or hospitalized'),
    'incarcerated':fields.boolean('viii. incarcerated'),
    'relocated':fields.boolean('ix. relocated or moved'),
    'unabletocontact':fields.boolean('x. unknown/unable to contact.'),
    'other':fields.boolean('xi.other, specify:'),
	'visit_location':fields.selection([('1','clinic'),('2','home'),('3','other, specify')],'Location of study visit:'),
	'typeofvisit':fields.selection([('1','i. scheduled'),('2','ii. interim'),('3','iii. stop visit')],'Type of visit:'),
	'conduct_procedure':fields.selection([('yes','Yes'),('no','No')],'4. Were all the scheduled procedure conducted on the same day?'),
    'comschdproc':fields.boolean('i. complete scheduled procedures'),
    'repsocharm':fields.boolean('ii. report social harm'),
    'blooddraw':fields.boolean('iii. blood draw for additional testing'),
    'stisymp':fields.boolean('iv. STI symptoms. If diagnosed with an STI, complete Index Physical Exam.'),
    'artref':fields.boolean('v. ART referral / initiation'),
    'suspregnancy':fields.boolean('vi. suspected or confirmed pregnancy. Complete pregnancy report.'),
    } 

