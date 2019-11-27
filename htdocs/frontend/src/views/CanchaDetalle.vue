<template>
  <div class="home">
    <div class="container mt-2">
      <div :key="cancha.id">

            <div class="card w-100">
              <div class="card-body">
                <h5 class="card-title">{{ this.cancha.nombre }}</h5>
                <h6>{{ this.cancha.tipo }}</h6>
                <span>Cod. Interno: {{ this.cancha.codigo }}</span>
                <p class="card-text mt-3">{{ cancha.descripcion}}</p>
                
                <div class="form-check">
                    <input readonly="true" disabled  class="form-check-input" type="checkbox" :checked="cancha.tiene_vestuario" id="defaultCheck1">
                    <label class="form-check-label" for="defaultCheck1">
                        Vestuarios
                    </label>
                </div>

                <div class="form-check">
                    <input readonly="true" disabled class="form-check-input" type="checkbox" :checked="cancha.tiene_iluminacion" id="defaultCheck2">
                    <label class="form-check-label" for="defaultCheck2">
                        Iluminacion
                    </label>
                </div>

                <div class="form-check">
                    <input readonly="true" disabled class="form-check-input" type="checkbox" :checked="cancha.tiene_cesped_sintetico" id="defaultCheck3">
                    <label class="form-check-label" for="defaultCheck3">
                        Cesped sintetico
                    </label>
                </div>
                
                <!-- <div v-for="alquiler in this.alquileres" :key="alquiler.cancha">


                </div> -->
                <!-- <div v-for="alquiler in this.cancha.alquileres" :key="alquiler.cancha">
                <router-link
                :to="{ name: 'alquiler', params: { int: cancha.alquiler.cancha } }"
                class="question-link"
                >
                <a href="#" class="card-link">Card link</a>
                </router-link> -->

                    <ul class="list-group list-group-flush">
                        <hr class="mt-4">
                        <h3>Hay {{ this.alquileres.length }} Reservas en esta cancha </h3>
                        <li v-for="alquiler in this.alquileres" :key="alquiler.id" :id="alquiler.id" class="list-group-item">
                            <h5> Reserva {{ alquiler.id }}</h5>
                            <ul>
                                <li>Cliente: {{ alquiler.cliente }}</li>
                                <li>Empleado: {{ alquiler.empleado }}</li>
                                <li>Fecha de la reserva desde: {{ alquiler.turno_desde       }}</li>
                                <li>Turno hasta: {{ alquiler.turno_hasta }}</li>
                                <button @click.prevent="eliminarAlquiler(alquiler.id, alquiler)" type="button" class="my-3 btn btn-danger">Eliminar reserva</button>
                            </ul>
                        </li>
                    </ul>


                </div>

              </div>


            </div>
            <button @click.prevent="alquilar(cancha.id)" class="btn btn-primary mt-4 w-100 py-4 mb-5" type="submit">Alquilar</button>

      
      </div>

        <div v-show="this.alquilando" class="border border-primary w-75 mx-auto px-4 py-4 mb-5" style="border-radius: 10px">
            <form @submit.prevent="onSubmit(cancha.id)">
                <h3>Reservar cancha {{ cancha.nombre }}</h3>

        <div class="form-group">
            <label for="cliente">Cliente:</label>
            <input v-model="clienteSend" type="text" class="form-control" id="cliente" aria-describedby="emailHelp" placeholder="Nombre dle cliente">
             <label for="empleado">Empleado:</label>
            <input v-model="empleadoSend" type="text" class="form-control" id="empleado" aria-describedby="emailHelp" placeholder="Nombre del empleado">
        </div>

        <div class="form-group">
            <h4> Fecha del turno: </h4>
            <input v-model="fechaTurno" type="date">
        
        </div>

        <div class="form-group">
            <h4> Horario: </h4>
            <input v-model="horarioTurno" type="time">

        </div>

        <button @click.prevent="cerrarFormulario" type="button" class="my-3 btn btn-danger">Cancelar</button>
        <button class="ml-2 btn btn-primary">Submit</button>
        </form>
        </div>

      <div class="my-4">
        <p v-show="loadingQuestions">...loading...</p>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "canchadetalle",
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      cancha: {},
      alquileres: [],
      next: null,
      loadingQuestions: false,
      alquilando: false,
      alquilandoNum: 0,
      fechaTurno: null,
      horarioTurno: null,
      canchaAlquilandoSend: '',
      clienteSend: '',
      empleadoSend: '',
      fechahorarioTurno: '',
    }
  },
  methods: {
      onSubmit: function(id){
      // Mandamos a la base
            if (this.fechaTurno && this.horarioTurno) {
            let endpoint = `/apic/alquileres/`;
            let datetime = this.fechaTurno + 'T' + this.horarioTurno;
            this.fechahorarioTurno = datetime;
            apiService(endpoint, "POST", { turno_desde: datetime,
                                            turno_hasta: datetime,
                                            cancha: this.cancha.id,
                                            cliente: this.clienteSend,
                                            empleado: this.empleadoSend,})
                .then(data => {
                this.alquileres.unshift(data)
                })
            if (this.error) {
                this.error = null;
            }
            } else {
                this.error = "You can't send an empty answer!";
            }

                this.fechaTurno = '';
                this.horarioTurno = '';
                this.canchaAlquilandoSend = '';
                this.clienteSend = '';
                this.empleadoSend = '';
                this.fechahorarioTurno = '';
                this.alquilando = false;

      },
        cerrarFormulario: function(){
        this.alquilando = false;
        this.alquilandoNum = 0;
        },

    getCanchaDetalles() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/apic/canchas/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.cancha = data;
            console.log(data);
            this.alquileres = data.alquileres
            this.setPageTitle(data.nombre)
          } else {
            this.question = null;
            this.setPageTitle("404 - Page Not Found")
          }

        })
    },
    setPageTitle(title) {
      // set a given title string as the webpage title
      document.title = title;
    },
    setRequestUser() {
      // the username has been set to localStorage by the App.vue component
      this.requestUser = window.localStorage.getItem("username");
    },
    /*getCanchaDetalles() {
      // make a GET Request to the questions list endpoint and populate the questions array
      let endpoint = `/apic/canchas/${this.pk}`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      apiService(endpoint)
        .then(data => {
          this.canchas.push(...data.results)
          this.loadingQuestions = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        })
    },*/
    async eliminarAlquiler(id, alquiler) {
      // delete a given answer from the answers array and make a delete request to the REST API
      let endpoint = `/apic/alquileres/${id}/`;
      try {
        await apiService(endpoint, "DELETE");
        let conseguidor = id;
        var index = this.alquileres.indexOf(alquiler);
        if (index !== -1) this.alquileres.splice(index, 1);
      }
      catch (err) {
        console.log(err)
      }
    },
    alquilar(id){
        this.alquilando = true;
        this.alquilandoNum = id;
    }
  },
  created() {
    this.getCanchaDetalles()
    document.title = "Proyecto Final";
  }, 
};
</script>

<style scoped>
.question-author {
  font-weight: bold;
  color: #DC3545;
}

.question-link {
  font-weight: bold;
  color: black;
}

.question-link:hover {
  color: #343A40;
  text-decoration: none;
}
</style>
