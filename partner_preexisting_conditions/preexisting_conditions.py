from openerp.osv import osv, fields
from openerp import tools

class preexisting_conditions(osv.Model):
    _name = "preexisting.conditions"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'no_preexisting_conditions':fields.boolean('No pre-existing conditions'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'diagnosis1':fields.char('Diagnosis'),
        'dateofdiagnosis' : fields.date('a. Date of diagnosis / surgery:'),
        'conditionongoing' : fields.selection([('yes','YES'),('no','NO')],'b. Is condition ongoing?'),
        'initials' : fields.char('c. initials/date'),
        'diagnosis2':fields.char('Diagnosis'),
        'dateofdiagnosis2' : fields.date('a. Date of diagnosis / surgery:'),
        'conditionongoing2' : fields.selection([('yes','YES'),('no','NO')],'b. Is condition ongoing?'),
        'initials2' : fields.char('c. initials/date'),
        'diagnosis3':fields.char('Diagnosis'),
        'dateofdiagnosis3' : fields.date('a. Date of diagnosis / surgery:'),
        'conditionongoing3' : fields.selection([('yes','YES'),('no','NO')],'b. Is condition ongoing?'),
        'initials3' : fields.char('c. initials/date'),
        'diagnosis4':fields.char('Diagnosis'),
        'dateofdiagnosis4' : fields.date('a. Date of diagnosis / surgery:'),
        'conditionongoing4' : fields.selection([('yes','YES'),('no','NO')],'. Is condition ongoing?'),
        'initials4' : fields.char('c. initials/date'),
        'diagnosis5':fields.char('Diagnosis'),
        'dateofdiagnosis5' : fields.date('a. Date of diagnosis / surgery:'),
        'conditionongoing5' : fields.selection([('yes','YES'),('no','NO')],'b. Is condition ongoing?'),
        'initials5' : fields.char('c. initials/date'),
        'diagnosis6':fields.char('Diagnosis'),
        'dateofdiagnosis6' : fields.date('a. Date of diagnosis / surgery:'),
        'conditionongoing6' : fields.selection([('yes','YES'),('no','NO')],'b. Is condition ongoing?'),
        'initials6' : fields.char('c. initials/date'),
    }