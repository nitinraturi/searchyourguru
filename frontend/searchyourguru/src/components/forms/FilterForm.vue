<template>
  <div>
    <form action="#" v-on:submit.prevent="search" method="get">
      <div class="field">
        <label class="label">City | Pincode</label>
        <div class="control">
          <input
            type="text"
            class="input"
            placeholder="eg: Delhi or 110092"
            v-model="location_keyword"
          />
        </div>
        <p class="help is-danger" v-if="location_keyword_error != null">
          {{ location_keyword_error }}
        </p>
      </div>
      <div class="field">
        <label class="label">Course</label>
        <div class="control">
          <input
            type="text"
            class="input"
            placeholder="eg:Math"
            v-model="category"
          />
        </div>
        <p class="help is-danger" v-if="category_error != null">
          {{ category_error }}
        </p>
      </div>
      <div class="field">
        <p class="control">
          <button
            type="submit"
            v-on:submit.prevent="search"
            class="button is-success"
            v-bind:class="{ 'is-loading': is_search_loading }"
          >
            Search
          </button>
        </p>
      </div>
    </form>
  </div>
</template>

<script>
// import axios from 'axios'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'
export default {
  name: 'FilterForm',
  data: function() {
    return {
      is_search_loading: false,
      location_keyword: '',
      category: '',
      location_keyword_error: null,
      category_error: null
    }
  },
  computed: {
    search_filters() {
      return this.$store.state.search_filters
    }
  },
  methods: {
    search: function() {
      this.location_keyword_error = null
      this.category_error = null
      if (this.location_keyword == null || this.location_keyword == '') {
        this.location_keyword_error = 'Please enter a valid city or zipcode'
      } else if (this.category == null || this.category == '') {
        this.category_error = 'Please enter a valid category'
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
