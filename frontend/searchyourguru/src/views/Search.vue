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
                            src="https://previews.123rf.com/images/triken/triken1608/triken160800028/61320729-male-avatar-profile-picture-default-user-avatar-guest-avatar-simply-human-head-vector-illustration-i.jpg"
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
                          {{ user.dob }}, {{ user.gender }}
                        </p>
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
                    <p class="is-size-7"><b>Exp</b>: {{ user.experience }}Y</p>
                    <p class="is-size-7"><b>Locality</b>: {{ user.zipcode }}</p>
                    <p class="is-size-7">
                      <b>Fees</b>: &#8377; {{ user.price_per_hour }} / Hour
                    </p>
                    <p class="is-size-7">
                      <b>Qualification</b>: {{ user.qualification }}
                    </p>
                    <p class="is-size-7"><b>Subject</b>: Mathematics</p>
                    <br />
                    <div class="field is-grouped is-grouped-centered">
                      <div class="control">
                        <button
                          type="button"
                          name="button"
                          class="button is-info is-outlined is-small"
                          v-on:click="ShowProfileQuickView"
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
    <div class="modal" v-bind:class="{ 'is-active': isActiveProfileQuickView }">
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
                  :disabled="isAuthenticated == false"
                >
                  Connect
                </button>
              </div>
              <div class="control" v-if="isAuthenticated == false">
                <router-link to="/login/">
                  Login to connect
                </router-link>
              </div>
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
import AdvancedFilterForm from '@/components/forms/AdvancedFilterForm.vue'
export default {
  data: function() {
    return {
      isActiveProfileQuickView: false
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
    ShowProfileQuickView: function() {
      this.isActiveProfileQuickView = true
    },
    HideProfileQuickView: function() {
      this.isActiveProfileQuickView = false
    }
  },
  components: {
    // FilterForm,
    AdvancedFilterForm
  }
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
