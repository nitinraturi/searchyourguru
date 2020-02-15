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
      <div class="columns is-multiline">
        <div class="column is-5">
          <div class="field">
            <label class="label">Email</label>
            <p class="control has-icons-left has-icons-right">
              <input
                v-model="login_email"
                class="input"
                type="email"
                :disabled="is_login_loading == true"
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
        </div>

        <div class="column is-5">
          <div class="field">
            <label class="label">Password</label>
            <p class="control has-icons-left">
              <input
                v-model="login_password"
                class="input"
                type="password"
                :disabled="is_login_loading == true"
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
        </div>

        <div class="column is-2">
          <div class="field">
            <label class="label">...</label>
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
        </div>

        <div class="column is-full" v-if="login_error_message != null">
          <article class="message is-danger" v-if="login_error_message != null">
            <div class="message-body">
              {{ login_error_message }}
            </div>
          </article>
        </div>
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
              localStorage.setItem('guru-user-token', response.data.access)
              localStorage.setItem(
                'guru-user-token-refresh',
                response.data.refresh
              )
              localStorage.setItem('syg_user_type', response.data.user_type)
              this.$store.state.isAuthenticated = true
              if (this.redirectTo != null) {
                this.$router.push(this.redirectTo)
              }
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
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin],
  props: ['redirectTo']
}
</script>

<style></style>
