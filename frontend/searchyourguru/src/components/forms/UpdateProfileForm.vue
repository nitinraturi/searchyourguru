<template>
  <div>
    <form
      action="#"
      v-on:submit.prevent="save_formdata('general_settings')"
      method="POST"
    >
      <!-- Email -->
      <div class="field">
        <p class="control">
          <input
            v-model="general_settings.user_email"
            class="input"
            type="email"
            placeholder="Email"
            required
            disabled
          />
        </p>
        <p
          class="help is-danger"
          v-if="general_settings.user_email_error != null"
        >
          {{ general_settings.user_email_error }}
        </p>
      </div>

      <!-- Phone -->
      <div class="field">
        <p class="control">
          <input
            v-model="general_settings.user_phone"
            class="input"
            type="number"
            placeholder="Your Mobile Number"
            required
            disabled
          />
        </p>
        <p
          class="help is-danger"
          v-if="general_settings.user_phone_error != null"
        >
          {{ general_settings.user_phone_error }}
        </p>
      </div>

      <!-- Name -->
      <div class="field">
        <p class="control">
          <input
            v-model="general_settings.user_name"
            class="input"
            type="text"
            placeholder="Full Name"
            required
            v-bind:disabled="general_settings.edit_mode == false"
          />
        </p>
        <p
          class="help is-danger"
          v-if="general_settings.user_name_error != null"
        >
          {{ general_settings.user_name_error }}
        </p>
      </div>

      <div class="field">
        <p class="control">
          <button
            type="submit"
            v-on:submit="save_formdata('general_settings')"
            class="button"
            v-bind:class="{
              'is-loading': general_settings.is_loading,
              'is-danger': general_settings.edit_mode,
              'is-success': !general_settings.edit_mode
            }"
          >
            {{ general_settings.mode_text }}
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
  name: 'UpdateProfileForm',
  data: function() {
    return {
      general_settings: {
        user_name: '',
        user_name_error: null,
        user_phone: '',
        user_phone_error: null,
        user_email: '',
        user_email_error: null,
        edit_mode: false,
        mode_text: 'Edit',
        is_loading: false
      }
    }
  },
  mounted: function() {
    this.get_user_profile()
  },
  methods: {
    update_general_profile: function() {
      this.general_settings.is_loading = true
      axios
        .post(
          this.get_endpoint(this.endpoints.update_user_profile),
          {
            name: this.general_settings.user_name
          },
          this.get_headers()
        )
        .then(
          () => {
            this.general_settings.is_loading = false
          },
          () => {
            this.general_settings.is_loading = false
          }
        )
    },
    get_user_profile: function() {
      let config = this.get_headers()
      axios.get(this.get_endpoint(this.endpoints.user_profile), config).then(
        response => {
          let res = response.data
          this.is_loading = false
          this.general_settings.user_name = res.name
          this.general_settings.user_email = res.email
          this.general_settings.user_phone = res.phone
        },
        () => {
          this.is_loading = false
        }
      )
    },
    save_formdata: function(source) {
      // general_settings form toggle
      if (source == 'general_settings') {
        this.general_settings.edit_mode = !this.general_settings.edit_mode
        if (this.general_settings.edit_mode == true) {
          this.general_settings.mode_text = 'Save'
        } else {
          this.general_settings.mode_text = 'Edit'
          this.update_general_profile()
        }
      }
    }
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>

<style></style>
