<template>
  <div id="search_app">
    <!-- <section class="hero is-info is-bold is-small">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-8">
              <div class="box">
                <FilterForm />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section> -->

    <section class="section">
      <div class="container is-fluid">
        <div class="columns is-centered">
          <div class="column is-3 is-hidden-mobile is-hidden-tablet-only">
            <div class="sticky">
              <section class="hero is-info is-bold is-small">
                <div class="hero-body">
                  <h1 class="title is-6 has-text-centered">
                    Refine Search
                  </h1>
                </div>
              </section>
              <div class="card">
                <div class="card-content">
                  <AdvancedFilterForm />
                </div>
              </div>
            </div>
          </div>
          <div class="column is-9">
            <section class="hero is-info is-bold is-small">
              <div class="hero-body">
                <h1 class="title is-6 has-text-centered">
                  Find the right tutor or student
                </h1>
              </div>
            </section>
            <br />
            <div class="columns is-multiline">
              <div
                class="column is-4"
                v-for="user in filtered_users"
                :key="user.user_id"
              >
                <div class="card box is-paddingless is-small">
                  <div class="card-content">
                    <div class="media">
                      <div class="media-left">
                        <figure class="image is-rounded is-48x48">
                          <img
                            src="https://image.flaticon.com/icons/png/512/13/13471.png"
                            alt="Placeholder image"
                          />
                        </figure>
                      </div>
                      <div class="media-content">
                        <p class="title is-size-6">
                          {{ user.name }}
                          <span class="tag is-primary">New</span>
                        </p>
                        <p class="subtitle is-size-7">
                          <span v-if="user.gender == 1"><b>Gen</b>: Male</span>
                          <span v-if="user.gender == 2"
                            ><b>Gen</b>: Female</span
                          >
                          <span v-if="user.gender == 3"><b>Gen</b>: Other</span>
                        </p>
                      </div>
                    </div>
                    <!-- <p class="is-size-7">
                      <b>Rating</b> - <span class="has-text-info">1</span>/5
                    </p> -->
                    <!-- <progress
                      id="progress-bar"
                      class="progress is-info is-small"
                      value="20"
                      max="100"
                    ></progress> -->
                    <p class="is-size-7"><b>Exp</b>: {{ user.experience }}Y</p>
                    <p class="is-size-7"><b>Pincode</b>: {{ user.zipcode }}</p>
                    <p class="is-size-7">
                      <b>Fees</b>: &#8377; {{ user.price_per_hour }} / Hour
                    </p>
                    <!-- <p class="is-size-7">
                      <b>Qualification</b>: {{ user.qualification }}
                    </p> -->
                    <!-- <p class="is-size-7"><b>Subject</b>: Mathematics</p> -->
                    <p class="subtitle is-size-7">
                      <b>Date of Birth</b>: {{ user.dob }}
                    </p>
                    <br />
                    <div class="field is-grouped is-grouped-centered">
                      <div class="control">
                        <button
                          type="button"
                          name="button"
                          class="button is-info is-outlined is-small"
                          v-on:click="ShowProfileQuickView(user)"
                        >
                          View Profile
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Modal for profile quickview -->
    <div
      class="modal"
      v-bind:class="{ 'is-active': isActiveProfileQuickView }"
      v-if="user != null"
    >
      <div class="modal-background"></div>
      <div class="modal-content">
        <div class="card box is-paddingless is-small">
          <div class="card-content">
            <div class="media">
              <div class="media-left">
                <figure class="image is-rounded is-48x48">
                  <img
                    src="https://image.flaticon.com/icons/png/512/13/13471.png"
                    alt="Placeholder image"
                  />
                </figure>
              </div>
              <div class="media-content">
                <p class="title is-size-6">
                  {{ user.name }}
                  <span class="tag is-primary">New</span>
                </p>
                <p class="subtitle is-size-7">
                  <span v-if="user.gender == 1"><b>Gen</b>: Male</span>
                  <span v-if="user.gender == 2"><b>Gen</b>: Female</span>
                  <span v-if="user.gender == 3"><b>Gen</b>: Other</span>
                </p>
              </div>
            </div>
            <!-- <p class="is-size-7">
                      <b>Rating</b> - <span class="has-text-info">1</span>/5
                    </p> -->
            <!-- <progress
                      id="progress-bar"
                      class="progress is-info is-small"
                      value="20"
                      max="100"
                    ></progress> -->
            <p class="is-size-7"><b>Exp</b>: {{ user.experience }}Y</p>
            <p class="is-size-7"><b>Pincode</b>: {{ user.zipcode }}</p>
            <p class="is-size-7">
              <b>Fees</b>: &#8377; {{ user.price_per_hour }} / Hour
            </p>
            <!-- <p class="is-size-7">
                      <b>Qualification</b>: {{ user.qualification }}
                    </p> -->
            <!-- <p class="is-size-7"><b>Subject</b>: Mathematics</p> -->
            <p class="subtitle is-size-7">
              <b>Date of Birth</b>: {{ user.dob }}
            </p>
            <br />
            <p
              class="subtitle is-6 has-text-info has-text-centered"
              v-if="connection_response != null"
            >
              {{ connection_response }}
            </p>
            <div class="field is-grouped is-grouped-centered">
              <div class="control">
                <button
                  type="button"
                  name="button"
                  class="button is-info is-small"
                  :disabled="isAuthenticated == false || is_loading == true"
                  v-bind:class="{ 'is-loading': is_loading }"
                  v-on:click="AddConnection"
                >
                  Connect
                </button>
              </div>
            </div>
            <div class="" v-if="isAuthenticated == false">
              <h1 class="title is-5 has-text-danger">Login to Connect</h1>
              <LoginForm />
            </div>
          </div>
        </div>
      </div>
      <button
        class="modal-close is-large"
        aria-label="close"
        v-on:click="HideProfileQuickView"
      ></button>
    </div>
  </div>
</template>

<script>
// import FilterForm from '@/components/forms/FilterForm.vue'
import axios from 'axios'
import ValidatorsMixin from '@/components/mixins/ValidatorsMixin.vue'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'
import AdvancedFilterForm from '@/components/forms/AdvancedFilterForm.vue'
import LoginForm from '@/components/forms/LoginForm.vue'
export default {
  data: function() {
    return {
      isActiveProfileQuickView: false,
      user: null,
      connection_response: null,
      is_loading: false
    }
  },
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated
    },
    filtered_users() {
      return this.$store.state.filtered_users
    }
  },
  methods: {
    ShowProfileQuickView: function(user) {
      this.isActiveProfileQuickView = true
      this.user = user
    },
    HideProfileQuickView: function() {
      this.isActiveProfileQuickView = false
      this.user = null
    },
    AddConnection: function() {
      this.connection_response = null
      if (this.user != null) {
        this.is_loading = true
        axios
          .post(
            this.get_endpoint(this.endpoints.tution_request_add),
            {
              tutor_id: this.user.user__id
            },
            this.get_headers()
          )
          .then(
            response => {
              console.log(response)
              this.connection_response =
                "Successfully Connected, Check your dashboard to see tutor's contact information"
              this.is_loading = false
            },
            err => {
              console.log(err)
              this.connection_response = err.response.data.detail[0]
              this.is_loading = false
            }
          )
      }
    }
  },
  components: {
    // FilterForm,
    AdvancedFilterForm,
    LoginForm
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>

<style>
.sticky {
  position: sticky;
  top: 100px;
}
html {
  scroll-behavior: smooth;
}
</style>
