<template>
  <div id="app">
    <div id="nav">
      <nav
        class="navbar is-fixed-top is-bold"
        role="navigation"
        aria-label="main navigation"
        id="nav_app"
      >
        <div class="container">
          <div class="navbar-brand">
            <a class="navbar-item" href="/">
              <span class="has-text-weight-bold is-family-monospace has-text-info">SearchYourGuru</span>
            </a>
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
              <a class="navbar-item" href>Blog</a>
            </div>
            <div class="navbar-end">
              <a class="navbar-item" href="/">Login</a>
              <a class="navbar-item" href="/">Register</a>
            </div>
          </div>
        </div>
      </nav>
      <!-- <router-link to="/">Home</router-link>|
      <router-link to="/about">About</router-link>-->
    </div>
    <!-- <router-view /> -->
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
