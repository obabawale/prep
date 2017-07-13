from openerp.osv import osv, fields
from openerp import tools

class followup_prep(osv.Model):
    _name = "followup.prep"
    _columns = {
    'visit_date':fields.date('Visit Date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'beenusing':fields.selection([('yes','Yes'),('no','No(If no, End of form)')],'1. Has the index participant been using ART for > 6 months?'),
    'artuse':fields.selection([('yes','Yes(If yes, Go to item 3)'),('no','No(If no, Complete item 2a, then end of form)')],'Is the participant discontinuing PrEP due to index ART use?'),
    'vloadntsupp':fields.boolean('i. index viral load not suppressed'),
    'longerartuse':fields.boolean('ii	waiting for longer ART use by index'),
    'preppreg':fields.boolean('iii. consented to PrEP during pregnancy'),
    'fertdesire':fields.boolean('iv. immediate fertility desire'),
    'outpartner':fields.boolean('v. outside partner HIV infected with unknown or unsuppressed viral load'),
    'notadherent':fields.boolean('vi. index not adherent to ART'),
    'nottakenprep':fields.boolean('vii. has not taken PrEP since the last scheduled quarterly visit'),
    'other':fields.boolean('viii. Other:'),
	'onarvsnow':fields.boolean('my partner is on ARVs now'),
	'other2':fields.boolean('Other:'),
	'stopprep':fields.selection([('yes','Yes'),('no','No')],'4. Are you concerned about stopping PrEP?'),
	'stoporstay':fields.selection([('yes','Yes'),('no','No')],'5. If you could choose, would you prefer to stop PrEP or stay on PrEP?'),
	'moreconc':fields.selection([('more_concern','more concern'),('less_concern','less concern'),('No_change','No change in concern')],'6. Now that you are stopping PrEP, do you have more concerns about getting HIV than you had while you were getting PrEP?'),
	'mreoften':fields.selection([('more_often','more often'),('less_often','less often'),('No_change','No change')],'7. Do you think you will have sex with your partner more or less often now that you are not using PrEP?'),
	'moreoften':fields.selection([('more_often','more often'),('less_often','less often'),('No_change','No change')],'8. Do you think you will use condoms with your partner more or less often now that you are not using PrEP?'),
	'verypoor':fields.selection([('very_poor','very poor'),('poor','poor'),('fair','fair'),('good','good'),('very_good','very good'),('excellent','excellent'),('Don\'t_know','Don\'t know')],'9. How well do you think your study partner has taken his / her ARVs?'),
    } 
