<template>
  <div id="home_view" class="has-background-white">
    <section class="hero is-link is-bold is-fullheight-with-navbar">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-6">
              <p class="title">
                SearchYourGuru
              </p>
              <div class="box">
                <FilterForm />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section" v-if="isAuthenticated == false">
      <div class="container">
        <center>
          <router-link to="/signup/" class="button is-success">
            Register & Get your 1st connection for free
          </router-link>
        </center>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h1 class="title has-text-centered">Learn & Earn - 3 Step Process</h1>
        <hr />
        <div class="columns is-centered">
          <div class="column is-9">
            <div class="columns">
              <div class="column is-full">
                <figure class="image">
                  <img src="@/assets/student-h1.jpg" alt="" />
                </figure>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section" v-if="isAuthenticated == false">
      <div class="container">
        <center>
          <router-link to="/signup/" class="button is-success">
            Register For a Free Account Today
          </router-link>
        </center>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h1 class="title has-text-centered">Why US</h1>
        <hr />
        <div class="columns is-centered">
          <div class="column is-9">
            <div class="columns">
              <div class="column is-full">
                <figure class="image">
                  <img src="@/assets/banner1.jpg" alt="" />
                </figure>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import FilterForm from '@/components/forms/FilterForm.vue'
export default {
  name: 'home',
  components: {
    FilterForm
  },
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated
    }
  }
}
</script>
