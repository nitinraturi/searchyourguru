<template>
  <div>
    <div class="table-container" v-if="tution_list.length > 0">
      <table class="table is-fullwidth">
        <thead>
          <tr>
            <td>Tution Id</td>
            <td>Title</td>
            <td>Status</td>
            <td>Application Received</td>
            <td></td>
            <td></td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="t in tution_list" :key="t.id">
            <td>{{ t.id }}</td>
            <td>{{ t.title }}</td>
            <td>
              <span v-if="t.is_active == true" class="tag"
                >Active</span
              >
              <span v-if="t.is_active == false" class="tag is-danger"
                >Disabled</span
              >
            </td>
            <td>
              <span
                v-if="t.applications.length > 0"
                class="tag is-success is-rounded"
                >{{ t.applications.length }}</span
              >
              <span v-if="t.applications.length == 0" class="">{{
                t.applications.length
              }}</span>
            </td>
            <td>
              <button
                type="button"
                name="button"
                class="button is-success is-outlined is-small"
                :disabled="t.applications.length == 0"
                v-on:click="SetApplicationsState(t.applications)"
              >
                Applications
              </button>
            </td>
            <td>
              <button
                type="button"
                name="button"
                class="button is-info is-outlined is-small"
                v-on:click="SetViewState(t)"
              >
                Manage
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-if="tution_list.length == 0">
      <p class="subtitle is-5">No tutions created yet !</p>
      <p>
        Click on the <span class="has-text-link">new tution</span> button above
      </p>
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
            <form v-on:submit.prevent="update_tution">
              <div class="columns is-multiline is-mobile">
                <div class="column is-full">
                  <label class="label">Title</label>
                  <div class="field">
                    <p class="control">
                      <input
                        v-model="tution.title"
                        class="input"
                        type="text"
                        required
                        :disabled="tution_update_mode == false"
                      />
                    </p>
                  </div>
                </div>
                <div class="column is-full">
                  <div class="field">
                    <label class="label">Description</label>
                    <div class="control">
                      <textarea
                        class="textarea"
                        v-model="tution.description"
                        :disabled="tution_update_mode == false"
                        required
                      ></textarea>
                    </div>
                  </div>
                </div>
                <div class="column is-full">
                  <div class="columns is-multiline is-mobile">
                    <div class="column is-6">
                      <div class="field">
                        <label class="label">Preferred Timings</label>
                        <div class="control">
                          <div class="select is-fullwidth">
                            <select
                              v-model="tution.timing"
                              :disabled="tution_update_mode == false"
                              required
                            >
                              <option value="2">Morning</option>
                              <option value="3">Afternoon</option>
                              <option value="4">Evening</option>
                              <option value="1">Anytime (7 AM - 7 PM)</option>
                            </select>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="column is-6">
                      <div class="field">
                        <label class="label">Hourly Price</label>
                        <div class="control">
                          <input
                            type="number"
                            class="input"
                            v-model="tution.price"
                            :disabled="tution_update_mode == false"
                            required
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="column is-full">
                  <div class="columns is-multiline is-mobile">
                    <div class="column is-6">
                      <div class="field">
                        <label class="label">Location Preference</label>
                        <div class="control">
                          <div class="select is-fullwidth">
                            <select
                              v-model="tution.location"
                              :disabled="tution_update_mode == false"
                              required
                            >
                              <option value="1">At Tutor Home</option>
                              <option value="2">At Student Home</option>
                              <option value="3">At Institute</option>
                            </select>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="column is-6">
                      <div class="field">
                        <label class="label">Tution Status</label>
                        <div class="control">
                          <div class="select is-fullwidth">
                            <select
                              v-model="tution.is_active"
                              :disabled="tution_update_mode == false"
                              required
                            >
                              <option value="true">Active</option>
                              <option value="false">Disabled</option>
                            </select>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="column is-full">
                  <div class="columns is-multiline is-mobile">
                    <div class="column is-4">
                      <b>Area</b>: {{ tution.area }}
                    </div>
                    <div class="column is-4">
                      <b>Subject</b>: {{ tution.category.name }}
                    </div>
                    <div class="column is-4">
                      <b>Batch Size</b>: {{ tution.batch_size }}
                    </div>
                  </div>
                </div>
                <div class="column is-full">
                  <button
                    v-if="tution_update_mode == false"
                    type="button"
                    class="button is-danger is-outlined"
                    v-bind:class="{ is_loading: is_loading }"
                    v-on:click.prevent="ToggleUpdateMode(true)"
                  >
                    Edit
                  </button>
                  <button
                    v-if="tution_update_mode == true"
                    type="submit"
                    class="button is-link is-outlined"
                    v-bind:class="{ is_loading: is_loading }"
                    v-on:submit.prevent="update_tution"
                  >
                    Update
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
      <button
        class="modal-close is-large"
        aria-label="close"
        v-on:click="HideQuickView"
      ></button>
    </div>

    <div
      class="modal"
      v-if="applications.length > 0"
      v-bind:class="{ 'is-active': quickview != false }"
    >
      <div class="modal-background"></div>
      <div class="modal-content">
        <div class="card box is-paddingless is-small">
          <div class="card-content">
            <h1 class="title has-text-centered is-5">
              Tution Applications -
              <span class="tag is-rounded is-info">{{
                applications.length
              }}</span>
            </h1>
            <div
              class="notification applicant_box"
              v-for="a in applications"
              :key="a.id"
            >
              <p><b>Name</b>: {{ a.student.user_profile.name }}</p>
              <p>
                <b>Gender</b>:
                <span v-if="a.student.user_profile.gender == 1">Male</span>
                <span v-if="a.student.user_profile.gender == 2">Female</span>
                <span v-if="a.student.user_profile.gender == 3">Other</span>
              </p>
              <p><b>Phone</b>: {{ a.phone }}</p>
              <p><b>Locality</b>: {{ a.address }}</p>
            </div>
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
export default {
  name: 'TutionManageForm',
  data: function() {
    return {
      tution_list: [],
      quickview: false,
      tution: null,
      applications: [],
      tution_update_mode: false,
      is_loading: false
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
    ToggleUpdateMode: function(mode) {
      this.tution_update_mode = mode
    },
    SetApplicationsState: function(applications) {
      this.applications = applications
      this.quickview = true
    },
    HideQuickView: function() {
      this.quickview = false
      this.tution = null
      this.applications = []
    },
    get_request_list: function() {
      axios
        .get(this.get_endpoint(this.endpoints.tution_list), this.get_headers())
        .then(
          response => {
            // console.log(response)
            this.tution_list = response.data.data
          },
          () => {
            // console.log(err)
          }
        )
    },
    update_tution: function() {
      if (this.tution != null) {
        this.is_loading = true
        axios
          .post(
            this.get_endpoint(this.endpoints.tution_update),
            {
              id: this.tution.id,
              price: this.tution.price,
              title: this.tution.title,
              description: this.tution.description,
              timing: this.tution.timing,
              location: this.tution.location,
              is_active: this.tution.is_active
            },
            this.get_headers()
          )
          .then(
            () => {
              this.HideQuickView()
              this.get_request_list()
              this.is_loading = false
              this.tution_update_mode = false
            },
            () => {
              this.is_loading = false
            }
          )
      }
    }
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>

<style>
.applicant_box {
  border: 1px solid cadetblue;
}
</style>
