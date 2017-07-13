from openerp.osv import osv, fields
from openerp import tools

class followuppartner_labresults(osv.Model):
    _name = "followuppartner.labresults"
    _columns = {
    'visit_date':fields.date('Visit Date:'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Screening ID", related='partner_id.name'),
    'speccoldate':fields.date('Specimen collection date:'),
    'hiv_negative':fields.boolean('A. Negative'),
    'hiv_positive':fields.boolean('B. Positive'),
    'hiv_indeterminate':fields.boolean('C. Indeterminate'),
    'eia_negative':fields.boolean('A. Negative'),
    'eia_positive':fields.boolean('B. Positive'),
    'eia_indeterminate':fields.boolean('C. Indeterminate'),
    'mensdate':fields.date('3. Date of last menstrual period:'),
    'dont_know':fields.boolean('Don\'t Know'),
    'partpregnant':fields.selection([('1','Yes'),('2',"No")],"4. Is the participant pregnant?"),
    'already_reported':fields.boolean("Already reported"),
    'reported_date':fields.date('Reported at visit'),
    'breastfeeding':fields.selection([('1',('Yes')),('2','No')],"5. Is the participant breastfeeding?"),
    'specimendate':fields.date('6. Specimen collection date:'),
    'creatinine':fields.float('7. Creatinine:'),
    'creatgrade':fields.integer("a. Creatinine grade (0-4)"),
    'adversevnt':fields.selection([('yes','Yes'),('no','No')],'b. Is this an adverse event?'),
    'reltomed':fields.selection([('1','Definitely related '),('2','Probably related'),('3','Possibly related'),('4','Probably not related'),('5','pending')],"c. Relationship to study medication:"),
    'creatinine_clear':fields.float('8. Creatinine clearance:'),
    } 
