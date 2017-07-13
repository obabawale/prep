from openerp.osv import osv, fields
from openerp import tools

class followuppartner_drugdispensing(osv.Model):
    _name = "followuppartner.drugdispensing"
    _columns = {
        'visitdate' : fields.date('Visit Date'),
        'partner_id' : fields.many2one('res.partner', 'Sceening ID'),
        'sceening_id' : fields.char(string="Sceening ID", related='partner_id.name'),
        'neveraccepted' : fields.boolean('never accepted study PrEP'),
	    'enrolment' : fields.boolean('Enrolment'),
	    'retbottles' : fields.char('Number of bottles returned'),
	    'retpills' : fields.char('Number of pills returned'),
	    'leftpills' : fields.char('Number of pills left at home'),
	    'disbottles' : fields.char('Number of bottles dispensed'),
	    'whynodispense' : fields.char('Why were no bottles dispensed?'),
	    'memsno' : fields.char("MEMS cap number"),
	    'mems_data_upload' : fields.selection([('yes','Yes'),('no','No')],'4. Were MEMS data uploaded?'),
	    'lost' : fields.boolean('i. lost /stolen'),
	    'malfunctioning' : fields.boolean('ii. malfunctioning'),
	    'mems_others' : fields.boolean('iii. Others'),
	    'replacement_cap' : fields.selection([('yes','Yes'),('no','No')],'5 Was a replacement cap dispensed today?'),
	    'cap_number' : fields.char('a New cap number:'),
	    'reason_dispensed_lost' : fields.boolean('i. lost /stolen'),
	    'reason_dispensed_malfunction' : fields.boolean ('ii. malfunctioning'),
		'reason_dispensed_Others': fields.boolean ('iii. Others'),
		'cap_returned' : fields.selection([('yes','Yes'),('no','No'),],'6 Was a previously dispensed cap returned today?'),
		'returned_cap_no' : fields.char('a Returned cap number:'),
		'med_bottle_open' : fields.integer('7. Since the last visit, how many times have you or someone else opened your special medication bottle without taking any tablets out of it?'),
		'taken_more_tablet' : fields.integer('8 Since the last visit, how many times have you taken more than one tablet out of your special medication bottle at a time?'),
		'extra_tablets' : fields.integer('8a Since the last visit, how many extra tablets in total have you taken out of your special medication bottle? Do not include the tablet taken out to be used that day.'),
	
  
    } 
