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
        :value="sub.code"
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
      key_event_end_time: null,
      pre_category_len: 0
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
    subject_keyword_changed: function() {
      this.key_event_end_time = new Date().getTime()

      if (
        this.category != null &&
        this.category != '' &&
        this.category.length > 0 &&
        // this.is_valid_time_duration() == true &&
        this.pre_category_len != this.category.length
      ) {
        this.pre_category_len = this.category.length
        // this.key_event_start_time = new Date().getTime()
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
