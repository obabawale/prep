from openerp.osv import osv, fields
from openerp import tools

class followup_viralload(osv.Model):
    _name = "followup.viralload"
    _columns = {
    'visitmonth':fields.selection([('1','January'),('2','February'),('3','March'),('4','April'),('5','May'),('6','June'),('7','July'),('8','August'),('9','September'),('10','October'),('11','November'),('12','December')],'Visit Month'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    "speccoldate":fields.date('1. Specimen collection date'),
    'notdone': fields.boolean('Not done'),
    'cd4count':fields.char('2. CD4 count'),
    'cd4percent':fields.char('3. CD4 percent'),
    'notdone2':fields.boolean('Not done'),
    'cd4countyes':fields.selection([('yes','yes'),('no','no')],'4. Does the CD4 count in item 2 change the participant\'s ART eligibility?'),
    'contactyes':fields.selection([('yes','yes'),('no','no')],'4a. Was an attempt made to contact the participant?'),
    'firstattemptdate':fields.date('4a1. Date of first attempt:'),
    'interimvisityes':fields.selection([('yes','yes'),('no','no')],'4b. Was an interim visit scheduled?'),
    'scheduledvisitdate':fields.date('4b1. Date of scheduled visit:'),
    'declined':fields.selection([('participant_declined','participant declined'),('participant_cannot_be_reached','participant cannot be reached')],'4b2. What was the reason for not scheduling an interim visit?'),
    'others':fields.char('Others:'),
    'viralload':fields.char('5. Viral load'),
    'nonedone':fields.boolean('None was done'),
    } 
