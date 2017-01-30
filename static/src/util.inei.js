/**
 * Created by lfarfan on 29/01/2017.
 */

export function showDivAlert(message, type) {
    return `<div class="alert bg-${type} alert-styled-left">
                <button type="button" class="close" data-dismiss="alert"><span>×</span><span class="sr-only">Close</span></button>
                <span class="text-semibold">${message}</span>
            </div>`;
}

export function showSwalAlert(message, type) {
    new PNotify({
        title: 'Primary notice',
        text: 'Check me out! I\'m a notice.',
        icon: 'icon-menu6'
    });
}

