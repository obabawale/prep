from openerp.osv import osv, fields
from openerp import tools

class followupparticipant_prepcorrection(osv.Model):
    _name = "followupparticipant.prepcorrection"
    _columns = {
    'visit_date':fields.date('Visit date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'givenprep': fields.selection([('yes','Yes'),('no','No (If no end of form)')],'1. At the last study visit attended, was the participant given PrEP?'),
    'takebreak': fields.selection([('yes','Yes'),('no','No')],'2. Since the last study visit was there any period of time when the participant deliberately decided to take a break from taking PrEP?'),
    'lastbreak':fields.integer("3. How many deliberate breaks were there since the last attended studyvisit?"),
    'lengthofbreak':fields.integer("4. What was the length of the longest deliberate break?"),
    'notathome':fields.boolean('i. participant was not at home'),
    'tired':fields.boolean('ii. tired of taking the pills'),
    'partnernothom':fields.boolean('iii. partner was not at home'),
    'brokeup':fields.boolean('iv. Broke up with partner'),
    'outofpill':fields.boolean('v. ran out of pills'),
    'others':fields.char('Others:'),
    "high":fields.boolean("high"),
    "moderate":fields.boolean('moderate'),
    "low":fields.boolean('low'),
    "none":fields.boolean('none'),
    'stopprep':fields.selection([('yes',"yes"),('no','No'),('dont_know','Dont Know')],"7. During the longest break, did the participants partner know that theparticipant stopped taking PrEP?"),
    'startprep':fields.selection([('yes',"yes"),('no','No. If no go to item 9')],"8. Did the participant start taking PrEP again after this break?"),
    'reasonnotapply':fields.boolean('i. the reason mentioned in item 5 no longer applied'),
    'wantababy':fields.boolean('ii. the participant wants to have a baby'),
    'newprtner':fields.boolean('iii. new partner of unknown or positive HIV status'),
    'thoughtchange':fields.boolean('iv. the participant thought his/her risk of getting HIV changed'),
    'other':fields.boolean('other, specify:'),
    'comm':fields.text('9. Comments (Provide additional details about the time when the participant did not take PrEP, and whether the participant is currently using PrEP or plans to use PrEP in the future):'),
    } 
