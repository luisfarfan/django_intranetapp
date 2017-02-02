define(['exports'], function (exports) {
    'use strict';

    Object.defineProperty(exports, "__esModule", {
        value: true
    });
    /**
     * Created by lfarfan on 29/01/2017.
     */

    class ObjectHelper {
        isEmpty(obj) {
            return Object.keys(obj).length === 0;
        }

        findInArrayObject(obj, value_search, _key) {
            let res = false;
            if (!this.isEmpty(obj)) {
                obj.map((value, key) => {
                    if (_key in value) {
                        if (value[_key] == value_search) {
                            res = value;
                        }
                    }
                });
            }
            return res;
        }

        findInArrayObjectRecursive(obj, value_search, key, key_array) {
            let res = false;
            if (!this.isEmpty(obj)) {
                obj.map((value, key) => {
                    if (_key in value) {
                        if (value[_key] == value_search) {
                            res = value;
                        } else {
                            if (value[key_array].length) {
                                this.findInArrayObject(value[key_array], value_search, key, key_array)
                            }
                        }
                    }
                });
            }
            return res;
        }
    }

    exports.ObjectHelper = ObjectHelper;

    class SessionHelper {
        setSession(key, object) {
            localStorage.setItem(key, JSON.stringify(object));
            return this.getSession();
        }

        getSession(key = 'usuario') {
            return JSON.parse(localStorage.getItem(key));
        }
    }
    exports.SessionHelper = SessionHelper;

    class MenuHelper {
        drawSidebar(menu) {
            let html = '';
            html += `<li class="navigation-header"><span>Censo de Poblacion y Vivienda VIII</span> <i class="icon-menu" title="Main pages"></i></li>`;
            html += this.recursiveHTMLSideBar(menu);
            return html;
        }

        recursiveHTMLSideBar(array) {
            let html = '';
            array.map((value, key) => {
                if (value.modulos_hijos.length) {
                    html += `<li ${value.id == MODULO_ID ? 'class="active"' : ''}><a href="#"><i class="icon-tree5"></i> <span>${value.descripcion}</span></a><ul>`;
                    value.modulos_hijos.map((child1, k) => {
                        html += `<li ${value.id == MODULO_ID ? 'class="active"' : ''}><a href="${child1.slug}/"><i class="icon-IE"></i>${child1.descripcion}</a></li>`;
                    });
                    html += this.recursiveHTMLSideBar(value.modulos_hijos);
                    html += `</ul>`;
                } else {
                    html += `<li ${value.id == MODULO_ID ? 'class="active"' : ''}><a href="${BASEURL}/${value.slug}/"><i class="icon-home4"></i> <span>${value.descripcion}</span></a></li>`;
                }
            });
            return html;
        }

        setPageHeader() {
            let sessionHelper = new SessionHelper();
            let session = sessionHelper.getSession();

        }

        findRecursiveInMenu() {
            let sessionHelper = new SessionHelper();
            let menu = sessionHelper.getSession();


        }
    }
    exports.MenuHelper = MenuHelper;
});