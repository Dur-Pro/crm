# Copyright 2016 Antiun Ingeniería S.L. - Jairo Llopis
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Firstname and Lastname in Leads",
    "summary": "Specify split names for contacts in leads",
    "version": "17.0.1.0.1",
    "category": "Customer Relationship Management",
    "description": """
Firstname and Lastname in Leads
===============================
This module adds firstname and lastname fields to leads, so you can specify
split names for contacts in leads.
    """,
    "website": "https://github.com/OCA/crm",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["crm", "partner_firstname"],
    "data": ["views/crm_lead_view.xml"],
}
