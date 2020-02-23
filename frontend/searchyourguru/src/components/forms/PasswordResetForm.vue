<template>
  <div>
    <article class="message is-success" v-if="verification_msg != null">
      <div class="message-body">
        <p>{{ verification_msg }}</p>
      </div>
    </article>
    <form action="#" v-on:submit.prevent="resend_reset_email" method="POST">
      <div class="field">
        <label class="label">Email</label>
        <p class="control">
          <input
            v-model="reset_email"
            class="input"
            type="email"
            placeholder="eg: abc@gmail.com"
            required
          />
        </p>
        <p class="help is-danger" v-if="reset_email_error == true">
          Please enter a valid email
        </p>
      </div>
      <article class="message is-danger" v-if="error_msg != null">
        <div class="message-body">
          {{ error_msg }}
        </div>
      </article>
      <div class="field">
        <p class="control">
          <button
            type="submit"
            v-on:submit="resend_reset_email"
            class="button is-success"
            v-bind:class="{ 'is-loading': is_loading }"
          >
            Get password reset mail
          </button>
        </p>
      </div>
    </form>
    <hr />
    <p>
      Dont have an account,
      <router-link to="/signup/">Register here</router-link>
    </p>
    <p>
      Account already activated,
      <router-link to="/login/">Login here</router-link>
    </p>
  </div>
</template>

<script>
import axios from 'axios'
import ValidatorsMixin from '@/components/mixins/ValidatorsMixin.vue'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'

export default {
  name: 'PasswordResetForm',
  data: function() {
    return {
      reset_email: null,
      reset_email_error: false,
      is_loading: false,
      error_msg: null,
      verification_msg: null
    }
  },
  methods: {
    resend_reset_email: function() {
      this.error_msg = null
      this.verification_msg = null
      this.reset_email_error = false
      this.verification_msg = null

      if (this.validEmail(this.reset_email) == false) {
        this.reset_email_error = true
      } else {
        this.is_loading = true
        axios
          .post(
            this.get_endpoint(this.endpoints.password_reset),
            {
              email: this.reset_email
            },
            this.guest_headers()
          )
          .then(
            () => {
              this.is_loading = false
              this.verification_msg =
                'Password Reset mail has been sent. If not received try again after 60 seconds.'
            },
            error => {
              this.is_loading = false
              this.error_msg = error.response.data.detail[0]
            }
          )
      }
    }
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>

<style></style>
