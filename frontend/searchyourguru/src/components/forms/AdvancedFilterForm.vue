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
            :disabled="is_search_loading"
            v-model="search_filters.location_keyword"
          />
        </div>
      </div>

      <div class="field">
        <label for="#" class="label is-size-7 has-text-grey">Course</label>
        <div class="control">
          <input
            type="text"
            class="input is-small"
            placeholder="eg:Math"
            :disabled="is_search_loading"
            v-model="search_filters.category"
          />
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
            class="button is-success is-small"
            v-bind:class="{ 'is-loading': is_search_loading }"
          >
            Apply
          </button>
        </p>
      </div>
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
      selected_locations: []
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
              this.$store.state.filtered_users = response.data.data
            },
            error => {
              console.log(error)
            }
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
          console.log('sl', this.selected_locations)
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
              console.log(response)
              this.$store.state.filtered_users = response.data.data
              this.is_search_loading = false
            },
            error => {
              this.is_search_loading = false
              console.log(error)
            }
          )
      }
    }
  },
  mixins: [EndpointsMixin, RequestMixin]
}
</script>

<style></style>
