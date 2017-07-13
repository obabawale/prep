from openerp.osv import osv, fields
from openerp import tools

class followup_harm(osv.Model):
    _name = "followup.harm"
    _columns = {
    'visit_date':fields.date('Visit Date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Screening ID", related='partner_id.name'),
    'verbalabuse':fields.selection([('1','yes'),('2','no')],"1. Was the participant verbally abused by his or her study partner?"),
    'howoften1':fields.char('1a. How often'),
    'physabuse':fields.selection([('1','yes'),('2','no')],'2. Was the participant physically abused by his or her study partner?'),
    'hwoften2':fields.char('2a. How often'),
    'econabuse':fields.selection([('1','yes'),('2','no')], '3. Was the participant economically abused by his or her study partner?'),
    'otherabuse':fields.selection([('1','yes'),('2','no')], '4. Was the participant abused by his or her study partner in any other way (not fitting into the categories of verbal, physical, or economic abuse)?'),
    'breakup':fields.boolean('i	relationship break-up'),
    'lossofinc':fields.boolean('ii. loss of income or economic support'),
    'lossofemplo':fields.boolean('iii. loss of employment'),
    'chngeofresid':fields.boolean('iv. change of residence'),
    'lossofcustody':fields.boolean('v	loss of custody of children'),
    'other':fields.boolean('vi. Other:'),
    'none':fields.boolean('vii. None'),
    'socharm':fields.text('6. Concisely describe the social harm:'),
    } 
