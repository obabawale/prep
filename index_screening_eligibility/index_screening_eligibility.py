#!/usr/bin/env python
# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp import tools

class index_screening(osv.Model):
    _name = "index.screening"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'theparticipant' : fields.selection([('yes','YES'),('no','NO')],'1. Is the participant ≥18 years old as at last birthday?'),
        'participantwilling' : fields.selection([('yes','YES'),('no','NO')],'2. Is the participant willing and able to provide independent, written, informed consent for screening?'),
        'informedconsent' : fields.date('2a. When was the informed consent for screening marked or signed?'),
        'locatorinformation' : fields.selection([('yes','YES'),('no','NO')],'3. Is the participant willing and able to provide adequate locator information?'),
        'clinicalevaluations' : fields.selection([('yes','YES'),('no','NO')],'4. Is the participant willing and able to undergo clinical evaluations, and adhere to the follow-up schedule?'),
        'HIVnegative' : fields.selection([('yes','YES'),('no','NO')],'5. Is the participant HIV infected?'),
        'undergoclinical' : fields.selection([('yes','YES'),('no','NO')],'6. Do you plan to maintain a relationship with your study partner for the next 12 months?'),
        'vaginaland' : fields.selection([('yes','YES'),('no','NO')],'7. Whenever \"sex\" or \"sexual intercourse\" is stated, it includes vaginal and anal sex, but not oral sex. \
Have you had sex with your study partner at least six times in the last three months?'),
        'beendiagnosed' : fields.selection([('yes','YES'),('no','NO')],'8. Has the participant ever been diagnosed with a WHO stage 3 or 4 condition?'),
        'treatmenttrial' : fields.selection([('yes','YES'),('no','NO')],'9. Is the participant currently enrolled in any other HIV treatment trial?'),
        'antiretroviral' : fields.selection([('yes','YES'),('no','NO')],'10. Is the participant currently taking antiretroviral therapy (ARVs) and viral is ≤5000 copies?'),
        'laboratory' : fields.selection([('yes','YES'),('no','NO')],'11. Does the participant have any laboratory indications of renal pathologies?'),
        'TBinfection' : fields.selection([('yes','YES'),('no','NO')],'12. Does the participant have any evidence of TB infection?'),
        'activehepatitis' : fields.selection([('yes','YES'),('no','NO')],'13. Does the participant have any evidence of active hepatitis infection?'),
        'conditionthat' : fields.selection([('yes','YES'),('no','NO')],'14. Does the participant have any condition that, in the opinion of the site investigator or designee, would preclude provision of informed consent, make participation in the study unsafe, complicate interpretation of study outcome data, or otherwise interfere with achieving the study objectives?'),
        'criteriaabove' : fields.selection([('yes','YES'),('no','NO')],'15. Based on the criteria above, is the participant eligible?'),
        } 
