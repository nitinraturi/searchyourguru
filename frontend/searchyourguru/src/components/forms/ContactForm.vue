<template>
  <div>
    <article class="message is-info" v-if="is_submitted == true">
      <div class="message-body">
        Your query has been successfully submitted
      </div>
    </article>
    <form
      action="#"
      method="POST"
      v-if="is_submitted == false"
      v-on:submit.prevent="submit_contact_form"
    >
      <div class="field">
        <label class="label">Name</label>
        <div class="control">
          <input
            type="text"
            :disabled="is_loading == true"
            v-model="contact.name"
            class="input"
            required
          />
        </div>
      </div>
      <div class="field">
        <label class="label">Email</label>
        <div class="control">
          <input
            type="email"
            :disabled="is_loading == true"
            v-model="contact.email"
            class="input"
            required
          />
        </div>
      </div>
      <div class="field">
        <label class="label">Subject</label>
        <div class="control">
          <input
            type="text"
            :disabled="is_loading == true"
            v-model="contact.subject"
            class="input"
            required
          />
        </div>
      </div>
      <div class="field">
        <label class="label">Message</label>
        <div class="control">
          <textarea
            class="textarea"
            v-model="contact.message"
            :disabled="is_loading == true"
            required
          ></textarea>
        </div>
      </div>
      <button
        type="submit"
        class="button is-link is-outlined"
        v-bind:class="{ 'is-loading': is_loading }"
        v-on:submit.prevent="submit_contact_form"
      >
        Submit
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import ValidatorsMixin from '@/components/mixins/ValidatorsMixin.vue'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'

export default {
  name: 'ContactForm',
  data: function() {
    return {
      contact: {
        name: '',
        email: '',
        subject: '',
        message: ''
      },
      is_loading: false,
      is_submitted: false
    }
  },
  methods: {
    submit_contact_form: function() {
      this.is_submitted = false
      this.is_loading = true
      axios
        .post(
          this.get_endpoint(this.endpoints.contact),
          this.contact,
          this.guest_headers()
        )
        .then(
          () => {
            this.is_loading = false
            this.is_submitted = true
          },
          () => {
            this.is_loading = false
          }
        )
    }
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>

<style></style>
