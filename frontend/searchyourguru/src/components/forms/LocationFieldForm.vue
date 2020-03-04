<template>
  <div>
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
</template>

<script>
import axios from 'axios'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'
export default {
  name: 'LocationFieldForm',
  data: function() {
    return {
      suggested_cities: [],
      location_keyword: '',
      key_event_start_time: new Date().getTime(),
      key_event_end_time: null,
      pre_keyword_len: 0
    }
  },
  mixins: [EndpointsMixin, RequestMixin],
  methods: {
    is_valid_time_duration: function() {
      let elapsed_time = this.key_event_end_time - this.key_event_start_time
      if (elapsed_time / 1000 >= 0.5) {
        return true
      }
      return false
    },
    location_keyword_changed: function() {
      this.key_event_end_time = new Date().getTime()

      if (
        this.location_keyword != null &&
        this.location_keyword != '' &&
        this.location_keyword.length > 3 &&
        this.is_valid_time_duration() == true &&
        this.pre_keyword_len != this.location_keyword.length
      ) {
        this.key_event_start_time = new Date().getTime()
        this.pre_keyword_len = this.location_keyword.length
        this.$emit('location_changed', this.location_keyword)
        // console.log(e.keyCode, this.location_keyword)
        axios
          .post(
            this.get_endpoint(this.endpoints.suggested_cities),
            { location_keyword: this.location_keyword },
            this.guest_headers()
          )
          .then(
            response => {
              this.suggested_cities = response.data.data
              //   for (let city of this.suggested_cities) {
              //     if (this.location_keyword !== city.po_name) {
              //       this.location_keyword_error = 'Please select a valid option'
              //     } else {
              //       this.location_keyword_error = ''
              //       break
              //     }
              //   }
            },
            () => {}
          )
      }
    }
  }
}
</script>

<style></style>
