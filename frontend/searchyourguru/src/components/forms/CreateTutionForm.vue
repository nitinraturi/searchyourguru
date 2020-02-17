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
                  <input
                    type="text"
                    class="input"
                    v-model="tution.area"
                    :disabled="is_loading"
                    required
                    placeholder="eg: 110092 or Laxmi Nagar or Delhi"
                  />
                </div>
              </div>
            </div>
            <div class="column is-6">
              <div class="field">
                <label class="label">Subject</label>
                <div class="control">
                  <input
                    type="text"
                    class="input"
                    list="subjects_list"
                    v-on:keyup="subject_keyword_changed"
                    v-model="tution.subject"
                    placeholder="eg: Math or Physics"
                    :disabled="is_loading"
                    required
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
                <p class="control">
                  <input
                    v-model="tution.location"
                    class="input"
                    type="number"
                    placeholder="eg: Alex Williams"
                    :disabled="is_loading"
                    required
                  />
                </p>
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
                    :disabled="is_loading"
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
            v-bind:class="{ is_loading: is_loading }"
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
export default {
  name: 'TutionRequestForm',
  data: function() {
    return {
      tution: {
        title: null,
        description: null,
        subject: null,
        area: null,
        timing: null,
        location: null,
        batch_size: 1,
        price: 200
      },
      tution_created: false,
      is_loading: false,
      suggested_subjects: []
    }
  },
  methods: {
    subject_keyword_changed: function() {
      if (
        this.tution.subject != null &&
        this.tution.subject != '' &&
        this.tution.subject.length > 2
      ) {
        axios
          .post(
            this.get_endpoint(this.endpoints.suggested_subjects),
            { subject_keyword: this.tution.subject },
            this.guest_headers()
          )
          .then(
            response => {
              this.suggested_subjects = response.data.data
            },
            err => console.log(err)
          )
      }
    },
    create_tution: function() {
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
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>

<style></style>
