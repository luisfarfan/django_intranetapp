/**
 * Created by LFarfan on 20/12/2016.
 */

$(function () {
    getProyectosSiga();
    getProyectosSeguridad();
});

$('#proyectos_siga').select2({
    containerCssClass: 'bg-primary-400'
});

var proyectos_siga = [];
var proyectos_siga_selected = {};
var proyectos_seguridad = [];
var proyectos_seguridad_selected = [];

function getProyectosSiga() {
    "use strict";
    $.ajax({
        url: `${BASE_URL}/rest/getProyectosSiga/`,
        type: 'GET',
        success: response => {
            proyectos_siga = response;
            setSelect_v2('proyectos_siga', proyectos_siga, ['id', 'desc_proyecto']);
            $('#proyectos_siga').trigger('change');
        }
    })
}

$('#proyectos_siga').on('change', event => {
    "use strict";
    proyectos_siga_selected = findInObject(proyectos_siga, 'id', event.target.value);
    setTable('tbl_proyecto_siga_selected', proyectos_siga_selected, ['id', 'desc_proyecto', 'codi_meta', 'CODI_DEPE_TDE', 'annio_meta']);
    if (proyectos_siga_selected.length > 0) {
        $('#btn_agregar_proyecto').prop('disabled', false);
    } else {
        $('#btn_agregar_proyecto').prop('disabled', true);
    }
});

function getProyectosSeguridad() {
    "use strict";
    let html = '';
    $('#tbl_proyectos_seguridad').find('tbody').empty();
    $.ajax({
        url: `${BASE_URL}/rest/proyectos/`,
        type: 'GET',
        success: response => {
            proyectos_seguridad = response;
            $.each(proyectos_seguridad, (key, val)=> {
                html += `<tr>
                            <td>${val.sigla}</td>
                            <td>${val.anio}</td>
                            <td>${val.descripcion == null ? '' : val.descripcion}</td>
                            <td>${val.cod_meta}</td>
                            <td>${val.estado == 1 ? '<span class="label label-success">Activo</span>' : '<span class="label label-danger">Inactivo</span>'}</td>
                            <td>
                               <ul class="icons-list">
                                    <li><a data-popup="tooltip" onclick="modal_editarProyecto(${val['id']})" title="" data-original-title="Editar Proyecto"><i class="icon-pencil7"></i></a></li>
                                    <li><a data-popup="tooltip" onclick="modal_asignarSistemas(${val['id']})" title="" data-original-title="Asignar Sistemas"><i class="icon-cog7"></i></a></li>
						        </ul>
						     </td>`;
                html += `</tr>`
            });
            $('#tbl_proyectos_seguridad').find('tbody').html(html);
        }
    })
}


function modal_editarProyecto(id) {
    "use strict";
    $('#modal_editar_proyecto').modal('show');
    proyectos_seguridad_selected = findInObject(proyectos_seguridad, 'id', id);
    for (let i in proyectos_seguridad_selected[0]) {
        if (i == 'estado') {
            if (proyectos_seguridad_selected[0][i] == 1) {
                $(`input[name=${i}]`).prop('checked', true);
            } else {
                $(`input[name=${i}]`).prop('checked', false);
            }
        }
        $(`input[name=${i}]`).val(proyectos_seguridad_selected[0][i])
    }
}

function modal_asignarSistemas(id) {
    "use strict";
    proyectos_seguridad_selected = findInObject(proyectos_seguridad, 'id', id);

}

function addProyecto() {
    "use strict";
    let url = `${BASEURL}/rest/proyectos/`;
    let data = {
        id_siga: proyectos_siga_selected[0].id,
        nombre: proyectos_siga_selected[0].desc_proyecto,
        sigla: proyectos_siga_selected[0].sigla,
        anio: proyectos_siga_selected[0].annio_meta,
        cod_meta: proyectos_siga_selected[0].codi_meta,
        estado: 1
    };
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        success: response => {
            getProyectosSiga();
            getProyectosSeguridad();
        }
    })
}

function saveProyecto() {
    "use strict";
    let data = proyectos_seguridad_selected[0];
    let url = `${BASEURL}/rest/proyectos/`;
    $.ajax({
        url: url,
        type: 'PUT',
        data: data,
        success: response => {
            getProyectosSiga();
            getProyectosSeguridad();
        }
    })
}

$('#btn_agregar_proyecto').on('click', event => {
    "use strict";
    alert_confirm(addProyecto);

});