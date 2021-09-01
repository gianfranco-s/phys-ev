

var sitio = window.location.origin
    sitio += '/ejercicios/mostrarListado'
    
const app = Vue.createApp({
    el: '#abm',
    delimiters: ['[[', ']]'],

    data() {
        return{
            accion: 'Elija una acción',
            mostrar_get : false,
            mostrar_pst : false,
            mostrar_put : false,
            mostrar_dlt : false,

            respuesta : '',
            id:'',
            titulo:'',
            tema:'',
            enunciado:'',
            algoritmo:''
            
        }
    },

    methods:{
        m_get(){
            this.accion = 'Datos obtenidos',
            this.mostrar_get = true,
            this.mostrar_pst = false,
            this.mostrar_put = false,
            this.mostrar_dlt = false
            
            axios.get(sitio,{headers: {"X-CSRFToken": csrfToken}})
                .then(res => showOutput(res))
                .catch(err => console.error(err))
        
            },

        m_pst(){
            this.accion = 'Ingrese nuevo ejercicio',
            this.mostrar_get = false,
            this.mostrar_pst = true,
            this.mostrar_put = false,
            this.mostrar_dlt = false

        },
        m_put(){
            this.accion = 'Modificar ejercicio',
            this.mostrar_get = false,
            this.mostrar_pst = false,
            this.mostrar_put = true,
            this.mostrar_dlt = false
        },
        m_dlt(){
            this.accion = '¿Qué número de ejercicio desea borrar?',
            this.mostrar_get = false,
            this.mostrar_pst = false,
            this.mostrar_put = false,
            this.mostrar_dlt = true
        },

        send_pst(){
            let data = new FormData()
            data.append('titulo',this.titulo)
            data.append('tema',this.tema)
            data.append('enunciado',this.enunciado)
            data.append('algoritmo',this.algoritmo)
                        
            axios.post(sitio,data,{headers: {"X-CSRFToken": csrfToken}})
                .then(res => showOutput(res))
                .catch(error => {console.log(error.response)})
        },

        send_put(){
            let data = new FormData()
            data.append('id',this.id)
            data.append('titulo',this.titulo)
            data.append('tema',this.tema)
            data.append('enunciado',this.enunciado)
            data.append('algoritmo',this.algoritmo)

            let dire = sitio+'/'+this.id;
            axios.put(dire,data,{headers: {"X-CSRFToken": csrfToken},})
                .then(res => showOutput(res))
                .catch(error => {console.log(error.response)}) 
        },

        send_dlt(){
            let dire = sitio+'/'+this.id;
            console.log(dire)
            axios.delete(dire,{headers: {"X-CSRFToken": csrfToken}})
                .then(res => showOutput(res))
                .catch(error => console.error(error))
        },        
    },
    
})

app.mount('#abm')

function showOutput(res) {
    document.getElementById('respuesta').innerHTML = `
    <pre>${JSON.stringify(res.data, null, 2)}</pre>
    `;
}

