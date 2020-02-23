<template>
  <div>
    <div class="table-container">
      <table class="table is-fullwidth">
        <thead>
          <tr>
            <td>Tution Id</td>
            <td>Title</td>
            <td>Last Updated</td>
            <td></td>
            <td></td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="t in tution_list" :key="t.id">
            <td>{{ t.id }}</td>
            <td>{{ t.title }}</td>
            <td>{{ t.updated_at }}</td>
            <td>
              <button
                type="button"
                name="button"
                class="button is-info is-outlined is-small"
                v-on:click="ShowRequestQuickView"
              >
                View
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ValidatorsMixin from '@/components/mixins/ValidatorsMixin.vue'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'
export default {
  name: 'TutionManageForm',
  data: function() {
    return {
      tution_list: [],
      isActiveRequestQuickView: false,
      user: null
    }
  },
  mounted: function() {
    this.get_request_list()
  },
  methods: {
    ShowRequestQuickView: function() {
      this.isActiveRequestQuickView = true
    },
    HideRequestQuickView: function() {
      this.isActiveRequestQuickView = false
    },
    get_request_list: function() {
      axios
        .post(
          this.get_endpoint(this.endpoints.tution_list),
          {},
          this.get_headers()
        )
        .then(
          response => {
            // console.log(response)
            this.tution_list = response.data.data
          },
          () => {
            // console.log(err)
          }
        )
    }
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>
