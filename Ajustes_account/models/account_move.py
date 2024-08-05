from odoo import models, fields, api
import qrcode
import base64
import io

class AccountMove(models.Model):
    _inherit = 'account.move'

    #  _                           
    # |_) ._     _  |_   _.   |_|_ 
    # |   | |_| (/_ |_) (_|     |  
                              
                              
    x_qr_invoice = fields.Binary(
        string="QR Code",
        compute="_generate_qr_code")

    def generate_qr_code(self, qr_string):
        qr = qrcode.QRCode(version=4, box_size=4, border=1)
        qr.add_data(qr_string)
        qr.make(fit=True)
        img = qr.make_image()
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue())
        return img_str

    @api.depends('invoice_line_ids', 'amount_total')
    def _generate_qr_code(self):
        for record in self:
            qr_string = f"{record.name}|{record.partner_id.name}|{record.invoice_date}|{sum(line.quantity for line in record.invoice_line_ids)}|{record.amount_total}"
            record.x_qr_invoice = self.generate_qr_code(qr_string)
    
    #  _                       _  
    # |_) ._     _  |_   _.   |_  
    # |   | |_| (/_ |_) (_|    _) 
                                
    serial_number = fields.Char(
        string='Número de Serie',
        compute='_compute_serial_correlativo')
    correlative_number = fields.Char(
        string='Número Correlativo', 
        compute='_compute_serial_correlativo')
    
    @api.depends('name')
    def _compute_serial_correlativo(self):
        for move in self:
            if move.name:
                parts = move.name.split('/')
                move.serial_number = parts[0] + parts[1] if len(parts) >= 2 else ''
                move.correlative_number = parts[2].zfill(8) if len(parts) >= 3 else ''
            else:
                move.serial_number = ''
                move.correlative_number = ''
    
    #  _                       _  
    # |_) ._     _  |_   _.   |_  
    # |   | |_| (/_ |_) (_|   |_) 
    
    sale_channel_id = fields.Many2one(
        comodel_name='sale.channel',
        string='Canal de venta',
    )
    
    
    #  _                      __ 
    # |_) ._     _  |_   _.    / 
    # |   | |_| (/_ |_) (_|   /  
                            
    invoice_date_time = fields.Datetime(
        string='Fecha de emisión',
        default=fields.Datetime.now,
        required=True
    )

    #  _                       _  
    # |_) ._     _  |_   _.   (_| 
    # |   | |_| (/_ |_) (_|     | 
                             
    
    picking_ids = fields.Many2many(
        comodel_name='stock.picking',
        string='Transferencias',
        compute='_compute_picking_ids',
        store=True
    )
    @api.depends('name')
    def _compute_picking_ids(self):
        for move in self:
            if move.invoice_origin:
                sale_orders = self.env['sale.order'].search([('name', '=', move.invoice_origin)])
                move.picking_ids = sale_orders.mapped('picking_ids')
            else:
                move.picking_ids = False
            
