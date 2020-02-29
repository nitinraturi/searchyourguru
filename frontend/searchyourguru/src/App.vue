<template>
  <div id="app">
    <Navbar />
    <!-- <Loader /> -->
    <router-view />
  </div>
</template>

<script>
import Navbar from '@/components/snippets/Navbar.vue'
// import Loader from '@/components/snippets/Loader.vue'

export default {
  name: 'App',
  components: {
    Navbar
    // Loader
  }
}
</script>

<style>
body {
  background: #f5f4f3 !important;
  font-size: 0.95em !important;
}

.box {
  background: #fff;
  border-radius: 2px;
}
.box {
  /* box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24); */
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22) !important;
  /* transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); */
}
/* .box:hover {
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
} */
</style>
