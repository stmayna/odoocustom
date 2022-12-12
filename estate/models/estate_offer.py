# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero
import pdb


class EstatePropertyOffer(models.Model):

    # ---------------------------------------- Private Attributes -------------------------------------

    _name = 'estate.property.offer'
    _description = 'estate.property.offer'
    _order = "price desc"
    _sql_constraints = [
        ('check_price', 'CHECK(price >= 0)',
         'The offer price must be strictly positive.')
    ]

    # ---------------------------------------- Fields Declaration -------------------------------------

    price = fields.Float()
    state = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate', required=True)
    validity = fields.Integer(string='Validity (days)', default=7)
    date_deadline = fields.Date(
        compute='_compute_date_deadline', inverse='_inverse_date_deadline')
    property_type_id = fields.Many2one(
        'estate.property.type', related='property_id.property_type_id', string="Property Type", store=True)

    # ---------------------------------------- Compute methods ------------------------------------

    @api.depends('validity', 'create_date')
    def _compute_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline = date + relativedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.validity = (offer.date_deadline - date).days

    # ---------------------------------------- Action Methods -------------------------------------

    def action_accept(self):
        if 'accepted' in self.mapped('property_id.offer_ids.state'):
            raise UserError("An offer as already been accepted.")
        self.write({'state': 'accepted'})

        return self.mapped("property_id").write(
            {
                "state": "offer_accepted",
                "selling_price": self.price,
                "buyer_id": self.partner_id.id,
            }
        )

    def action_refuse(self):
        return self.write({'state': 'refused'})

    # ------------------------------------------ CRUD Methods -------------------------------------

    @api.model
    def create(self, vals):
        if vals.get("property_id") and vals.get("price"):
            prop = self.env["estate.property"].browse(vals["property_id"])
            # We check if the offer is higher than the existing offers
            if prop.offer_ids:
                max_offer = max(prop.mapped("offer_ids.price"))
                if float_compare(vals["price"], max_offer, precision_rounding=0.01) <= 0:
                    raise UserError(
                        "The offer must be higher than %.2f" % max_offer)
            prop.state = "offer_received"
        return super().create(vals)
