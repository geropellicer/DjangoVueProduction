<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link 
        :to="{ name: 'home' }" 
        class="navbar-brand"
        >Canchitas Cancheras :)
      </router-link>

      <router-link 
        :to="{ name: 'logout' }" 
        class="desloguearse"
        >Log Out
      </router-link>

    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent"
};
</script>

<style>
.my-navbar {
  border-bottom: 1px solid #ddd;
}

.navbar-brand {
  font-weight: bold;
  font-size: 130%;
}

.navbar-brand:hover {
  color: #dc3545 !important;
}
</style>