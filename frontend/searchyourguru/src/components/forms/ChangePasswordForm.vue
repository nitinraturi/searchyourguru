<template>
  <div>
    <article class="message is-success" v-if="verification_msg != null">
      <div class="message-body">
        <p>{{ verification_msg }}</p>
      </div>
    </article>
    <form
      action="#"
      v-on:submit.prevent="change_password"
      method="POST"
      v-if="verification_msg == null"
    >
      <div class="field">
        <p class="control has-icons-left">
          <input
            class="input"
            id="user_email"
            type="email"
            placeholder="email"
            value=""
            required
            disabled
          />
          <span class="icon is-small is-left">
            <i class="fas fa-lock"></i>
          </span>
        </p>
      </div>
      <div class="field">
        <p class="control has-icons-left">
          <input
            v-model="new_password"
            class="input"
            type="password"
            placeholder="New Password"
            required
          />
          <span class="icon is-small is-left">
            <i class="fas fa-lock"></i>
          </span>
        </p>
        <p class="help is-danger" v-if="new_password_error == true">
          Please enter password
        </p>
      </div>
      <div class="field">
        <p class="control has-icons-left">
          <input
            v-model="confirm_new_password"
            class="input"
            type="password"
            placeholder="Confirm New Password"
            required
          />
          <span class="icon is-small is-left">
            <i class="fas fa-lock"></i>
          </span>
        </p>
        <p class="help is-danger" v-if="confirm_new_password_error == true">
          Please enter confirm password
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
            v-on:submit="change_password"
            class="button is-success"
            v-bind:class="{ 'is-loading': is_loading }"
          >
            Change Password
          </button>
        </p>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import ValidatorsMixin from '@/components/mixins/ValidatorsMixin.vue'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'

export default {
  name: 'ChangePasswordForm',
  data: function() {
    return {
      new_password: null,
      new_password_error: null,
      confirm_new_password: null,
      confirm_new_password_error: null,
      is_loading: false,
      error_msg: null,
      verification_msg: null
    }
  },
  methods: {
    change_password: function() {
      this.error_msg = null
      this.new_password_error = null
      this.confirm_new_password_error = null
      this.verification_msg = null

      if (this.new_password == '') {
        this.new_password_error = true
      } else if (this.confirm_new_password == '') {
        this.confirm_new_password_error = true
      } else {
        this.is_loading = true
        axios
          .post(
            this.get_endpoint(this.endpoints.change_password),
            {
              email: document.querySelector('#user_email').value,
              password: this.new_password,
              confirm_password: this.confirm_new_password
            },
            this.guest_headers()
          )
          .then(
            () => {
              this.is_loading = false
              this.verification_msg = 'Password has been successfully changed.'
              setTimeout(function() {
                window.location = '/login/'
              }, 5000)
            },
            error => {
              console.log(error.response)
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
