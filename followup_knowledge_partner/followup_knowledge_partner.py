from openerp.osv import osv, fields
from openerp import tools

class followup_knowldgepartner(osv.Model):
    _name = "followup.knowldgepartner"
    _columns = {
    'visit_date':fields.date('Visit date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
    'sexualintercourse':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')], "a. Sexual intercourse with person who has HIV"),
    'bloodtransfusion':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"b. Blood transfusion with blood from person who has HIV"),
    'mothertochild':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"c. Mother to unborn child"),
    'sharingtoilet':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"d. Sharing toilets with person who has HIV"),
    'sharingobject':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"e. Sharing sharp objects like razors with person who has HIV"),
    'sharingneedles':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"f. Sharing needles with person who has HIV"),
    'sharingfood':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"g. sharing food with person who has HIV"),
    'sharingutensil':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"h. Sharing eating utensils with person who has HIV"),
    'mosquitobite':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"i. being bitten by an infected mosquito"),
    'witchcraft':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"j. Witchcraft"),
    'kissing':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"k. Kissing"),
    'hugging':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"l. Hugging"),
    'avoidsharing':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"a. Avoid sharing of sharp objects like needles, razors with your partner"),
    'praying':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"b. Praying to God"),
    'abstfromsex':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"c. Abstaining from sex with your partner"),
    'usingcondom':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"d. Using condom during every sexual intercourse with your partner"),
    'useantibiotics':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"e. Use antibiotics"),
    'traditionalheal':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"f. Seek protection from traditional healers"),
    'doingnothin':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"g. Doing nothing"),
    'circumcision':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"h. Circumcision"),
    'takingprep':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"i. Taking PrEP everyday"),
    'preptimetotime':fields.selection([('yes','Yes'),('no','No'),('dont_know','dont know')],"j.Taking PrEP time to time"),
    } 
