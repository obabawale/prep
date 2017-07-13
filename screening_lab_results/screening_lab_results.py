#!/usr/bin/env python
# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp import tools

class screeninglab_results(osv.Model):
    _name = "screeninglab.results"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id': fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id': fields.char(string="Screening ID", related='partner_id.name'),
        'specimen' : fields.date('Specimen collection date'),
        'hiv_status_national_algo' : fields.selection([
            ('negative','Negative'),
            ('positive','Positive'),
            ('indeterminate','Indeterminate')
            ],"2. HIV status by national algorithm"),
        'collectiondate' : fields.date('Specimen collection date'),
        'hepatitisb' : fields.selection([('neg','Negative'),('pos','Positive')],'4. Hepatitis B surface antigen (HBsAg):'),
        'creatinine' : fields.float('5. Creatinine(μmol/L)'),
        'creatinineclearance' : fields.float('6. Creatinine clearance(ml/min)'),
        'specimencollection' : fields.date('7. Specimen collection date'),
        'CD4' : fields.integer('8. CD4 count(/μL)'),
        'viralload' : fields.integer('9. Viral load(Copies/ml)'),
        'comm' : fields.text('Comments'),
    }
