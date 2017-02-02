/**
 * Created by lfarfan on 29/01/2017.
 */

export class ObjectHelper {
    isEmpty(obj) {
        return Object.keys(obj).length === 0;
    }

    findInArrayObject(obj, value_search, key) {
        let res = false;
        if (!this.isEmpty(obj)) {
            obj.map((value, key)=> {
                if (key in value) {
                    if (value[key] == value_search) {
                        res = value;
                    }
                }
            })
        }
        return res;
    }
}

export class MenuHelper {

    drawSidebar(menu) {
        let html = '';
        html += `<li class="navigation-header"><span>Censo de Poblacion y Vivienda VIII</span> <i class="icon-menu" title="Main pages"></i></li>`;
        html += this.recursiveHTMLSideBar(menu);
        return html;
    }

    recursiveHTMLSideBar(array) {
        let html = '';
        array.map((value, key)=> {
            if (value.modulos_hijos.length) {
                html += `<li><a href="#"><i class="icon-tree5"></i> <span>${value.descripcion}</span></a><ul>`;
                value.modulos_hijos.map((child1, k)=> {
                    html += `<li><a href="${child1.slug}"><i class="icon-IE"></i>${child1.descripcion}</a></li>`;
                })
                html += this.recursiveHTMLSideBar(value.modulos_hijos);
                html += `</ul>`;
            } else {
                html += `<li><a href="${BASEURL}/${value.slug}"><i class="icon-home4"></i> <span>${value.descripcion}</span></a></li>`;
            }
        });
        return html;
    }
}
export class SessionHelper {
    setSession(key, object) {
        localStorage.setItem(key, JSON.stringify(object))
        return this.getSession();
    }

    getSession(key = 'usuario') {
        return JSON.parse(localStorage.getItem(key));
    }
}