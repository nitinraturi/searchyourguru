<template>
  <div id="navbar">
    <nav
      class="navbar is-fixed-top"
      role="navigation"
      aria-label="main navigation"
    >
      <div class="container">
        <div class="navbar-brand">
          <router-link class="navbar-item" to="/">
            <span class="has-text-weight-bold is-family-monospace has-text-info"
              >SearchYourGuru</span
            >
          </router-link>
          <a
            role="button"
            class="navbar-burger burger"
            aria-label="menu"
            aria-expanded="false"
            data-target="navbarBasicExample"
          >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div id="navbarBasicExample" class="navbar-menu">
          <div class="navbar-start">
            <router-link class="navbar-item" to="/">Blog</router-link>
          </div>
          <div class="navbar-end">
            <router-link
              class="navbar-item"
              to="/login/"
              v-if="isAuthenticated == false"
              >Login</router-link
            >
            <router-link
              class="navbar-item"
              to="/signup/"
              v-if="isAuthenticated == false"
              >Register</router-link
            >
            <router-link
              class="navbar-item"
              to="/dashboard/"
              v-if="isAuthenticated == true"
              >Dashboard</router-link
            >
            <a
              class="navbar-item"
              v-on:click.prevent="logout"
              v-if="isAuthenticated == true"
              >Logout</a
            >
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import axios from 'axios'
import ValidatorsMixin from '@/components/mixins/ValidatorsMixin.vue'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'

document.addEventListener('DOMContentLoaded', () => {
  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(
    document.querySelectorAll('.navbar-burger'),
    0
  )

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {
    // Add a click event on each of them
    $navbarBurgers.forEach(el => {
      el.addEventListener('click', () => {
        // Get the target from the "data-target" attribute
        const target = el.dataset.target
        const $target = document.getElementById(target)

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active')
        $target.classList.toggle('is-active')
      })
    })
  }
})

export default {
  name: 'Navbar',
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated
    }
  },
  methods: {
    logout: function() {
      axios
        .post(this.get_endpoint(this.endpoints.logout), {}, this.get_headers())
        .then(
          () => {
            localStorage.removeItem('guru-user-token')
            localStorage.removeItem('guru-user-token-refresh')
            this.$store.state.isAuthenticated = false
            this.$router.push('/')
          },
          () => {}
        )
    }
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>

<style scoped></style>
