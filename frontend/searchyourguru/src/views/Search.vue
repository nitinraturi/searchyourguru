<template>
  <div id="search_app">
    <section class="hero is-info is-bold is-small">
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
    </section>

    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-3">
            <div class="card box">
              <h1 class="title is-5 has-text-centered">Filters</h1>
              <AdvancedFilterForm />
            </div>
          </div>
          <div class="column is-9">
            <div class="columns is-multiline">
              <div class="column is-4">
                <div class="card box">
                  <div class="card-image">
                    <div class="media">
                      <div class="media-left">
                        <figure class="image is-rounded is-96x96">
                          <img
                            src="https://previews.123rf.com/images/triken/triken1608/triken160800028/61320729-male-avatar-profile-picture-default-user-avatar-guest-avatar-simply-human-head-vector-illustration-i.jpg"
                            alt="Placeholder image"
                          />
                        </figure>
                      </div>
                      <div class="media-content">
                        <b>Prabhu Deva</b>
                        <p>24 Years old, Male</p>
                        <p>Exp: 2 Years</p>
                      </div>
                    </div>
                  </div>
                  <div class="card-content">
                    <p><b>Rating</b> - 1/5</p>
                    <progress
                      id="progress-bar"
                      class="progress is-info is-large"
                      value="20"
                      max="100"
                    ></progress>
                    <p>
                      <span class="icon is-small is-left">
                        <i class="fas fa-home"></i>
                      </span>
                      Laxmi Nagar, Delhi
                    </p>
                    <p>
                      <span class="icon is-small is-left">
                        <i class="fas fa-home"></i>
                      </span>
                      Post Graduate - MCA
                    </p>
                    <p>
                      <span class="icon is-small is-left">
                        <i class="fas fa-home"></i>
                      </span>
                      All Subjects
                    </p>
                    <hr />
                    <div class="field is-grouped is-grouped-centered">
                      <div class="control">
                        <button
                          type="button"
                          name="button"
                          class="button is-info is-outlined"
                        >
                          View Profile
                        </button>
                      </div>
                      <div class="control">
                        <button
                          type="button"
                          name="button"
                          class="button is-info"
                        >
                          Request a Demo
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
  </div>
</template>

<script>
import FilterForm from '@/components/forms/FilterForm.vue'
import AdvancedFilterForm from '@/components/forms/AdvancedFilterForm.vue'
export default {
  components: {
    FilterForm,
    AdvancedFilterForm
  }
}
</script>

<style></style>
