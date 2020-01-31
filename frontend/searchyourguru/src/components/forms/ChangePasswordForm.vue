<template>
  <div>
    <form
      action="#"
      v-on:submit.prevent="save_formdata('change_password')"
      method="POST"
    >
      <!-- Old Password -->
      <div class="field">
        <p class="control has-icons-left">
          <input
            v-model="change_password.old_password"
            class="input"
            type="password"
            placeholder="Current Password"
            required
          />
          <span class="icon is-small is-left">
            <i class="fas fa-lock"></i>
          </span>
        </p>
      </div>

      <!-- New Password -->
      <div class="field">
        <p class="control has-icons-left">
          <input
            v-model="change_password.new_password"
            class="input"
            type="password"
            placeholder="New Password"
            required
          />
          <span class="icon is-small is-left">
            <i class="fas fa-lock"></i>
          </span>
        </p>
      </div>

      <!-- Confirm New Password -->
      <div class="field">
        <p class="control has-icons-left">
          <input
            v-model="change_password.confirm_new_password"
            class="input"
            type="password"
            placeholder="Confirm New Password"
            required
          />
          <span class="icon is-small is-left">
            <i class="fas fa-lock"></i>
          </span>
        </p>
      </div>

      <article
        class="message is-danger"
        v-if="change_password.error_msg != null"
      >
        <div class="message-body">
          {{ change_password.error_msg }}
        </div>
      </article>

      <div class="field">
        <p class="control">
          <button
            type="submit"
            v-on:submit="save_formdata('change_password')"
            class="button is-success"
            v-bind:class="{ 'is-loading': change_password.is_loading }"
          >
            {{ change_password.mode_text }}
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
      change_password: {
        old_password: '',
        new_password: '',
        confirm_new_password: '',
        error_msg: null,
        mode_text: 'Update',
        is_loading: false
      }
    }
  },
  methods: {
    save_formdata: function(source) {
      // change_password form toggle
      if (source == 'change_password') {
        this.update_password()
      }
    },
    update_password: function() {
      this.change_password.is_loading = true
      this.change_password.error_msg = null
      axios
        .post(
          this.get_endpoint(this.endpoints.update_password),
          {
            old_password: this.change_password.old_password,
            new_password: this.change_password.new_password,
            confirm_new_password: this.change_password.confirm_new_password
          },
          this.get_headers()
        )
        .then(
          () => {
            this.change_password.is_loading = false
            this.change_password.error_msg = null
            this.change_password.old_password = ''
            this.change_password.new_password = ''
            this.change_password.confirm_new_password = ''
          },
          error => {
            this.change_password.error_msg = error.response.data.detail[0]
            this.change_password.is_loading = false
          }
        )
    }
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>

<style></style>
