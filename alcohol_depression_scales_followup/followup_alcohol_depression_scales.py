from openerp.osv import osv, fields
from openerp import tools

class followup_alcoholdepression(osv.Model):
    _name = "followup.alcoholdepression"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'feelingafterdrinking' : fields.selection([('yes','YES'),('no','NO')],'1. During the last year, have you had a feeling of guilt or remorse after drinking?'),
        'remember' : fields.selection([('yes','YES'),('no','NO')],'2. During the last year, has a friend or family member ever told you about things you said or did while you were drinking that you could not remember?'),
        'failedbecauseofdrinking' : fields.selection([('yes','YES'),('no','NO')],'3. During the last year, have you failed to do what was normally expected of you because of drinking?'),
        'firstgetup' : fields.selection([('yes','YES'),('no','NO')],'4. Do you sometimes take a drink in the morning when you first get up?'),
        'lowinenergy' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'5. Feeling low in energy, slowed down'),
        'blamingyourself' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'6. Blaming yourself for things'),
        'cryingeasily' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'7. Crying easily'),
        'feelingfidgety' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'8. Feeling fidgety'),
        'poorappetite' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'9. Poor appetite'),
        'stayingasleep' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'10. Difficulty falling asleep or staying asleep'),
        'feelinghopeless' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'11. Feeling hopeless about the future'),
        'feelingsad' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'12. Feeling sad'),
        'feelinglonely' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'13. Feeling lonely'),
        'endingyourlife' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'14. Thoughts of ending your life'),
        'worryingtoomuch' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'15. Worrying too much about things'),
        'feelingnointerest' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'16. Feeling no interest in things'),
        'feelingeverything' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'17. Feeling everything is an effort'),
        'feeling_wortless' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'18. Feeling of worthlessness'),
        'lossofsexual' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],'19. Loss of sexual interest or sexual pleasure'),
        'dontcare' : fields.selection([('not_at_all','not at all'),('a_little','a little'),('quite_a_bit','quite a bit'),('extremely','extremely')],"20. Feeling like I dont care what happens to my health"), 
        'sexsafe' : fields.selection([('yes','Yes'),('no','No'),('maybe','Maybe'),('na','NA')],'21. Do you think the anti-HIV medication you are taking or your partner is taking makes sex completely safe from HIV?'),
        } 
