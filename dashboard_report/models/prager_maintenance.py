
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo import api, exceptions, fields, models, _, tools



class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'




class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'



class MaintenanceEquipmentSummary(models.Model):
    _name = 'maintenance.equipment.summary'
    _description = 'Maintenance Equipment Summary'
    _auto = False

    equipment_id = fields.Many2one('maintenance.equipment', string='Equipment')
    total_mr = fields.Float('Total MR')
    total_duration = fields.Float('Total Duration')
    
    

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute('''
            CREATE OR REPLACE VIEW %s AS (
                    select
                    me.id,
                    me.id equipment_id,
                    count(*) total_mr,
                    sum(duration) total_duration
                    from
                    (select * from maintenance_equipment where active = True) me 
                    inner join
                    maintenance_request mr on mr.equipment_id = me.id group by me.id
            )''' % (self._table,)
        )


    


    




    

