from openerp.osv import osv, fields
from openerp import tools

class logs_protocolviolation(osv.Model):
    _name = "logs.protocolviolation"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'startdate' : fields.date('1. Date event occurred (start date):'),
        'sitedate':fields.date('a. Date of site awareness'),
        'briefdescription':fields.text('2. Provide a brief description of the protocol violation:'),
        'requirereporting':fields.selection([('no','No'),('yes', 'Yes')],'3. Does this event require reporting to the site IRB?'),
        'why_not':fields.text('a. If no, why not:'),
        'datereported':fields.date('b. If yes, Date reported to  site IRB'),
        'eventdate':fields.date('4. Date event ended:'),
        'breachof':fields.boolean('breach of confidentiality'),
        'safetyrelated':fields.boolean('safety related to RAE'),
        'informed':fields.boolean('informed consent'),
        'eligibility':fields.boolean('eligibility criteria'),
        'failureto':fields.boolean('failure to implement required study procedure'),
        'useof':fields.boolean('use of non-HREC approved materials and/or performing non-IRB approved procedure'),
        'study':fields.boolean('study drug and accountability'),
        'others' : fields.char('Others: specify'),
        'whatsteps': fields.text('6. What steps have been taken to address this event?'),
        'occurrences': fields.text('7. What steps have been taken to prevent future occurrences?'),
        'additional': fields.text('8. Additional comments:'),        
        } 
