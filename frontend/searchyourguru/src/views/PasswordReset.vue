<template>
  <div id="password_reset_app">
    <section class="hero is-fullheight-with-navbar is-bold">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-6">
              <p class="title">
                SearchYourGuru.
              </p>
              <p class="subtitle">Password Reset</p>
              <div class="box">
                <PasswordResetForm />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import PasswordResetForm from '@/components/forms/PasswordResetForm.vue'

export default {
  name: 'PasswordReset',
  components: {
    PasswordResetForm
  }
}
</script>

<style></style>
