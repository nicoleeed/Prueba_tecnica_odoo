/** @odoo-module **/
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";  

patch(PosStore.prototype, {
    async addProductToCurrentOrder(product, options = {}) {
            //  _                      _  
            // |_) ._     _  |_   _.    ) 
            // |   | |_| (/_ |_) (_|   /_ 
            
        console.log('product', product.display_name);
        console.log('product.list_price', product.lst_price);
        if (product.lst_price == 0) {
            await this.popup.add(ErrorPopup, {
                title: _t("Producto sin precio"),
                body: _t("El precio del %s es 0.", product.display_name),
            });
            console.log('Producto sin precio');
            console.log('product.list_price', product.lst_price);
            return 
        }
        // Call the parent method
        return super.addProductToCurrentOrder(product, options);
    },
});
