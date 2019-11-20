<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <span v-if="!isLoggedIn">
        <router-link to="/login">Login</router-link>
      </span>
      <span v-else>
        <a @click.prevent="logout" href="">Logout</a>
      </span>
    </div>
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'App',
  methods: {
    ...mapGetters(['isLoggedIn']),
    ...mapActions(['logout']),
  }
}

</script>

<style>

</style>
