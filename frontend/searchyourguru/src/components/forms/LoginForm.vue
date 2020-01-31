<template>
  <div>
    <article class="message is-danger" v-if="verification_email != null">
      <div class="message-body">
        <p>Hii {{ verification_email }},</p>
        <p>
          Your account is not verified, please verify it first to continue using
          our services.
        </p>
        <hr />
        <router-link class="button is-info" to="/verification/"
          >Verify Account</router-link
        >
      </div>
    </article>

    <form
      action="#"
      v-on:submit.prevent="login"
      method="POST"
      v-if="verification_email == null"
    >
      <div class="field">
        <p class="control has-icons-left has-icons-right">
          <input
            v-model="login_email"
            class="input"
            type="email"
            placeholder="Email"
          />
          <span class="icon is-small is-left">
            <i class="fas fa-envelope"></i>
          </span>
          <span class="icon is-small is-right">
            <i class="fas fa-check"></i>
          </span>
        </p>
        <p class="help is-danger" v-if="login_email_error == true">
          Please enter a valid email
        </p>
      </div>
      <div class="field">
        <p class="control has-icons-left">
          <input
            v-model="login_password"
            class="input"
            type="password"
            placeholder="Password"
          />
          <span class="icon is-small is-left">
            <i class="fas fa-lock"></i>
          </span>
        </p>
        <p class="help is-danger" v-if="login_password_error == true">
          Please enter password
        </p>
      </div>

      <article class="message is-danger" v-if="login_error_message != null">
        <div class="message-body">
          {{ login_error_message }}
        </div>
      </article>

      <div class="field">
        <p class="control">
          <button
            type="submit"
            v-on:submit="login"
            id="login-btn"
            class="button is-success"
            v-bind:class="{ 'is-loading': is_login_loading }"
          >
            Login
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
      Forgot password ?
      <router-link to="/password-reset/">Reset now</router-link>
    </p>
  </div>
</template>

<script>
import axios from 'axios'
import ValidatorsMixin from '@/components/mixins/ValidatorsMixin.vue'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'

export default {
  name: 'LoginForm',
  data: function() {
    return {
      login_email: '',
      login_password: '',
      login_error_message: null,
      login_email_error: false,
      login_password_error: false,
      is_login_loading: false,
      verification_email: null
    }
  },
  methods: {
    login: function() {
      this.login_email_error = false
      this.login_password_error = false
      this.verification_email = null

      if (this.validEmail(this.login_email) == false) {
        this.login_email_error = true
      } else if (this.login_password == '') {
        this.login_password_error = true
      } else {
        this.login_error_message = null
        this.is_login_loading = true
        axios
          .post(
            this.get_endpoint(this.endpoints.login),
            {
              email: this.login_email,
              password: this.login_password
            },
            this.guest_headers()
          )
          .then(
            response => {
              this.is_login_loading = false
              localStorage.setItem('user-token', response.data.access)
              localStorage.setItem('user-token-refresh', response.data.refresh)
              localStorage.setItem('user-is-authenticated', true)
              this.$router.push('/dashboard/')
            },
            error => {
              let response = error.response.data.status[0]
              if (response == 'doesnotexist') {
                this.login_error_message =
                  'No active account found with the given credentials'
              }
              if (response == 'inactive') {
                this.verification_email = this.login_email
              }
              this.is_login_loading = false
            }
          )
      }
    }
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>

<style></style>
