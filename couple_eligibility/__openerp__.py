{
    "name" : "The PROJECT Study Couple Eligibility Worksheet",
    "version" : "1.0",
    "author" : "MgB Computers",
    "website" : "http://www.mgbcomputers.com",
    "category": "Screening",
    "complexity": "easy",
    "description": """couple_eligibility.
        Additional Partner Fields 
                    """,
    "depends" : ["base","crm","custom_naca"],
    "data" : [
            "couple_eligibility_view.xml",
            'security/ir.model.access.csv',
    ],


    "installable": True,
    "auto_install": False,
    "application": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: