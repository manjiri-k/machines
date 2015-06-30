from openerp.osv import fields, osv

class machines_machines(osv.osv):
    _name="machines.machines"
    _rec_name="machine_name"
    
    _columns={'machine_name':fields.char(string='machine_name',size=50),
              'sheet_supported':fields.one2many('p_q','sheet',string='sheets supported by machine')
              }
    

class sheet_sheet(osv.osv):
    _name='sheet.sheet' 
    _rec_name="sheet_type" 
    _columns={"sheet_type":fields.char(string='sheet type'),
              
              }
    
class sheet_price_quantity(osv.osv):
    _name='p_q'
    _columns={'sheet_list':fields.many2one('sheet.sheet',string='sheet list'),
              "price":fields.float(string="price"),
              "quantity":fields.integer(string="quantity"),
              'sheet':fields.many2one('machines.machines'),

              }

    