<template>
  <div>
    <form action="#" v-on:submit.prevent="search" method="get">
      <div class="columns is-multiline">
        <div class="column is-5">
          <div class="field">
            <label class="label">City or Pincode</label>
            <div class="control">
              <p v-if="location_keyword_error != null" class="help is-small is-danger">{{ location_keyword_error }}</p>
              <input
                type="text"
                class="input"
                list="cities_list"
                placeholder="eg: Delhi or 110092"
                v-model="location_keyword"
                v-on:keyup="location_keyword_changed"
              />
              <datalist id="cities_list">
                <option
                  v-for="city in suggested_cities"
                  :key="city.id"
                  :value="city.po_name"
                  >{{ city.zipcode }} {{ city.po_name }}</option
                >
              </datalist>
            </div>
          </div>
        </div>
        <div class="column is-5">
          <div class="field">
            <label class="label">Subject</label>
            <div class="control">
              <p v-if="subject_keyword_error != null" class="help is-small is-danger">{{ subject_keyword_error }}</p>
              <input
                type="text"
                class="input"
                list="subjects_list"
                placeholder="eg:Math"
                v-on:keyup="subject_keyword_changed"
                v-model="category"
              />
              <datalist id="subjects_list">
                <option
                  v-for="sub in suggested_subjects"
                  :key="sub.code"
                  :value="sub.name"
                  >{{ sub.name }}</option
                >
              </datalist>
            </div>
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
import axios from 'axios'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'
export default {
  name: 'FilterForm',
  data: function() {
    return {
      is_search_loading: false,
      location_keyword: '',
      pre_location_keyword_len: 0,
      category: '',
      location_keyword_error: null,
      subject_keyword_error: null,
      valid_search_entries: false,
      suggested_cities: [],
      suggested_subjects: []
    }
  },
  computed: {
    search_filters() {
      return this.$store.state.search_filters
    }
  },
  methods: {
    location_keyword_changed: function() {
      if (
        this.location_keyword != null &&
        this.location_keyword != '' &&
        this.location_keyword.length > 3 &&
        this.location_keyword.length != this.pre_location_keyword_len
      ) {
        this.pre_location_keyword_len = this.location_keyword.length
        axios
          .post(
            this.get_endpoint(this.endpoints.suggested_cities),
            { location_keyword: this.location_keyword },
            this.guest_headers()
          )
          .then(
            response => {
              this.suggested_cities = response.data.data
              for (let city of this.suggested_cities) {
                if (this.location_keyword !== city.po_name) {
                    this.location_keyword_error = 'Please select a valid option'
                } else {
                    this.location_keyword_error = ''
                    break
                }
              }
            },
            () => {}
          )
      }
    },
    subject_keyword_changed: function() {
      if (
        this.category != null &&
        this.category != '' &&
        this.category.length > 2
      ) {
        axios
          .post(
            this.get_endpoint(this.endpoints.suggested_subjects),
            { subject_keyword: this.category },
            this.guest_headers()
          )
          .then(
            response => {
              this.suggested_subjects = response.data.data
              for (let subject of this.suggested_subjects) {
                if (this.category !== subject.name) {
                    this.subject_keyword_error = 'Please select a valid option'
                } else {
                    this.subject_keyword_error = ''
                    break
                }
              }
            },
            () => {}
          )
      }
    },
    search: function() {
        this.$store.state.search_filters.location_keyword = this.location_keyword
        this.$store.state.search_filters.category = this.category
        localStorage.setItem(
          'search_filters',
          JSON.stringify(this.$store.state.search_filters)
        )
        this.$router.push('/search/')
    }
  },
  mixins: [EndpointsMixin, RequestMixin]
}
</script>

<style></style>
