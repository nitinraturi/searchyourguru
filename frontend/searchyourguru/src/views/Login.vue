<template>
  <div id="login_app">
    <section class="hero is-fullheight-with-navbar is-bold">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-6">
              <p class="title">
                SearchYourGuru
              </p>
              <p class="subtitle">Login Now</p>
              <div class="box">
                <LoginForm redirectTo="/dashboard/" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import LoginForm from '@/components/forms/LoginForm.vue'
export default {
  name: 'Login',
  components: {
    LoginForm
  }
}
</script>

<style></style>
