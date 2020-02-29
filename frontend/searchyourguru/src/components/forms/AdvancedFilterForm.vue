<template>
  <div class="">
    <form action="#" v-on:submit.prevent="search">
      <div class="field">
        <label for="" class="label is-size-7 has-text-grey"
          >Pincode or City</label
        >
        <div class="control">
          <input
            type="text"
            class="input is-small"
            placeholder="eg: Delhi or 110092"
            list="cities_list"
            :disabled="is_search_loading"
            v-model="search_filters.location_keyword"
            v-on:keyup="location_keyword_changed"
          />
          <datalist id="cities_list">
            <option
              v-for="city in suggested_cities"
              :key="city.id"
              :value="city.po_name"
              >{{ city.po_name }}</option
            >
          </datalist>
        </div>
      </div>

      <div class="field">
        <label for="#" class="label is-size-7 has-text-grey">Course</label>
        <div class="control">
          <input
            type="text"
            class="input is-small"
            placeholder="eg:Math"
            list="subjects_list"
            :disabled="is_search_loading"
            v-model="search_filters.category"
            v-on:keyup="subject_keyword_changed"
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

      <div class="field">
        <label for="#" class="label is-size-7 has-text-grey">Gender</label>
        <div class="control">
          <select
            class="input is-small"
            :disabled="is_search_loading"
            v-model="search_filters.gender"
          >
            <option value="1">Male</option>
            <option value="2">Female</option>
            <option value="3">Other</option>
          </select>
        </div>
      </div>

      <div class="field">
        <label class="label is-size-7 has-text-grey">Preferred Timings</label>
        <div class="control">
          <div class="select is-fullwidth">
            <select
              v-model="search_filters.timing"
              :disabled="is_search_loading"
              class="is-small is-size-7"
            >
              <option value="2">Morning</option>
              <option value="3">Afternoon</option>
              <option value="4">Evening</option>
              <option value="1">Anytime (7 AM - 7 PM)</option>
            </select>
          </div>
        </div>
      </div>

      <div>
        <label for="#" class="label is-size-7 has-text-grey"
          >Location Preference</label
        >
        <div class="field">
          <div class="control">
            <label class="checkbox is-small is-size-7">
              <input
                type="checkbox"
                :value="2"
                v-model="selected_locations"
                :disabled="is_search_loading"
              />
              <span> At Student's Home</span>
            </label>
          </div>
        </div>
        <div class="field">
          <div class="control">
            <label class="checkbox is-small is-size-7">
              <input
                type="checkbox"
                :value="1"
                v-model="selected_locations"
                :disabled="is_search_loading"
              />
              <span> At Tutors Home</span>
            </label>
          </div>
        </div>
        <div class="field">
          <div class="control">
            <label class="checkbox is-small is-size-7">
              <input
                type="checkbox"
                :value="3"
                v-model="selected_locations"
                :disabled="is_search_loading"
              />
              At Institute
            </label>
          </div>
        </div>
      </div>
      <div class="field">
        <label for="#" class="label is-size-7 has-text-grey"
          >Experience (Years)</label
        >
        <div class="control">
          <input
            type="number"
            class="input is-small"
            placeholder="eg:5"
            :disabled="is_search_loading"
            v-model="search_filters.experience"
          />
        </div>
      </div>

      <div class="field">
        <label for="#" class="label is-size-7 has-text-grey"
          >Per Hour Fees (Rs)</label
        >
        <div class="control">
          <input
            type="number"
            class="input is-small"
            placeholder="eg:300"
            :disabled="is_search_loading"
            v-model="search_filters.price_per_hour"
          />
        </div>
      </div>

      <div class="field">
        <p class="control">
          <button
            v-on:submit="search"
            type="submit"
            class="button is-info is-small"
            :disabled="is_search_loading"
            v-bind:class="{ 'is-loading': is_search_loading }"
          >
            Apply
          </button>
        </p>
      </div>
      <a
        v-on:click.prevent.stop="reset_filters"
        class="subtitle is-6 has-text-link"
        :disabled="is_search_loading"
      >
        Reset filters
      </a>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'
