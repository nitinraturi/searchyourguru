<template>
  <div>
    <article class="message is-link" v-if="tution_created == true">
      <div class="message-body">
        <p>
          Your tution is created successfully.
        </p>
      </div>
    </article>
    <form
      action="#"
      method="POST"
      v-on:submit.prevent="create_tution"
      v-if="tution_created == false"
    >
      <div class="columns is-multiline">
        <div class="column is-full">
          <div class="field">
            <label class="label">Title</label>
            <div class="control">
              <input
                type="text"
                class="input"
                placeholder="Eg: Math Tution"
                v-model="tution.title"
                :disabled="is_loading"
                required
              />
            </div>
          </div>
        </div>
        <div class="column is-full">
          <div class="field">
            <label class="label">Description</label>
            <div class="control">
              <textarea
                class="textarea"
                v-model="tution.description"
                :disabled="is_loading"
                required
                placeholder="Describe your tution a little bit. Attractive descriptions are likely to get more requests."
              ></textarea>
            </div>
          </div>
        </div>
        <div class="column is-full">
          <div class="columns is-multiline">
            <div class="column is-6">
              <div class="field">
                <label class="label">City or Pincode</label>
                <div class="control">
                  <LocationFieldForm @location_changed="set_location_keyword" />
                </div>
                <p
                  v-if="location_keyword_error != null"
                  class="help is-small is-danger"
                >
                  {{ location_keyword_error }}
                </p>
              </div>
            </div>
            <div class="column is-6">
              <div class="field">
                <label class="label">Subject</label>
                <div class="control">
                  <CategoryFieldForm @category_changed="set_category" />
                </div>
                <p
                  class="help is-small is-danger"
                  v-if="tution_subject_error != null"
                >
                  {{ tution_subject_error }}
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-full">
          <div class="columns is-multiline">
            <div class="column is-6">
              <div class="field">
                <label class="label">Preferred Timings</label>
                <div class="control">
                  <div class="select is-fullwidth">
                    <select
                      v-model="tution.timing"
                      :disabled="is_loading"
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
                    :disabled="is_loading"
                    required
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-full">
          <div class="columns is-multiline">
            <div class="column is-6">
              <div class="field">
                <label class="label">Location Preference</label>
                <div class="control">
                  <div class="select is-fullwidth">
                    <select
                      v-model="tution.location"
                      :disabled="is_loading"
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
                <label class="label">Batch Size</label>
                <div class="control">
                  <input
                    type="number"
                    class="input"
                    v-model="tution.batch_size"
                    :disabled="true"
                    required
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-full">
          <button
            type="submit"
            class="button is-link is-outlined"
            v-bind:class="{ 'is-loading': is_loading }"
            v-on:submit.prevent="create_tution"
          >
            Create
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import ValidatorsMixin from '@/components/mixins/ValidatorsMixin.vue'
import EndpointsMixin from '@/components/mixins/EndpointsMixin.vue'
import RequestMixin from '@/components/mixins/RequestMixin'
import LocationFieldForm from '@/components/forms/LocationFieldForm.vue'
import CategoryFieldForm from '@/components/forms/CategoryFieldForm.vue'

export default {
  name: 'CreateTutionForm',
  data: function() {
    return {
      tution: {
        title: null,
        description: null,
        area: null,
        category: null,
        timing: null,
        location: null,
        batch_size: 1,
        price: 200
      },
      tution_created: false,
      is_loading: false,
      tution_subject_error: null,
      location_keyword_error: null,
      suggested_subjects: [],
      suggested_cities: []
    }
  },
  components: {
    LocationFieldForm,
    CategoryFieldForm
  },
  methods: {
    set_location_keyword: function(value) {
      this.tution.area = value
    },
    set_category: function(value) {
      this.tution.category = value
    },
    create_tution: function() {
      this.location_keyword_error = null
      this.tution_subject_error = null
      if (this.tution.area == null || this.tution.area == '') {
        this.location_keyword_error = 'This field is required'
      } else if (this.tution.category == null || this.tution.category == '') {
        this.tution_subject_error = 'This field is required'
      } else {
        this.is_loading = true
        axios
          .post(
            this.get_endpoint(this.endpoints.tution_create),
            this.tution,
            this.get_headers()
          )
          .then(
            () => {
              this.is_loading = false
              this.tution_created = true
            },
            () => {
              this.is_loading = false
              this.tution_created = false
            }
          )
      }
    }
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>

<style></style>
