<template>
  <div>
    <div class="table-container" v-if="tution_list.length > 0">
      <table class="table is-fullwidth">
        <thead>
          <tr>
            <td>Tution Id</td>
            <td>Title</td>
            <td>Last Updated</td>
            <td>Status</td>
            <td></td>
            <td></td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="t in tution_list" :key="t.id">
            <td>{{ t.tution.id }}</td>
            <td>{{ t.tution.title }}</td>
            <td>{{ t.tution.updated_at }}</td>
            <td>
              <span v-if="t.is_accepted == true" class="has-text-success"
                >Accepted</span
              >
              <span v-if="t.is_accepted == false" class="has-text-danger"
                >Pending</span
              >
            </td>
            <td>
              <!-- <button
                type="button"
                name="button"
                class="button is-info is-outlined is-small"
                v-on:click="SetViewState(t)"
              >
                View
              </button> -->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-if="tution_list.length == 0">
      <p class="subtitle is-5">
        No tutions applied yet ! Search for a tution now.
      </p>
      <FilterForm />
    </div>

    <div
      class="modal"
      v-if="tution != null"
      v-bind:class="{ 'is-active': quickview != false }"
    >
      <div class="modal-background"></div>
      <div class="modal-content">
        <div class="card box is-paddingless is-small">
          <div class="card-content">
            <h1 class="title has-text-centered is-5">Tution Details</h1>
            <p><b>Title</b>: {{ tution.title }}</p>
            <p><b>Price</b>: {{ tution.price }}</p>
            <p><b>Area</b>: {{ tution.area }}</p>
            <p><b>Batch Size</b>: {{ tution.batch_size }}</p>
            <p><b>Create At</b>: {{ tution.created_at }}</p>
            <p><b>Updated At</b>: {{ tution.updated_at }}</p>
            <p><b>Subject</b>: {{ tution.category.name }}</p>
            <p><b>Description</b></p>
            <p>{{ tution.description }}</p>
          </div>
        </div>
      </div>
      <button
        class="modal-close is-large"
        aria-label="close"
        v-on:click="HideQuickView"
      ></button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ValidatorsMixin from '@/components/mixins/ValidatorsMixin.vue'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'
import FilterForm from '@/components/forms/FilterForm.vue'

export default {
  name: 'TutionAppliedForm',
  data: function() {
    return {
      tution_list: [],
      quickview: false,
      tution: null
    }
  },
  mounted: function() {
    this.get_request_list()
  },
  methods: {
    SetViewState: function(tution) {
      this.tution = tution
      this.quickview = true
    },
    HideQuickView: function() {
      this.quickview = false
      this.tution = null
    },
    get_request_list: function() {
      axios
        .get(
          this.get_endpoint(this.endpoints.tution_request_applied),
          this.get_headers()
        )
        .then(
          response => {
            // console.log(response)
            this.tution_list = response.data
          },
          () => {
            // console.log(err)
          }
        )
    }
  },
  components: {
    FilterForm
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>
