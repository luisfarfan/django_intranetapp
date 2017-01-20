/// <reference path="./../../typings/index.d.ts" />

import ProyectosService from './proyectos.service';
import * as $ from 'jquery';
class Proyectos {
    dataservice:Object;
    proyectosservice = new ProyectosService();

    getData(){
        this.dataservice = this.proyectosservice.getProyectos();
        return this.dataservice;
    }
    

}

var proyectos = new Proyectos();
console.log(proyectos.getData());