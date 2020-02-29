<template>
  <div>
    <div class="column is-full" v-if="connection_response != null">
      <p class="has-text-info has-text-centered">
        {{ connection_response }}
      </p>
    </div>
    <form
      action="#"
      method="POST"
      v-on:submit.prevent="AddConnection"
      v-if="connection_response == null"
    >
      <div class="columns is-multiline">
        <div class="column is-full">
          <div class="field">
            <label class="label is-size-7">Mobile</label>
            <div class="control">
              <input
                type="text"
                class="input is-small"
                placeholder="Eg: 9810141414"
                v-model="student_mobile"
                required
              />
            </div>
          </div>
          <p class="help is-danger" v-if="student_mobile_error != null">
            {{ student_mobile_error }}
          </p>
        </div>
        <div class="column is-full">
          <div class="field">
            <label class="label is-size-7">Locality</label>
            <div class="control">
              <textarea
                class="textarea is-small"
                placeholder="Eg: krishna nagar or east delhi or 110051"
                v-model="student_address"
                required
              ></textarea>
            </div>
          </div>
          <p class="help is-danger" v-if="student_address_error != null">
            {{ student_address_error }}
          </p>
        </div>
        <div class="column is-full">
          <div class="field is-grouped is-grouped-centered">
            <div class="control">
              <button
                type="submit"
                name="button"
                class="button is-small is-info"
                :disabled="isAuthenticated == false || is_loading == true"
                v-bind:class="{ 'is-loading': is_loading }"
                v-on:submit.prevent="AddConnection"
              >
                Request Demo Class
              </button>
            </div>
          </div>
        </div>
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
  name: 'TutionRequestDetailForm',
  data: function() {
    return {
      student_mobile: null,
      student_address: null,
      student_mobile_error: null,
      student_address_error: null,
      connection_response: null,
      is_loading: false
    }
  },
  props: ['tution'],
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated
    }
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin],
  methods: {
    AddConnection: function() {
      this.connection_response = null
      this.student_mobile_error = null
      this.student_address_error = null
      if (this.tution == null) {
        alert('something went wrong, please refresh the page')
      } else if (this.student_mobile == null || this.student_mobile == '') {
        this.student_mobile_error = 'This field is required'
      } else if (this.student_mobile.length != 10) {
        this.student_mobile_error = 'Please enter 10 digit phone number'
      } else if (this.student_address == null || this.student_address == '') {
        this.student_address_error = 'This field is required'
      } else {
        this.is_loading = true
        axios
          .post(
            this.get_endpoint(this.endpoints.tution_request_add),
            {
              tution: this.tution.id,
              phone: this.student_mobile,
              address: this.student_address
            },
            this.get_headers()
          )
          .then(
            () => {
              this.connection_response =
                'Request sent, wait for the tutor to accept your request'
              this.is_loading = false
            },
            err => {
              if (err.response.data.phone) {
                this.student_mobile_error = err.response.data.phone[0]
              } else {
                this.connection_response = err.response.data.detail[0]
              }
              this.is_loading = false
            }
          )
      }
    }
  }
}
</script>
