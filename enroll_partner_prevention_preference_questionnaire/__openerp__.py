{
    "name" : "Partner Prevention Preference Questionnaire",
    "version" : "1.0",
    "author" : "MgB Computers",
    "website" : "http://www.mgbcomputers.com",
    "category": "Others",
    "complexity": "easy",
    "description": """Partner Prevention Preference Questionnaire.
        Additional Partner Fields 
                    """,
    "depends" : ["base","crm","custom_naca"],
    "data" : [
        "partner_prevention_preference_questionnaire_view.xml",
        'security/ir.model.access.csv',
        ],
    "installable": True,
    "auto_install": False,
    "application": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