export default {
  name: 'AdvancedFilterForm',
  data: function() {
    return {
      is_search_loading: false,
      location_keyword: '',
      category: '',
      location_keyword_error: null,
      category_error: null,
      selected_locations: [],
      suggested_cities: [],
      suggested_subjects: []
    }
  },
  computed: {
    search_filters() {
      return this.$store.state.search_filters
    }
  },
  mounted: function() {
    this.initial_filters()
  },
  methods: {
    initial_filters: function() {
      if (
        this.search_filters.location_keyword != null &&
        this.search_filters.category != null
      ) {
        axios
          .post(
            this.get_endpoint(this.endpoints.tution_search),
            {
              location_keyword: this.search_filters.location_keyword,
              category: this.search_filters.category
            },
            this.guest_headers()
          )
          .then(
            response => {
              this.$store.state.filtered_tutions = response.data.data
            },
            () => {}
          )
      }
    },
    reset_filters: function() {
      this.search_filters.experience = null
      this.search_filters.price_per_hour = null
      this.search_filters.timing = null
      this.search_filters.gender = null
      this.search_filters.location_preferences = []
    },
    location_keyword_changed: function() {
      if (
        this.search_filters.location_keyword != null &&
        this.search_filters.location_keyword != '' &&
        this.search_filters.location_keyword.length > 3
      ) {
        axios
          .post(
            this.get_endpoint(this.endpoints.suggested_cities),
            { location_keyword: this.search_filters.location_keyword },
            this.guest_headers()
          )
          .then(
            response => {
              this.suggested_cities = response.data.data
            },
            () => {}
          )
      }
    },
    subject_keyword_changed: function() {
      if (
        this.search_filters.category != null &&
        this.search_filters.category != '' &&
        this.search_filters.category.length > 2
      ) {
        axios
          .post(
            this.get_endpoint(this.endpoints.suggested_subjects),
            { subject_keyword: this.search_filters.category },
            this.guest_headers()
          )
          .then(
            response => {
              this.suggested_subjects = response.data.data
            },
            () => {}
          )
      }
    },
    search: function() {
      let payload = {}
      this.location_keyword_error = null
      this.category_error = null
      if (
        this.search_filters.location_keyword == null ||
        this.search_filters.location_keyword == ''
      ) {
        this.location_keyword_error = 'Please enter a valid city or zipcode'
      } else if (
        this.search_filters.category == null ||
        this.search_filters.category == ''
      ) {
        this.category_error = 'Please enter a valid category'
      } else {
        payload['location_keyword'] = this.search_filters.location_keyword
        payload['category'] = this.search_filters.category

        if (
          this.search_filters.experience != null ||
          this.search_filters.experience != ''
        ) {
          payload['experience'] = this.search_filters.experience
        }

        if (this.search_filters.gender != null || this.search_filters.gender) {
          payload['gender'] = this.search_filters.gender
        }

        if (
          this.search_filters.price_per_hour != null ||
          this.search_filters.price_per_hour != 0
        ) {
          payload['price_per_hour'] = this.search_filters.price_per_hour
        }

        if (this.selected_locations.length > 0) {
          payload['location_preferences'] = this.selected_locations
        }

        if (
          this.search_filters.timing != null ||
          this.search_filters.timing != ''
        ) {
          payload['timing'] = this.search_filters.timing
        }

        this.is_search_loading = true
        axios
          .post(
            this.get_endpoint(this.endpoints.tution_search),
            payload,
            this.guest_headers()
          )
          .then(
            response => {
              this.$store.state.filtered_tutions = response.data.data
              this.is_search_loading = false
              this.$emit('filters_applied')
            },
            () => {
              this.is_search_loading = false
            }
          )
      }
    }
  },
  mixins: [EndpointsMixin, RequestMixin]
}
</script>

<style></style>
