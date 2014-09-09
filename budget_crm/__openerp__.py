# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Leonardo Pistone
#    Copyright 2014 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{"name": "Budget CRM",
 "version": "1.0",
 "author": "Camptocamp",
 "category": "Generic Modules/Accounting",
 "website": "http://camptocamp.com",
 "description": """
Budget CRM
==========

Features:

* Create and update budget lines from Opportunities

This module depends on the OCA module "budget", not on the Odoo core
account_budget module.
    """,
 "complexity": "normal",
 "depends": ["budget",
             "crm",
             ],
 "data": [
     'view/lead.xml',
     'view/team.xml',
     'view/stage.xml',
     'view/budget_line.xml',
     'view/company.xml',
     'wizard/crm_to_budget.xml',
 ],
 "test": [
     'test/setup_team.yml',
     'test/setup_user.yml',
     'test/setup_budget.yml',
     'test/test_lead_defaults.yml',
     'test/test_crm_to_budget.yml',
     'test/test_update_crm_to_budget.yml',
 ],
 "installable": True,
 }
