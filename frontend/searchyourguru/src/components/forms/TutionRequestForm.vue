<template>
  <div>
    <div class="table-container">
      <table class="table is-fullwidth">
        <thead>
          <tr>
            <td>Name</td>
            <td>Date</td>
            <td>IsAccepted</td>
            <td>Action</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="req in tution_requests" :key="req.id">
            <td>{{ req.student.name }}</td>
            <td>{{ req.created_at }}</td>
            <td>{{ req.is_accepted }}</td>
            <td>
              <button
                type="button"
                name="button"
                class="button is-info is-outlined is-small"
                v-on:click="ShowRequestQuickView"
              >
                View Profile
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Modal for profile quickview -->
    <div class="modal" v-bind:class="{ 'is-active': isActiveRequestQuickView }">
      <div class="modal-background"></div>
      <div class="modal-content">
        <div class="card box is-paddingless is-small">
          <div class="card-content">
            <div class="media">
              <div class="media-left">
                <figure class="image is-rounded is-48x48">
                  <img
                    src="https://previews.123rf.com/images/triken/triken1608/triken160800028/61320729-male-avatar-profile-picture-default-user-avatar-guest-avatar-simply-human-head-vector-illustration-i.jpg"
                    alt="Placeholder image"
                  />
                </figure>
              </div>
              <div class="media-content">
                <p class="title is-size-6">
                  Prabhu Deva <span class="tag is-primary">New</span>
                </p>
                <p class="subtitle is-size-7">24 Years old, Male</p>
              </div>
            </div>
            <p class="is-size-7">
              <b>Rating</b> - <span class="has-text-info">1</span>/5
            </p>
            <progress
              id="progress-bar"
              class="progress is-info is-small"
              value="20"
              max="100"
            ></progress>
            <p class="is-size-7"><b>Exp</b>: 2Y</p>
            <p class="is-size-7"><b>Locality</b>: Laxmi Nagar, Delhi</p>
            <p class="is-size-7"><b>Fees</b>: &#8377; 300 / Hour</p>
            <p class="is-size-7"><b>Qualification</b>: Phd</p>
            <p class="is-size-7"><b>Subject</b>: Mathematics</p>
            <br />
            <div class="field is-grouped is-grouped-centered">
              <div class="control">
                <button
                  type="button"
                  name="button"
                  class="button is-info is-small"
                >
                  Accept
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button
        class="modal-close is-large"
        aria-label="close"
        v-on:click="HideRequestQuickView"
      ></button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ValidatorsMixin from '@/components/mixins/ValidatorsMixin.vue'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'
export default {
  name: 'TutionRequestForm',
  data: function() {
    return {
      tution_requests: [],
      isActiveRequestQuickView: false,
      user: null
    }
  },
  mounted: function() {
    this.get_request_list()
  },
  methods: {
    ShowRequestQuickView: function() {
      this.isActiveRequestQuickView = true
    },
    HideRequestQuickView: function() {
      this.isActiveRequestQuickView = false
    },
    get_request_list: function() {
      axios
        .get(
          this.get_endpoint(this.endpoints.tution_request_list),
          this.get_headers()
        )
        .then(
          response => {
            // console.log(response)
            this.tution_requests = response.data.data
          },
          () => {
            // console.log(err)
          }
        )
    }
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin],
}
</script>

<style></style>
