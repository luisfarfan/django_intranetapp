define(['./helper.inei.js', './util.inei.js'], function (_helperInei, _utilInei) {
    'use strict';

    /**
     * Created by LFarfan on 19/12/2016.
     */
    var sessionHelper = new _helperInei.SessionHelper();
    var objectHelper = new _helperInei.ObjectHelper();
    $('#iniciar_sesion').on('click', event => {
        "use strict";

        let url = `${BASEURL}/usuario/authentication/`;
        let data = { usuario: $('#usuario').val(), clave: $('#clave').val() };
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            success: response => {
                if (objectHelper.isEmpty(response)) {
                    //mostrar div error
                    $('#div_error_message').html((0, _utilInei.showDivAlert)('Usuario o contraseña no validos', 'danger'));
                } else {
                    $('#div_error_message').html((0, _utilInei.showDivAlert)('Bienvenido!', 'success'));
                    $('#iniciar_sesion').addClass('disabled');
                    setTimeout(() => {
                        sessionHelper.setSession('usuario', response);
                        let session = sessionHelper.getSession();
                        console.log(response);
                        window.location.href = `${BASEURL}/${session.routes[2].slug}`;
                    }, 1000);
                }
            }
        });
    });
});