/**
 * Created by LFarfan on 19/12/2016.
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function setSelect_v2(id, json, keys = []) {
    $('#' + id).find('option').remove();

    let html = '<option value="-1">Seleccione</option>';

    $.each(json, function (key, val) {
        if (typeof val == 'string') {
            html += `<option value="${val}">${val}</option>`
        } else {
            html += `<option value="${val[keys[0]]}">${val[keys[1]]}</option>`
        }
    });
    $('#' + id).html(html);
}

function findInObject(obj, key, value) {
    "use strict";
    let res = [];
    if (value != '-1') {
        if (obj.length > 0) {
            $.each(obj, (k, v)=> {
                if (v[key] == value) {
                    res.push(v);
                }
            });
        }
    }
    return res;
}

function setTable(id, json, params, datatable = false, datatable_params = {}) {
    let html = '';
    if (json.length > 0) {
        $.each(json, (key, val)=> {
            html += '<tr>';
            for (let i in params) {
                html += `<td>${val[params[i]] == null ? 0 : val[params[i]]}</td>`;
            }
            html += '</tr>';
        });
    }
    $('#' + id).find('tbody').empty();
    if (datatable) {
        ('#' + id).DataTable({datatable_params})
        ('#' + id).dataTable().fnDestroy();
    }
    $('#' + id).find('tbody').html(html);

    if (datatable) {
        ('#' + id).DataTable({datatable_params})
    }

}

function setTablev2(arguments, callback, datatable = false, datatable_params = {}) {
    let html = '';
    $('#' + id).find('tbody').empty();
    if (datatable) {
        ('#' + id).DataTable({datatable_params})
        ('#' + id).dataTable().fnDestroy();
    }
    $.each(arguments.json, (key, val)=> {
        html += '<tr>';
        for (let i in arguments.params) {
            html += `<td>${val[arguments.params[i]] == null ? 0 : val[arguments.params[i]]}</td>`;
        }
        if (arguments.params.pk) {
            html += `<td>${val[arguments.params.pk]}</td>`;
        }
        html += '</tr>';
    });
    $('#' + id).find('tbody').html(html);

    if (datatable) {
        ('#' + arguments.id).DataTable({datatable_params})
    }
}

function alert_confirm(callback) {
    "use strict";
    swal({
        title: 'Esta seguro de Guardar?',
        text: '',
        type: 'success',
        showCancelButton: true,
        confirmButtonColor: "#EF5350",
        confirmButtonText: "Si!",
        cancelButtonText: "No!",
        closeOnConfirm: true,
        closeOnCancel: true,
        showLoaderOnConfirm: true
    }, confirm => {
        if (confirm) {
            callback()
        }
    });
}