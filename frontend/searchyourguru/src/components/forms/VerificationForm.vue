<template>
  <div>
    <article class="message is-success" v-if="verification_msg != null">
      <div class="message-body">
        {{ verification_msg }}
      </div>
    </article>

    <form
      action="#"
      v-on:submit.prevent="resend_verification_email"
      method="POST"
    >
      <div class="field">
        <p class="control has-icons-left has-icons-right">
          <input
            v-model="verification_email"
            class="input"
            type="email"
            placeholder="Email"
            required
          />
          <span class="icon is-small is-left">
            <i class="fas fa-envelope"></i>
          </span>
          <span class="icon is-small is-right">
            <i class="fas fa-check"></i>
          </span>
        </p>
        <p class="help is-danger" v-if="verification_email_error == true">
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
            v-on:submit="resend_verification_email"
            class="button is-success"
            v-bind:class="{ 'is-loading': is_loading }"
          >
            Get verification mail
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
  name: 'VerificationForm',
  data: function() {
    return {
      verification_email: null,
      verification_email_error: false,
      is_loading: false,
      error_msg: null,
      verification_msg: null,
      app_state: 'login',
      source: ''
    }
  },
  methods: {
    resend_verification_email: function() {
      this.error_msg = null
      this.verification_msg = null
      this.verification_email_error = false

      if (this.validEmail(this.verification_email) == false) {
        this.verification_email_error = true
      } else {
        this.is_loading = true
        axios
          .post(
            this.get_endpoint(this.endpoints.account_activation),
            {
              email: this.verification_email
            },
            this.guest_headers()
          )
          .then(
            () => {
              this.is_loading = false
              this.verification_msg =
                'Verification mail has been sent. If not received try again after 60 seconds.'
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
