# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero


class ResUsers(models.Model):

    # ---------------------------------------- Private Attributes -------------------------------------

    _inherit = 'res.users'

    # ---------------------------------------- Fields Declaration -------------------------------------

    property_ids = fields.One2many('estate', 'user_id', string="Properties", domain=[
                                   ("state", "in", ["new", "offer_received"])])
