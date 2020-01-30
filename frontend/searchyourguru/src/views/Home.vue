<template>
  <div id="home_view">
    <section class="hero is-info is-bold is-medium">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-8">
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

    <section class="section">
      <div class="container">
        <center>
          <a href="#" class="button is-success">
            Register & Get your 1st connection for free
          </a>
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
                  <img src="../../public/img/student-h1.jpg" alt="" />
                </figure>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <center>
          <a href="#" class="button is-success">
            Register For a Free Account Today
          </a>
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
                  <img src="../../public/img/banner1.jpg" alt="" />
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
  }
}
</script>
