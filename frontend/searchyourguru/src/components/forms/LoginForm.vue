<template>
  <form action="#" v-on:submit.prevent="login" method="POST">
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
        [[login_error_message]]
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
</template>

<script>
import ValidatorsMixin from '@/components/mixins/ValidatorsMixin.vue'

export default {
  name: 'LoginForm',
  data: function() {
    return {
      login_endpoint: '/account/auth/login/',
      login_email: '',
      login_password: '',
      login_error_message: null,
      login_email_error: false,
      login_password_error: false,
      is_login_loading: false
    }
  },
  methods: {
    login: function() {
      this.login_email_error = true
      this.login_password_error = false
      if (this.validators.validEmail(this.login_email) == false) {
        this.login_email_error = true
      } else if (this.login_password == '') {
        this.login_password_error = true
      } else {
        this.login_error_message = null
        this.is_login_loading = true
        // axios
        //   .post(this.login_endpoint, {
        //     email: this.login_email,
        //     password: this.login_password
        //   })
        //   .then(
        //     response => {
        //       this.is_login_loading = false
        //       localStorage.setItem('user-token', response.data.access)
        //       localStorage.setItem('user-token-refresh', response.data.refresh)
        //       localStorage.setItem('user-is-authenticated', true)
        //       window.location = '/dashboard/'
        //     },
        //     error => {
        //       let response = error.response.data.status[0]
        //       if (response == 'doesnotexist') {
        //         this.login_error_message =
        //           'No active account found with the given credentials'
        //       }
        //       if (response == 'inactive') {
        //         window.location =
        //           '/verification/?source=login&verification_email=' +
        //           this.login_email
        //       }
        //       this.is_login_loading = false
        //     }
        //   )
      }
    }
  },
  mixins: [ValidatorsMixin]
}
</script>

<style></style>
