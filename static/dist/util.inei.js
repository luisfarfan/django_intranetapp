define(['exports', '../assets/js/plugins/notifications/pnotify.custom.min.js'], function (exports) {
    'use strict';

    Object.defineProperty(exports, "__esModule", {
        value: true
    });
    exports.showDivAlert = showDivAlert;
    exports.showSwalAlert = showSwalAlert;
    exports.jsonFormatFancyTree = jsonFormatFancyTree;
    function showDivAlert(message, type) {
        return `<div class="alert bg-${type} alert-styled-left">
                <button type="button" class="close" data-dismiss="alert"><span>×</span><span class="sr-only">Close</span></button>
                <span class="text-semibold">${message}</span>
            </div>`;
    } /**
       * Created by lfarfan on 29/01/2017.
       */
    function showSwalAlert(message, type) {
        new PNotify({
            title: 'Primary notice',
            text: 'Check me out! I\'m a notice.',
            icon: 'icon-menu6'
        });
    }

    function jsonFormatFancyTree(menu_json, rol_id_array = []) {
        /**
         * sample structure
         * [
         *  {title: "node1"},{title: "node2"},{title:"node3", folder:true,key:"__node3"},
         *      children: [
         *          {title: "sub_node1",
         *              children: [
         *                  {title: "sub_node2"},{title: "sub_node3"},{title: "sub_node4"}]}]]
         *
         *
         * **/
        let treejson = [];
        let interface_node = {};
        menu_json.map((value, key) => {
            interface_node = {};
            interface_node['title'] = value.descripcion;
            interface_node['key'] = value.id;
            if (value.modulos_hijos.length) {
                interface_node['folder'] = true;
                interface_node['children'] = [];
                let children = [];
                value.modulos_hijos.map((node_value, node_order) => {
                    children.push({
                        'title': node_value.descripcion,
                        'key': node_value.id,
                        'folder': node_value.modulos_hijos.length == 0 ? false : true,
                        'children': node_value.modulos_hijos.length == 0 ? [] : jsonFormatFancyTree(node_value.modulos_hijos),
                        'selected': rol_id_array.indexOf(node_value.id) != -1 ? true : false,
                        'preselected': rol_id_array.indexOf(node_value.id) != -1 ? true : false
                    });
                });
                interface_node['children'] = children;
                treejson.push(interface_node);
            } else {
                interface_node['folder'] = false;
                treejson.push(interface_node);
            }
        });
        return treejson;
    }
});