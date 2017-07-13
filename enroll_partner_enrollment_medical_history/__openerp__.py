{
    "name" : "Partner Enrollment Medical History",
    "version" : "1.0",
    "author" : "MgB Computers",
    "website" : "http://www.mgbcomputers.com",
    "category": "Others",
    "complexity": "easy",
    "description": """Partner Enrollment Medical History.
        Additional Partner Fields 
                    """,
    "depends" : ["base","crm","custom_naca"],
    "data" : [
        "partner_enrollment_medical_history_view.xml",
        'security/ir.model.access.csv',
        ],
    "installable": True,
    "auto_install": False,
    "application": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
