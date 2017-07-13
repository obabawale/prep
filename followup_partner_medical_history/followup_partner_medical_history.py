from openerp.osv import osv, fields
from openerp import tools

class followup_partner_medical_history(osv.Model):
    _name = "followuppartner.medicalhistory"
    _columns = {
    'visitdate' : fields.date('Visit Date'),
    'partner_id': fields.many2one('res.partner', 'Sceening ID'),
    'sceening_id': fields.char(string="Screening ID", related='partner_id.name'),

    'fever_yes':fields.boolean('yes'),
    'fever_no':fields.boolean('no'),
    'fever_dont_know':fields.boolean('don\'t know'),
    'fever_no_of_days':fields.integer('No of Days'),
    'fever_ongoing_yes':fields.boolean('yes'),
    'fever_ongoing_no':fields.boolean('yes'),

    'fatigue_yes':fields.boolean('yes'),
    'fatigue_no':fields.boolean('no'),
    'fatigue_dont_know':fields.boolean('don\'t know'),
    'fatigue_no_of_days':fields.integer('No of Days'),
    'fatigue_ongoing_yes':fields.boolean('yes'),
    'fatigue_ongoing_no':fields.boolean('yes'),

    'soreThroat_yes':fields.boolean('yes'),
    'soreThroat_no':fields.boolean('no'),
    'soreThroat_dont_know':fields.boolean('don\'t know'),
    'soreThroat_no_of_days':fields.integer('No of Days'),
    'soreThroat_ongoing_yes':fields.boolean('yes'),
    'soreThroat_ongoing_no':fields.boolean('yes'),

    'rash_yes':fields.boolean('yes'),
    'rash_no':fields.boolean('no'),
    'rash_dont_know':fields.boolean('don\'t know'),
    'rash_no_of_days':fields.integer('No of Days'),
    'rash_ongoing_yes':fields.boolean('yes'),
    'rash_ongoing_no':fields.boolean('yes'),

    'headache_yes':fields.boolean('yes'),
    'headache_no':fields.boolean('no'),
    'headache_dont_know':fields.boolean('don\'t know'),
    'headache_no_of_days':fields.integer('No of Days'),
    'headache_ongoing_yes':fields.boolean('yes'),
    'headache_ongoing_no':fields.boolean('yes'),

    'short_breath_yes':fields.boolean('yes'),
    'short_breath_no':fields.boolean('no'),
    'short_breath_dont_know':fields.boolean('don\'t know'),
    'short_breath_no_of_days':fields.integer('No of Days'),
    'short_breath_ongoing_yes':fields.boolean('yes'),
    'short_breath_ongoing_no':fields.boolean('yes'),

    'abdominal_pain_yes':fields.boolean('yes'),
    'abdominal_pain_no':fields.boolean('no'),
    'abdominal_pain_dont_know':fields.boolean('don\'t know'),
    'abdominal_pain_no_of_days':fields.integer('No of Days'),
    'abdominal_pain_ongoing_yes':fields.boolean('yes'),
    'abdominal_pain_ongoing_no':fields.boolean('yes'),

    'nausea_yes':fields.boolean('yes'),
    'nausea_no':fields.boolean('no'),
    'nausea_dont_know':fields.boolean('don\'t know'),
    'nausea_no_of_days':fields.integer('No of Days'),
    'nausea_ongoing_yes':fields.boolean('yes'),
    'nausea_ongoing_no':fields.boolean('yes'),

    'vomiting_yes':fields.boolean('yes'),
    'vomiting_no':fields.boolean('no'),
    'vomiting_dont_know':fields.boolean('don\'t know'),
    'vomiting_no_of_days':fields.integer('No of Days'),
    'vomiting_ongoing_yes':fields.boolean('yes'),
    'vomiting_ongoing_no':fields.boolean('yes'),

    'diarrhea_yes':fields.boolean('yes'),
    'diarrhea_no':fields.boolean('no'),
    'diarrhea_dont_know':fields.boolean('don\'t know'),
    'diarrhea_no_of_days':fields.integer('No of Days'),
    'diarrhea_ongoing_yes':fields.boolean('yes'),
    'diarrhea_ongoing_no':fields.boolean('yes'),

    'excess_intestinalgas_yes':fields.boolean('yes'),
    'excess_intestinalgas_no':fields.boolean('no'),
    'excess_intestinalgas_dont_know':fields.boolean('don\'t know'),
    'excess_intestinalgas_no_of_days':fields.integer('No of Days'),
    'excess_intestinalgas_ongoing_yes':fields.boolean('yes'),
    'excess_intestinalgas_ongoing_no':fields.boolean('yes'),

    'urinary_output_yes':fields.boolean('yes'),
    'urinary_output_no':fields.boolean('no'),
    'urinary_output_dont_know':fields.boolean('don\'t know'),
    'urinary_output_no_of_days':fields.integer('No of Days'),
    'urinary_output_ongoing_yes':fields.boolean('yes'),
    'urinary_output_ongoing_no':fields.boolean('yes'),

    'muscle_weakness_yes':fields.boolean('yes'),
    'muscle_weakness_no':fields.boolean('no'),
    'muscle_weakness_dont_know':fields.boolean('don\'t know'),
    'muscle_weakness_no_of_days':fields.integer('No of Days'),
    'muscle_weakness_ongoing_yes':fields.boolean('yes'),
    'muscle_weakness_ongoing_no':fields.boolean('yes'),

    'swelling_feet_yes':fields.boolean('yes'),
    'swelling_feet_no':fields.boolean('no'),
    'swelling_feet_dont_know':fields.boolean('don\'t know'),
    'swelling_feet_no_of_days':fields.integer('No of Days'),
    'swelling_feet_ongoing_yes':fields.boolean('yes'),
    'swelling_feet_ongoing_no':fields.boolean('yes'),

    'joint_pain_yes':fields.boolean('yes'),
    'joint_pain_no':fields.boolean('no'),
    'joint_pain_dont_know':fields.boolean('don\'t know'),
    'joint_pain_no_of_days':fields.integer('No of Days'),
    'joint_pain_ongoing_yes':fields.boolean('yes'),
    'joint_pain_ongoing_no':fields.boolean('yes'),

    'bone_pain_yes':fields.boolean('yes'),
    'bone_pain_no':fields.boolean('no'),
    'bone_pain_dont_know':fields.boolean('don\'t know'),
    'bone_pain_no_of_days':fields.integer('No of Days'),
    'bone_pain_ongoing_yes':fields.boolean('yes'),
    'bone_pain_ongoing_no':fields.boolean('yes'),

    'bone_fracture_yes':fields.boolean('yes'),
    'bone_fracture_no':fields.boolean('no'),
    'bone_fracture_dont_know':fields.boolean('don\'t know'),
    'bone_fracture_no_of_days':fields.integer('No of Days'),
    'bone_fracture_ongoing_yes':fields.boolean('yes'),
    'bone_fracture_ongoing_no':fields.boolean('yes'),

    'numbness_yes':fields.boolean('yes'),
    'numbness_no':fields.boolean('no'),
    'numbness_dont_know':fields.boolean('don\'t know'),
    'numbness_no_of_days':fields.integer('No of Days'),
    'numbness_ongoing_yes':fields.boolean('yes'),
    'numbness_ongoing_no':fields.boolean('yes'),

    'others_yes':fields.boolean('yes'),
    'others_no':fields.boolean('no'),
    'others_dont_know':fields.boolean('don\'t know'),
    'others_no_of_days':fields.integer('No of Days'),
    'others_ongoing_yes':fields.boolean('yes'),
    'others_ongoing_no':fields.boolean('yes'),

    'circumcised_yes':fields.boolean('yes'),
    'circumcised_no':fields.boolean('no'),
    'circumcised_dont_know':fields.boolean('don\'t know'),
    'circumcised_no_of_days':fields.integer('No of Days'),
    'circumcised_ongoing_yes':fields.boolean('yes'),
    'circumcised_ongoing_no':fields.boolean('yes'),
    } 