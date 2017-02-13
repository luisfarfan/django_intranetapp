define(['exports'], function (exports) {
    'use strict';

    Object.defineProperty(exports, "__esModule", {
        value: true
    });
    /**
     * Created by lfarfan on 12/02/2017.
     */
    class MenuAplicacionesModel {
        constructor() {
            this.url = `${BASEURL}/rest_modulousuario/rol/`;
            this.url_rol_modulo = `${BASEURL}/rest_modulousuario/modulos_rol/`;
        }

        get(pk = null) {
            return $.ajax({
                url: pk == null ? this.url_rol_modulo : `${this.url_rol_modulo}${pk}/`,
                type: 'GET'
            });
        }

        update(pk, obj) {
            return $.ajax({
                url: `${this.url}${pk}/`,
                type: 'PUT',
                data: obj
            });
        }

        add(obj) {
            return $.ajax({
                url: `${this.url}`,
                type: 'POST',
                data: obj
            });
        }

        delete(pk) {
            return $.ajax({
                url: `${this.url}${pk}/`,
                type: 'DELETE'
            });
        }
    }
    exports.default = MenuAplicacionesModel;
});