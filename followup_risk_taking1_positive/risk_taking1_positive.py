from openerp.osv import osv, fields
from openerp import tools

class followup_risktaking_positive(osv.Model):
    _name = "followup.risk.taking.positive"
    _columns = {
    'visitdate':fields.date('Visit Date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'ingeneral':fields.integer('a. in general'),
	'financialmatters':fields.integer('b. with financial matters'),
	'yourhealth':fields.integer('c. with your health'),
	'sexualbehaviours':fields.integer('d. In sexual behaviours'),
	'would_you_prefer':fields.selection([
        ('one','1'),
        ('two','2'),
        ('three','3')],
        'Answer'),
    'business1':fields.boolean('Preferred Business 1'),
    'business2':fields.boolean('Preferred Business 2'),
    'business3':fields.boolean('Preferred Business 3'),
    'business4':fields.boolean('Preferred Business 4'),
    'business5':fields.boolean('Preferred Business 5'),
    'business6':fields.boolean('Preferred Business 6'),
    }