# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models


class ProjectSolutionTags(models.Model):

    _name = 'project.solution.tag'
    _description = "Project Solution Tags"

    name = fields.Char(
        string='Name',
        required=True
    )

    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
