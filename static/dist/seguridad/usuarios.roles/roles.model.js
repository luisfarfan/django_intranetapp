define(['exports'], function (exports) {
    'use strict';

    Object.defineProperty(exports, "__esModule", {
        value: true
    });
    /**
     * Created by lfarfan on 29/01/2017.
     */
    class RolesModel {
        constructor(base_url_rest = `${BASEURL}/rest_modulousuario/rol/`) {
            this.url = base_url_rest;
        }

        get(pk = null) {
            return $.ajax({
                url: pk == null ? this.url : `${this.url}${pk}/`,
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
    exports.default = RolesModel;
});