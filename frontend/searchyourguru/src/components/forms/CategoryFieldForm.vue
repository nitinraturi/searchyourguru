<template>
  <div>
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
</template>

<script>
import axios from 'axios'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'
export default {
  name: 'LocationFieldForm',
  data: function() {
    return {
      suggested_subjects: [],
      category: '',
      key_event_start_time: new Date().getTime(),
      key_event_end_time: null
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
    is_valid_key_strokes: function(e) {
      let keyCode = e.which || e.keyCode
      if (
        (keyCode >= 65 && keyCode <= 90) ||
        (keyCode >= 97 && keyCode <= 122) ||
        (keyCode >= 43 && keyCode <= 53) ||
        (keyCode >= 29 && keyCode <= 54) ||
        (keyCode >= 7 && keyCode <= 16)
      ) {
        return true
      }
      return false
    },
    subject_keyword_changed: function(e) {
      this.key_event_end_time = new Date().getTime()

      if (
        this.category != null &&
        this.category != '' &&
        this.category.length > 3 &&
        this.is_valid_time_duration() == true &&
        this.is_valid_key_strokes(e) == true
      ) {
        this.key_event_start_time = new Date().getTime()
        this.$emit('category_changed', this.category)
        // console.log(e.keyCode, this.category)
        axios
          .post(
            this.get_endpoint(this.endpoints.suggested_subjects),
            { subject_keyword: this.category },
            this.guest_headers()
          )
          .then(
            response => {
              this.suggested_subjects = response.data.data
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
