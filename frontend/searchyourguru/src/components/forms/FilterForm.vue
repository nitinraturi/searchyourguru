<template>
  <div>
    <form v-on:submit.prevent="search" method="get">
      <div class="columns is-multiline">
        <div class="column is-5">
          <div class="field">
            <label class="label">City or Pincode</label>
            <div class="control">
              <LocationFieldForm @location_changed="set_location_keyword" />
            </div>
            <p
              v-if="location_keyword_error != null"
              class="help is-small is-danger"
            >
              {{ location_keyword_error }}
            </p>
          </div>
        </div>
        <div class="column is-5">
          <div class="field">
            <label class="label">Subject</label>
            <div class="control">
              <CategoryFieldForm @category_changed="set_category" />
            </div>
            <p
              v-if="subject_keyword_error != null"
              class="help is-small is-danger"
            >
              {{ subject_keyword_error }}
            </p>
          </div>
        </div>
        <div class="column is-2">
          <div class="field">
            <label class="label" for="">...</label>
            <div class="control">
              <button
                type="submit"
                v-on:submit.prevent="search"
                class="button is-info is-outlined"
                v-bind:class="{ 'is-loading': is_search_loading }"
              >
                Search
              </button>
            </div>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
// import axios from 'axios'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'
import LocationFieldForm from '@/components/forms/LocationFieldForm.vue'
import CategoryFieldForm from '@/components/forms/CategoryFieldForm.vue'

export default {
  name: 'FilterForm',
  data: function() {
    return {
      is_search_loading: false,
      location_keyword: '',
      category: '',
      location_keyword_error: null,
      subject_keyword_error: null,
      valid_search_entries: false,
      suggested_subjects: []
    }
  },
  computed: {
    search_filters() {
      return this.$store.state.search_filters
    }
  },
  components: {
    LocationFieldForm,
    CategoryFieldForm
  },
  methods: {
    set_location_keyword: function(value) {
      this.location_keyword = value
    },
    set_category: function(value) {
      this.category = value
    },
    search: function() {
      this.location_keyword_error = null
      this.subject_keyword_error = null
      if (this.location_keyword == null || this.location_keyword == '') {
        this.location_keyword_error = 'Please select a valid location'
      } else if (this.category == null || this.category == '') {
        this.subject_keyword_error = 'Please select a valid subject'
      } else {
        this.$store.state.search_filters.location_keyword = this.location_keyword
        this.$store.state.search_filters.category = this.category
        localStorage.setItem(
          'search_filters',
          JSON.stringify(this.$store.state.search_filters)
        )
        this.$router.push('/search/')
      }
    }
  },
  mixins: [EndpointsMixin, RequestMixin]
}
</script>

<style></style>
