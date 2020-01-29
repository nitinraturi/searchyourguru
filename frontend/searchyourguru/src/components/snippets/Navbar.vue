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
            <router-link class="navbar-item" to="/login/">Login</router-link>
            <router-link class="navbar-item" to="/signup/"
              >Register</router-link
            >
          </div>
        </div>
      </div>
    </nav>
    <!-- <router-link to="/">Home</router-link>|
      <router-link to="/about">About</router-link>-->
  </div>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped></style>
