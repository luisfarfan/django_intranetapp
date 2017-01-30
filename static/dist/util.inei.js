define(['exports'], function (exports) {
    'use strict';

    Object.defineProperty(exports, "__esModule", {
        value: true
    });
    exports.showDivAlert = showDivAlert;
    exports.showSwalAlert = showSwalAlert;
    /**
     * Created by lfarfan on 29/01/2017.
     */

    function showDivAlert(message, type) {
        return `<div class="alert bg-${type} alert-styled-left">
                <button type="button" class="close" data-dismiss="alert"><span>×</span><span class="sr-only">Close</span></button>
                <span class="text-semibold">${message}</span>
            </div>`;
    }

    function showSwalAlert(message, type) {
        new PNotify({
            title: 'Primary notice',
            text: 'Check me out! I\'m a notice.',
            icon: 'icon-menu6'
        });
    }
});