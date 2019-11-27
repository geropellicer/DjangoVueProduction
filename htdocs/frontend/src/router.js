import Vue from "vue";
import Router from "vue-router";
import CanchaDetalle from "./views/CanchaDetalle.vue";
import Home from "./views/Home.vue";
import NotFound from "./views/NotFound.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/logout/",
      name: "logout",
    },
    {
      path: "/cancha/:id",
      name: "cancha",
      component: CanchaDetalle,
      props: true
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound
    }
  ]
});
