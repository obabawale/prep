from openerp.osv import osv, fields
from openerp import tools

class followupindex_drugdispensing(osv.Model):
    _name = "followupindex.drugdispensing"
    _columns = {
        'visitdate': fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'eligibleforarv' : fields.selection([('yes','Yes'),('no','No')],'1. At this visit, is the participant eligible for ARVs under current national guidelines?'),
        'alreadyonarv' : fields.selection([('yes','Yes'),('no','No')],'2a. Is the participant already on ARVs?'),
        'getting_arv_where' : fields.selection([('onsite','On site'),('offsite','Off site')],'2b. Where is the participant getting his/her ARVs?'),
        'offsite_specify':fields.char('Offsite (specify)'),
        'arvsonsite' : fields.selection([('yes','YES'),('no','NO')],'ARVs offered on site?'),
        'referredoffsite' : fields.selection([('yes','YES'),('no','NO')],'participant referred to offsite'),
        'notofferedorreferred' : fields.char('not offered or referred, explain:'),
        'acceptedonsite' : fields.selection([('yes','YES'),('no','NO')],'accepted on site'),
        'declinedonsite' : fields.selection([('yes','YES'),('no','NO')],'declined on site'),
        'acceptedreferral' : fields.selection([('yes','YES'),('no','NO')],'accepted referral'),
        'declinedreferral' : fields.selection([('yes','YES'),('no','NO')], 'Declined referral'),
        'arvs_list' : fields.char('3b. If ARVs accepted on site today, list all ARVs dispensed'),
        'comments' : fields.text('4. Comments'),
    } 
