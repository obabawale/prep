#!/usr/bin/env python
# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp import tools

class partner_screening(osv.Model):
    _name = "partner.screening"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Sceening ID", related='partner_id.name'),
        'theparticipant' : fields.selection([('yes','YES'),('no','NO')],'1. Is the participant ≥  18 years old?'),
        'participantwilling' : fields.selection([('yes','YES'),('no','NO')],'2. Is the participant willing and able to provide independent, written, informed consent for screening?'),
        'informedconsent' : fields.date('2a. When was the informed consent for screening marked or signed?'),
        'locatorinformation' : fields.selection([('yes','YES'),('no','NO')],'3. Is the participant willing and able to provide adequate locator information?'),
        'clinicalevaluations' : fields.selection([('yes','YES'),('no','NO')],'4. Is the participant willing and able to undergo clinical evaluations, take study drug as directed, and adhere to the follow-up schedule?'),
        'undergoclinical' : fields.selection([('yes','YES'),('no','NO')],'5. Do you plan to maintain a relationship with your study partner for the next 12 months?'),
        'vaginaland' : fields.selection([('yes','YES'),('no','NO')],'6. Whenever \"sex\" or \"sexual intercourse\" is stated, it includes vaginal and anal sex, but not oral sex. Have you had sex with your study partner at least six times in the last three months?'),
        'HIVnegative' : fields.selection([('yes','YES'),('no','NO')],'7. HIV negative?'),
        'creatinineclearance' : fields.selection([('yes','YES'),('no','NO')],'8. Creatinine clearance ≥ 60 ml / min?'),
        'serumcreatinine' : fields.selection([('yes','YES'),('no','NO')],'9. Serum creatinine level of: ≤ 115μmol / L OR ≤ 1.30 mg / dL for men ≤ 99μmol / L  OR ≤ 1.12 mg / dL for women?'), 
        'infectedwith' : fields.selection([('yes','YES'),('no','NO')],'10. Not infected with hepatitis B? (This is defined as HBsAg negative.)'),
        'currentlyenrolled' : fields.selection([('yes','YES'),('no','NO')],'11. Is the participant currently enrolled in any other HIV vaccine or prevention trial?'),
        'conditionthat' : fields.selection([('yes','YES'),('no','NO')],'12. Does the participant have any condition that, in the opinion of the site investigator or designee, would preclude provision of informed consent, make participation in the study unsafe, complicate interpretation of study outcome data, or otherwise interfere with achieving the study objectives?'),
        'currentlypregnant' : fields.selection([('yes','YES'),('no','NO')],'13. Is the participant currently pregnant?'),
        'breastfeeding' : fields.selection([('yes','YES'),('no','NO')],'14. Is the participant currently breastfeeding?'),
        'serious' : fields.selection([('yes','YES'),('no','NO(If no, go to 16)')],'a. Active and serious infections '),
        'cardiac' : fields.selection([('yes','YES'),('no','NO(If no, go to 16)')],'b. Clinically significant cardiac disease'),
        'lung' : fields.selection([('yes','YES'),('no','NO(If no, go to 16)')],'c. Clinically significant lung disease'),
        'hypoglycemic' : fields.selection([('yes','YES'),('no','NO(If no, go to 16)')],'d. Diabetes requiring hypoglycemic medication'),
        'malignancy' : fields.selection([('yes','YES'),('no','NO(If no, go to 16)')],'e. Any malignancy expected to require further treatment'),
        'bonefractures' : fields.selection([('yes','YES'),('no','NO')],'16. History of bone fractures not related to trauma?'),
        'mayinhibit' : fields.selection([('yes','YES'),('no','NO(If no, go to 18)')],'a. Agents that may inhibit or compete for elimination via active renal tubular secretion'),
        'nephrotoxic' : fields.selection([('yes','YES'),('no','NO(If no, go to 18)')],'b. Agents with significant nephrotoxic potential'),
        'immunetherapies' : fields.selection([('yes','YES'),('no','NO(If no, go to 18)')],'c. Immune therapies'),
        'retroviraltherapy' : fields.selection([('yes','YES'),('no','NO(If no, go to 18)')],'d. Anti-retroviral therapy'),
        'investigational' : fields.selection([('yes','YES'),('no','NO(If no, go to 18)')],'e. Other investigational agents'),
        'criteriaabove' : fields.selection([('yes','YES'),('no','NO')],'18. Based on the criteria above, is the participant eligible?'),
        'comm' : fields.text('19. Comments'),
        } 
