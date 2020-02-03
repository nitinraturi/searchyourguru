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
              <!-- <figure class="image">
                <img src="@/assets/education2.png" alt="" />
              </figure> -->
              <article class="message is-success">
                <div class="message-body">
                  <p>
                    If a child can’t learn the way we teach, maybe we should
                    teach the way they learn.
                  </p>
                </div>
              </article>
              <hr />
              <p>
                Already have an account,
                <router-link to="/login/">Login here</router-link>
              </p>
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
