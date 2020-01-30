<template>
  <div id="login_app">
    <section class="hero is-fullheight-with-navbar is-bold">
      <div class="hero-body">
        <div class="container">
          <div class="columns">
            <div class="column is-6">
              <p class="title">
                SearchYourGuru
              </p>
              <p class="subtitle">Account Verification</p>
            </div>
            <div class="column is-6">
              <div class="box">
                <VerificationForm />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import VerificationForm from '@/components/forms/VerificationForm.vue'
export default {
  name: 'Verification',
  components: {
    VerificationForm
  }
}
</script>

<style></style>
