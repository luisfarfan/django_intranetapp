define(['./roles.model.js', '../../helper.inei.js'], function (_rolesModel, _helperInei) {
    'use strict';

    var _rolesModel2 = _interopRequireDefault(_rolesModel);

    function _interopRequireDefault(obj) {
        return obj && obj.__esModule ? obj : {
            default: obj
        };
    }

    var objectHelper = new _helperInei.ObjectHelper();
    var rolesModel = new _rolesModel2.default();
    var roles = [];
    var rol_selected = [];

    function getAllRoles() {
        rolesModel.get().done(response => {
            roles = response;
            drawRoles();
        });
    }
    function drawRoles() {
        let html = '';
        roles.map((value, key) => {
            html += `<tr onclick="getDetalle(this,${value.id})">
                    <td>${parseInt(key) + 1}</td>
                    <td>${value.nombre}</td>
                    <td><span class="label label-success">Activo</span></td>
                </tr>`;
        });
        $('#table_roles').find('tbody').html(html);
    }

    getAllRoles();
});