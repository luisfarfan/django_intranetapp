/**
 * Created by LFarfan on 19/12/2016.
 */

var pathArray = location.href.split('/');
var protocol = pathArray[0];
var host = pathArray[2];
BASEURL = protocol + '//' + host;


$('#iniciar_sesion').on('click', event => {
    "use strict";
    let url = `${BASEURL}/usuario/authentication/`;
    let data = {usuario: $('#usuario').val(), clave: $('#clave').val()};
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        success: response => {
            console.log(response);
        }
    });
});

