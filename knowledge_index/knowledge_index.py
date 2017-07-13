from openerp.osv import osv, fields
from openerp import tools

class knowledge_index(osv.Model):
    _name = "knowledge.index"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'intercourse' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'a. Sexual intercourse with person who has HIV'),
        'transfusion' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'b. Blood transfusion with blood from person who has HIV'),
        'unborn' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'c. Mother to unborn child'),
        'toilets' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'d. Sharing toilets with person who has HIV'),
        'objects' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'e. Sharing sharp objects like razors with person who has HIV'),
        'needles' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'f. Sharing needles with person who has HIV'),
        'food' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'g. sharing food with person who has HIV'),
        'utensils' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'h. Sharing eating utensils with person who has HIV'),
        'bitten' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'i. being bitten by an infected mosquito'),
        'witchcraft' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'j. Witchcraft'),
        'kissing' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'k. Kissing'),
        'hugging' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'l. Hugging'),
        'sharp' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'a. Avoid sharing of sharp objects like needles, razors with your partner'),
        'praying' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'b. Praying to God'),
        'abstaining' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'c. Abstaining from sex with your partner'),
        'condom' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'d. Using condom every sexual intercourse with your partner'),
        'antibiotics' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'e. Use antibiotics'),
        'protection' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'f. Seek protection from traditional healers'),
        'nothing' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'g. Doing nothing'),
        'circumcision' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'h. Circumcision'),
        'PrEPeveryday' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'i. Taking PrEP everyday'),
        'PrEPtime' : fields.selection([('yes','YES'),('no','NO'),('idk','Dont know')],'j. Taking PrEP sometimes'),
    }
