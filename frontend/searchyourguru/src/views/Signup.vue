<template>
  <div id="signup_app">
    <section class="hero is-fullheight-with-navbar is-bold">
      <div class="hero-body">
        <div class="container">
          <div class="columns">
            <div class="column is-6">
              <p class="title">
                We Help Students and Tutors Find Each Other
              </p>
              <p class="subtitle">Free Registration</p>
            </div>
            <div class="column is-6">
              <div>
                <div class="box">
                  <SignupForm />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import SignupForm from '@/components/forms/SignupForm.vue'
export default {
  name: 'Signup',
  components: {
    SignupForm
  }
}
</script>

<style></style>
