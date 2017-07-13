from openerp.osv import osv, fields
from openerp import tools

class custom_fields_partner(osv.Model):
    _inherit = 'res.partner'

    _columns = {
            'site': fields.integer('Site'),
            'study': fields.integer('Study'),
            'patsite': fields.integer('Site'),
            'patstudy': fields.integer('Study'),
            'couple': fields.integer('Couple'),
            'ips':fields.selection([('I','I'),('P','P')],'I/P'),
            'chk': fields.integer('Chk'),
            'paticipantno': fields.char('Participant NUmber')
               } 

    _sql_constraints = [
        ('doc_uniq', 'unique (site,study,name)','The Screening ID already exist!'),
    ]
