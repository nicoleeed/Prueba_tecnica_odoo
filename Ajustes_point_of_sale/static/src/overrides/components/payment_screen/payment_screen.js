/**@odoo-module **/
import { _t } from "@web/core/l10n/translation";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { ConfirmPopup } from "@point_of_sale/app/utils/confirm_popup/confirm_popup";
import { patch } from "@web/core/utils/patch";
patch(PaymentScreen.prototype, {
    
    //  _                      _  
    // |_) ._     _  |_   _.   _) 
    // |   | |_| (/_ |_) (_|   _) 
                            
    
    async onClick() {    
        this.popup.add(ConfirmPopup, {
            title: _t("Boleta"),
            body: _t("Total: %s", this.env.utils.formatCurrency(this.currentOrder.get_total_with_tax())),
        });
	
}})
