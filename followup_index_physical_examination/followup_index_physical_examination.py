#!/usr/bin/env python
# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp import tools

class followup_indexphysicalexam(osv.Model):
    _name = "followup.indexphysicalexam"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Screening ID", related='partner_id.name'),
	   'height': fields.float('1. Height(Enrollment only)'),
        'weight' : fields.float('2. Weight(kg)'),
        'temperature' : fields.integer('3. Temperature(°C)'),
        'bloodpressure' : fields.char('4. Blood pressure(mgHg)'),
        'respiratoryrate' : fields.char('5. Respiratory rate(/min)'),
        'pulserate' : fields.char('6. Pulse rate(/min)'),
        'genital' : fields.selection([('yes','YES'),('no','NO'),('not_done','Not done')],'7. Genital ulcer disease (GUD)'),
        'vaginitis' : fields.selection([('yes','YES'),('no','NO'),('not_done','Not done')],'8. Vaginitis or vaginal discharge'),
        'cervicitis' : fields.selection([('yes','YES'),('no','NO'),('not_done','Not done')],'9. Cervicitis or cervical discharge'),
        'pelvic' : fields.selection([('yes','YES'),('no','NO'),('not_done','Not done')],'10. Pelvic inflammatory disease (PID)'),
	   'urethral_discharge' : fields.selection([('yes','YES'),('no','NO'),('not_done','Not done')],'11. Urethritis or urethral discharge.'),
        'circumcision' : fields.selection([('Fully_circumcised','Fully circumcised'),('Partially_circumcised','Partially circumcised'),('not_circumcised','Not circumcised')],'12. Circumcision status'),
        'treatmentgiven' : fields.selection([('yes','Yes'),('no','No'),('maybe','Maybe')],'13. Treatment given for a genital tract infection?'),
        'listmedications' : fields.text('13 a. List medications'),
        'gingivitis' : fields.boolean('gingivitis/periodontitis'),
        'thrush' : fields.boolean('Thrush'),
        'ulcer' : fields.boolean('Ulcer'),
        'oralhairy' : fields.boolean('oral hairy leukoplakia'),
        'kaposi' : fields.boolean('Kaposi Sarcoma'),
        'Others' : fields.boolean('Others'),
        'generalized' : fields.boolean('generalized skin rash'),
        'kaposisarcoma' : fields.boolean('Kaposi Sarcoma'),
        'zoster' : fields.boolean('Zoster'),
        'Others2' : fields.boolean('Others'),
        'lymphnode' : fields.selection([('yes','YES'),('no','NO')],'16. Lymph node enlargement?'),
        'cervical' : fields.boolean('Cervical'),
        'inguinal' : fields.boolean('Inguinal'),
        'axillary' : fields.boolean('Axillary'),
        'Others3' : fields.char('Others (specify):'),
        'sizeof' : fields.integer('b. Size of largest lymph node (cm)'),
     } 
