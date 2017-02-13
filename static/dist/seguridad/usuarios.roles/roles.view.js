define(['exports', './roles.model.js', '../../helper.inei.js', '../../util.inei.js'], function (exports, _rolesModel, _helperInei, _utilInei) {
    'use strict';

    Object.defineProperty(exports, "__esModule", {
        value: true
    });
    exports.getRolSelected = getRolSelected;

    var _rolesModel2 = _interopRequireDefault(_rolesModel);

    var util = _interopRequireWildcard(_utilInei);

    function _interopRequireWildcard(obj) {
        if (obj && obj.__esModule) {
            return obj;
        } else {
            var newObj = {};

            if (obj != null) {
                for (var key in obj) {
                    if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key];
                }
            }

            newObj.default = obj;
            return newObj;
        }
    }

    function _interopRequireDefault(obj) {
        return obj && obj.__esModule ? obj : {
            default: obj
        };
    }

    var objectHelper = new _helperInei.ObjectHelper();
    var sessionHelper = new _helperInei.SessionHelper();
    var rolesModel = new _rolesModel2.default();
    var roles = [];
    var rol_selected = [];
    var session = sessionHelper.getSession();
    var tree_menu_format = [];
    var rol_id_array = [];
    var node_keys_selected = [];

    function getAllRoles() {
        rolesModel.get().done(response => {
            roles = response;
            drawRoles();
        });
    }

    function getRolSelected(id) {
        rol_selected = objectHelper.findInArrayObject(roles, id, 'id');
        rol_id_array = [];
        if (rol_selected.modulo_rol.length) {
            rol_selected.modulo_rol.map((value, key) => {
                rol_id_array.push(value.id);
            });
            tree_menu_format = util.jsonFormatFancyTree(session.menu, rol_id_array);
        } else {
            tree_menu_format = util.jsonFormatFancyTree(session.menu);
        }
        let options_tree = {
            checkbox: true,
            selectMode: 3,
            source: tree_menu_format,
            init: function (event, data) {
                data.tree.getRootNode().visit(function (node) {
                    if (node.data.preselected) node.setSelected(true);
                });
            },
            loadChildren: function (event, ctx) {
                ctx.node.fixSelection3AfterClick();
            },
            select: function (event, data) {
                // Get a list of all selected nodes, and convert to a key array:
                let selKeys = $.map(data.tree.getSelectedNodes(), function (node) {
                    return node.key;
                });
                // Get a list of all selected TOP nodes
                let selRootNodes = data.tree.getSelectedNodes(true);
                // ... and convert to a key array:
                let selRootKeys = $.map(selRootNodes, function (node) {
                    return node.key;
                });
                node_keys_selected = selKeys;
                console.log(node_keys_selected);
            },
            dblclick: function (event, data) {
                data.node.toggleSelected();
            },
            keydown: function (event, data) {
                if (event.which === 32) {
                    data.node.toggleSelected();
                    return false;
                }
            },
            // The following options are only required, if we have more than one tree on one page:
            //				initId: "SOURCE",
            cookieId: "fancytree-Cb3",
            idPrefix: "fancytree-Cb3-"
        };
        $('#tree_menu_rol').fancytree(options_tree);
        $('#tree_menu_rol').fancytree("destroy");
        $('#tree_menu_rol').fancytree(options_tree);
    }

    function drawRoles() {
        let html = '';
        roles.map((value, key) => {
            html += `<tr>
                    <td>${parseInt(key) + 1}</td>
                    <td>${value.nombre}</td>
                    <td><ul class="icons-list">
                            <li name="li_rol" data-value = "${value.id}" class="text-primary-600"><a href="#"><i class="icon-pencil7"></i></a></li>
                            <li class="text-danger-600"><a href="#"><i class="icon-trash"></i></a></li>
						</ul></td>
                </tr>`;
        });
        $('#table_roles').find('tbody').html(html);
        $('li[name="li_rol"]').on('click', event => {
            getRolSelected($(event.currentTarget).data('value'));
        });
    }

    var RolesCrud = {
        add: () => {
            if (form_rol_validate.valid()) {
                let valid_form = objectHelper.formToObject(util.serializeForm('form_rol'));
                rolesModel.add(valid_form).done(response => {
                    util.showSwalAlert('Se ha agregado el Rol correctamente', 'Exito!', 'success');
                    getAllRoles();
                    $('#modal_rol').modal('hide');
                    form_rol_validate.resetForm();
                }).error(error => {
                    util.showSwalAlert('Ha ocurrido un error, por favor intente nuevamente', 'Error!', 'error');
                });
            }
        }
    };

    var RolJsonRules = {
        form_rol: {
            nombre: {
                maxlength: 10
            },
            descripcion: {
                maxlength: 10
            }
        }
    };

    var form_rol_validate = $('#form_rol').validate(util.validateForm(RolJsonRules.form_rol));

    var Roles = {
        initRoles: () => {
            getAllRoles();
        }
    };

    Roles.initRoles();

    $('#btn_submit_form').on('click', event => {
        RolesCrud.add();
    });
});