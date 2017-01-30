import RolesModel from './roles.model.js';
import {ObjectHelper} from '../../helper.inei.js';
var objectHelper = new ObjectHelper();
var rolesModel = new RolesModel();
var roles = [];
var rol_selected = [];

function getAllRoles() {
    rolesModel.get().done(response=> {
        roles = response;
        drawRoles();
    });
}
function drawRoles() {
    let html = '';
    roles.map((value, key)=> {
        html += `<tr onclick="getDetalle(this,${value.id})">
                    <td>${parseInt(key) + 1}</td>
                    <td>${value.nombre}</td>
                    <td><span class="label label-success">Activo</span></td>
                </tr>`
    });
    $('#table_roles').find('tbody').html(html);
}

getAllRoles();



