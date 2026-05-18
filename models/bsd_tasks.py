from odoo import models,fields,api

class BsdTasks(models.Model):
    _name = "bsd.tasks"
    _description = "any"
    _rec_name = "reference"
    _log_access = False
    
    user_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user.id ,readonly=True)
    active = fields.Boolean(default=True)
    reference = fields.Char(string='Reference', required=True, copy=False, readonly=True, default='New')
    ticket_date = fields.Date(string='Date', default=fields.Date.today)
    task_duration = fields.Selection(
        string='Duration',
        selection=[('day','Day'),('week','Week'),('mounth','Mounth'),('year','Year')],
        help="Type is used duration",
        default="day"
        )
    line_ids = fields.One2many('bsd.tasks.line','user_id')
  
    
    ticket_done = fields.Selection(
            string='Ticket Done',
            selection=[('draft','Draft'),('in progres','In Progres'),('done','Done')],
            compute='_isDone',
            store=True
            )
                
    @api.depends('line_ids', 'line_ids.task_row_is_done')
    def _isDone(self):
        for rec in self:
            if not rec.line_ids:
                rec.ticket_done = 'draft'
                continue
            all_rows_status = [line.task_row_is_done for line in rec.line_ids]
            if all_rows_status and all(all_rows_status):
                rec.ticket_done = 'done'
            else:
                rec.ticket_done = 'in progres'
                
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('reference', 'New') == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('bsd.tasks') or 'New'
        
        return super(BsdTasks, self).create(vals_list)
    


class BsdTasksLine(models.Model):
    _name = "bsd.tasks.line"
    _description = "any"
    _log_access = False
    
    user_id = fields.Many2one('bsd.tasks')
    task_prompt = fields.Char()
    task_row_is_done = fields.Boolean(default=False)