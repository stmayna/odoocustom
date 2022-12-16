# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import ValidationError
from heyoo import WhatsApp


class WhatsappInt(models.Model):

    # ---------------------------------------- Private Attributes -------------------------------------

    _inherit = 'res.partner'

    # ---------------------------------------- Fields Declaration -------------------------------------

    wa_name = fields.Char()
    wa_number = fields.Char()

    def send_message(self):
        if not self.phone:
            raise ValidationError("Missing phone number.")
        message = "Hi {name}!".format(name=self.name)
        wa_redirect_share = 'https://api.whatsapp.com/send?phone={phone}&text={message}'.format(
            phone=self.phone, message=message)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': wa_redirect_share
        }
