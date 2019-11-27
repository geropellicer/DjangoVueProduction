<template>
  <div class="home">
    <div class="container mt-2">
      <div v-for="cancha in canchas"
           :key="cancha.pk">

            <div class="card w-100">
              <div class="card-body">
                <h5 class="card-title">{{ cancha.nombre }}</h5>
                <h6 v-if=" cancha.tipo == '7ABIERTA'" class="card-subtitle mb-2 text-muted">Cancha de 7 Abierta</h6>
                <h6 v-if=" cancha.tipo == '5ABIERTA'" class="card-subtitle mb-2 text-muted">Cancha de 5 Abierta</h6>
                <h6 v-if=" cancha.tipo == '7CERRADA'" class="card-subtitle mb-2 text-muted">Cancha de 7 Cerrada</h6>
                <h6 v-if=" cancha.tipo == '5CERRADA'" class="card-subtitle mb-2 text-muted">Cancha de 5 Cerrada</h6>
                <h6 v-if=" cancha.tipo == '11'" class="card-subtitle mb-2 text-muted">Cancha de fútbol 11</h6>
                <p class="card-text">{{ cancha.descripcion}}</p>
                
                <div v-if="cancha">
                    <router-link :to="{ name: 'cancha', params: { id: cancha.id }}">Ver detalles</router-link>
                </div>
                
              </div>
            </div>

        <h2>
          
        </h2>
      </div>
      <div class="my-4">
        <p v-show="loadingQuestions">...loading...</p>
        <button
          v-show="next"
          @click="getCanchas"
          class="btn btn-sm btn-outline-success"
          >Load More
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "home",
  data() {
    return {
      canchas: [],
      next: null,
      loadingQuestions: false
    }
  },
  methods: {
    getCanchas() {
      // make a GET Request to the questions list endpoint and populate the questions array
      let endpoint = "/apic/canchas/";
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
    }
  },
  created() {
    this.getCanchas()
    document.title = "Canchas Cancheras";
  }
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
