from openerp.osv import osv, fields
from openerp import tools

class followup_risk(osv.Model):
    _name = "followup.risk"
    _columns = {
    'visit_date':fields.date('Visit Date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'ingeneral':fields.boolean('in general'),
    'finmatters':fields.boolean('with financial matters'),
    'withealth':fields.boolean('with your health'),
    'witsex':fields.boolean('with sex'),
    'prefer500':fields.boolean('I would prefer 500 Naira for sure'),
    'playgame':fields.boolean('I would play the game'),
    'prefer1000':fields.boolean('I would prefer 1000 Naira for sure'),
    'playthegam':fields.boolean('I would play the game'),
    'never':fields.boolean('Never'),
    'sometimes':fields.boolean('Sometimes'),
    'often':fields.boolean('Often'),
    'never2':fields.boolean('Never'),
    'sometimes2':fields.boolean('Sometimes'),
    'often2':fields.boolean('Often'),
    } 
