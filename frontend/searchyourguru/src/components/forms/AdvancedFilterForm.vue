<template>
  <div class="">
    <form action="#" v-on:submit.prevent="apply_search">
      <div class="columns is-multiline">
        <div class="column is-full">
          <div class="field">
            <label for="" class="label is-size-7 has-text-grey"
              >Pincode or City</label
            >
            <div class="control">
              <p v-if="location_keyword_error != null" class="help is-small is-danger">{{ location_keyword_error }}</p>
              <input
                type="text"
                class="input is-small"
                placeholder="eg: Delhi or 110092"
                list="cities_list"
                :disabled="is_search_loading"
                v-model="search.location_keyword"
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
        </div>
      </div>

      <div class="field">
        <label for="#" class="label is-size-7 has-text-grey">Course</label>
        <div class="control">
          <p v-if="subject_keyword_error != null" class="help is-small is-danger">{{ subject_keyword_error }}</p>
          <input
            type="text"
            class="input is-small"
            placeholder="eg:Math"
            list="subjects_list"
            :disabled="is_search_loading"
            v-model="search.category"
            v-on:keyup="subject_keyword_changed"
          />
          <datalist id="subjects_list">
            <option
              v-for="sub in suggested_subjects"
              :key="sub.code"
              :value="sub.name"
              >{{ sub.code }} {{ sub.name }}</option
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
            v-model="search.gender"
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
              v-model="search.timing"
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
            v-model="search.experience"
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
            v-model="search.price_per_hour"
          />
        </div>
      </div>

      <div class="field">
        <p class="control">
          <button
            v-on:submit="apply_search"
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
      subject_keyword_error: null,
      selected_locations: [],
      suggested_cities: [],
      suggested_subjects: [],
      search: {
        location_keyword: '',
        category: '',
        experience: null,
        price_per_hour: null,
        qualification: null,
        timing: null,
        gender: null,
        location_preferences: []
      }
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
      this.search.location_keyword = this.search_filters.location_keyword
      this.search.category = this.search_filters.category
      if (
        this.search.location_keyword != null &&
        this.search.category != null
      ) {
        axios
          .post(
            this.get_endpoint(this.endpoints.tution_search),
            {
              location_keyword: this.search.location_keyword,
              category: this.search.category
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
      this.search.experience = null
      this.search.price_per_hour = null
      this.search.timing = null
      this.search.gender = null
      this.search.location_preferences = []
    },
    location_keyword_changed: function(e) {
      if (e.keyCode === 37 || e.keyCode === 39) {
        console.log('arrow keys pressed')
      } else {
      if (
        (this.search.location_keyword != null &&
        this.search.location_keyword != '') ||
        this.search.location_keyword.length > 3
      ) {
        axios
          .post(
            this.get_endpoint(this.endpoints.suggested_cities),
            { location_keyword: this.search.location_keyword },
            this.guest_headers()
          )
          .then(
            response => {
              this.suggested_cities = response.data.data
              for (let city of this.suggested_cities) {
                if (this.search.location_keyword !== city.po_name) {
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
     }
    },
    subject_keyword_changed: function(e) {
      if (e.keyCode === 37 || e.keyCode === 39) {
        console.log('arrow keys pressed')
      } else {
      if (
        (this.search.category != null &&
        this.search.category != '') ||
        this.search.category.length > 2
      ) {
        axios
          .post(
            this.get_endpoint(this.endpoints.suggested_subjects),
            { subject_keyword: this.search.category },
            this.guest_headers()
          )
          .then(
            response => {
              this.suggested_subjects = response.data.data
              for(let subject of this.suggested_subjects) {
                if (this.search.category !== subject.name) {
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
     }
    },
    apply_search: function() {
        let payload = {}
        payload['location_keyword'] = this.search.location_keyword
        payload['category'] = this.search.category

        if (this.search.experience != null || this.search.experience != '') {
          payload['experience'] = this.search.experience
        }

        if (this.search.gender != null || this.search.gender) {
          payload['gender'] = this.search.gender
        }

        if (
          this.search.price_per_hour != null ||
          this.search.price_per_hour != 0
        ) {
          payload['price_per_hour'] = this.search.price_per_hour
        }

        if (this.selected_locations.length > 0) {
          payload['location_preferences'] = this.selected_locations
        }

        if (this.search.timing != null || this.search.timing != '') {
          payload['timing'] = this.search.timing
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
  },
  mixins: [EndpointsMixin, RequestMixin]
}
</script>

<style></style>
