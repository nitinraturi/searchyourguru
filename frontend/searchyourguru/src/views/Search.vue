<template>
  <div id="search_app">
    <div>
      <a
        v-on:click.prevent.stop="show_mobile_filter"
        class="filter_icon_mobile is-hidden-desktop"
      >
        <figure class="image is-48x48">
          <img src="@/assets/filter.svg" alt="" />
        </figure>
      </a>
      <div
        class="modal"
        v-bind:class="{ 'is-active': isActiveFilterQuickView }"
      >
        <div class="modal-background"></div>
        <div class="modal-content">
          <div class="card box">
            <div class="card-content">
              <AdvancedFilterForm />
            </div>
          </div>
        </div>
        <button
          class="modal-close is-large"
          aria-label="close"
          v-on:click="hide_mobile_filter"
        ></button>
      </div>
    </div>

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
                  Finding a tution made easy
                </h1>
              </div>
            </section>
            <br />
            <div class="columns is-multiline">
              <div
                class="column is-4"
                v-for="t in filtered_tutions"
                :key="t.id"
              >
                <div class="card box is-paddingless is-small">
                  <div class="card-content">
                    <div class="media">
                      <p class="title is-size-6">
                        {{ t.title }}
                        <span class="tag is-primary">New</span>
                      </p>
                    </div>
                    <p class="is-size-7"><b>Pincode</b>: {{ t.area }}</p>
                    <p class="is-size-7">
                      <b>Fees</b>: &#8377; {{ t.price }} / Hour
                    </p>
                    <p class="is-size-7">
                      <b>Subject</b>: {{ t.category.name }}
                    </p>
                    <p class="is-size-7">
                      <b>Batch Size</b>: {{ t.batch_size }}
                    </p>
                    <br />
                    <div class="field is-grouped is-grouped-centered">
                      <div class="control">
                        <button
                          type="button"
                          name="button"
                          class="button is-info is-outlined is-small"
                          v-on:click="ShowProfileQuickView(t)"
                        >
                          Request Demo
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
      v-if="tution != null"
    >
      <div class="modal-background"></div>
      <div class="modal-content">
        <div class="card box is-paddingless is-small">
          <div class="card-content">
            <p class="title is-size-6">
              {{ tution.title }}
              <span class="tag is-primary">New</span>
            </p>
            <hr />
            <p class="subtitle is-6 has-text-centered">Tution Details</p>
            <p class="is-size-7"><b>Pincode</b>: {{ tution.area }}</p>
            <p class="is-size-7">
              <b>Fees</b>: &#8377; {{ tution.price }} / Hour
            </p>
            <p class="is-size-7"><b>Subject</b>: {{ tution.category.name }}</p>
            <p class="is-size-7"><b>Batch Size</b>: {{ tution.batch_size }}</p>
            <p class="is-size-7"><b>Posted On</b>: {{ tution.created_at }}</p>
            <p class="is-size-7"><b>Description</b></p>
            <p class="is-size-7">{{ tution.description }}</p>
            <hr />
            <p class="subtitle is-6 has-text-centered">Tutor Details</p>
            <p class="is-size-7"><b>Name</b>: {{ tution.tutor.name }}</p>
            <p class="is-size-7"><b>Exp</b>: {{ tution.tutor.experience }}Y</p>
            <p class="subtitle is-size-7">
              <b>Date of Birth</b>: {{ tution.tutor.dob }}
            </p>
            <p class="subtitle is-size-7">
              <span v-if="tution.tutor.gender == 1"><b>Gen</b>: Male</span>
              <span v-if="tution.tutor.gender == 2"><b>Gen</b>: Female</span>
              <span v-if="tution.tutor.gender == 3"><b>Gen</b>: Other</span>
            </p>
            <br />
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
                  Request Demo Class
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
      tution: null,
      connection_response: null,
      is_loading: false,
      isActiveFilterQuickView: false
    }
  },
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated
    },
    filtered_tutions() {
      return this.$store.state.filtered_tutions
    }
  },
  methods: {
    show_mobile_filter: function() {
      this.isActiveFilterQuickView = true
    },
    hide_mobile_filter: function() {
      this.isActiveFilterQuickView = false
    },
    ShowProfileQuickView: function(tution) {
      this.isActiveProfileQuickView = true
      this.tution = tution
    },
    HideProfileQuickView: function() {
      this.isActiveProfileQuickView = false
      this.tution = null
    },
    AddConnection: function() {
      this.connection_response = null
      if (this.tution != null) {
        this.is_loading = true
        axios
          .post(
            this.get_endpoint(this.endpoints.tution_request_add),
            {
              tutor_id: this.tution.id
            },
            this.get_headers()
          )
          .then(
            () => {
              this.connection_response =
                "Successfully Connected, Check your dashboard to see tutor's contact information"
              this.is_loading = false
            },
            err => {
              this.connection_response = err.response.data.detail[0]
              this.is_loading = false
            }
          )
      }
    }
  },
  components: {
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
.filter_icon_mobile {
  position: fixed;
  bottom: 10px;
  right: 10px;
}
</style>
