<template>
  <div>
    <div>
      <ul class="steps">
        <li
          class="step-item is-success"
          v-bind:class="{
            'is-active': signup_step == 1,
            'is-completed': signup_step >= 2
          }"
        >
          <div class="step-marker">1</div>
        </li>
        <li
          class="step-item is-info"
          v-bind:class="{
            'is-active': signup_step == 2,
            'is-completed': signup_step >= 3
          }"
        >
          <div class="step-marker">2</div>
        </li>
        <li
          class="step-item is-warning"
          v-bind:class="{
            'is-active': signup_step == 3,
            'is-completed': signup_step >= 4
          }"
        >
          <div class="step-marker">3</div>
        </li>
        <li
          class="step-item is-link"
          v-bind:class="{
            'is-active': signup_step == 4,
            'is-completed': signup_step >= 5
          }"
        >
          <div class="step-marker">4</div>
        </li>
        <li
          class="step-item is-danger"
          v-bind:class="{
            'is-active': signup_step == 5,
            'is-completed': signup_step >= 6
          }"
        >
          <div class="step-marker">5</div>
        </li>
      </ul>
    </div>
    <article class="message is-success" v-if="verification_email != null">
      <div class="message-body">
        <p>Hii {{ verification_email }},</p>
        <p>
          We have sent an email verification link to your inbox, kindly open it
          to activate your account.
        </p>
        <p>If not received within 60 seconds, click on button below</p>
        <hr />
        <router-link class="button is-info" to="/verification/"
          >Verify Account</router-link
        >
      </div>
    </article>
    <hr />
    <form
      action="#"
      v-on:submit.prevent="signup"
      method="POST"
      v-if="verification_email == null"
    >
      <div class="columns is-multiline">
        <!-- Step 1 -->
        <div class="column is-full" v-if="signup_step == 1">
          <h1 class="title is-4 has-text-centered">Signup</h1>
          <div class="">
            <div class="columns is-multiline">
              <div class="column is-7">
                <h1 class="title is-6">I want to grow my business</h1>
                <p class="subtitle is-6">
                  Respond to student requests and get hired
                </p>
              </div>
              <div class="column is-5">
                <button
                  type="button"
                  v-on:click="set_user_mode(4)"
                  class="button is-success"
                >
                  Register as tutor
                </button>
              </div>
            </div>
          </div>
          <hr />
          <div class="">
            <div class="columns is-multiline">
              <div class="column is-7">
                <h1 class="title is-6">I need tutoring</h1>
                <p class="subtitle is-6">
                  Get introduced to affordable tutors
                </p>
              </div>
              <div class="column is-5">
                <button
                  type="button"
                  v-on:click="set_user_mode(3)"
                  class="button is-success"
                >
                  Register as student
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Step 2 -->
        <div class="column is-full" v-if="signup_step == 2">
          <h1 class="title is-5 has-text-centered" v-if="signup_user_type == 4">
            What do you teach?
          </h1>
          <h1 class="title is-5 has-text-centered" v-if="signup_user_type == 3">
            What do you want to study?
          </h1>
          <p class="subtitle is-6 has-text-centered">
            You can edit these later if you'd like.
          </p>
          <hr />
          <p class="help is-danger" v-if="signup_user_subjects_error != null">
            {{ signup_user_subjects_error }}
          </p>
          <div v-if="selected_subjects.length > 0">
            <h1 class="subtitle is-6">You have selected</h1>
            <div class="tags">
              <span v-for="s in selected_subjects" :key="s" class="tag is-light"
                >{{ s
                }}<button
                  type="button"
                  v-on:click="remove_selected_code(s)"
                  class="delete is-small"
                ></button
              ></span>
            </div>
            <hr />
          </div>
          <div id="tabs-with-content">
            <h1 class="title is-6">Subjects</h1>
            <div class="columns is-multiline is-mobile">
              <div
                class="column is-3"
                v-for="s in subjects"
                :key="s.subject.code"
              >
                <button
                  type="button"
                  class="button is-small is-info"
                  v-on:click="show_subject_dialog(s)"
                >
                  {{ s.subject.name }}
                </button>
              </div>
            </div>
          </div>
          <hr />
          <button v-on:submit="signup" class="button is-success">
            Next
          </button>
        </div>

        <!-- Step 3 -->
        <div class="column is-full" v-if="signup_step == 3">
          <div class="columns is-multiline">
            <div class="column is-full">
              <h1
                class="title is-5 has-text-centered"
                v-if="signup_user_type == 4"
              >
                Where do you prefer teaching your students?
              </h1>
              <h1
                class="title is-5 has-text-centered"
                v-if="signup_user_type == 3"
              >
                Where do you prefer studying?
              </h1>
              <h1 class="title is-6"></h1>
              <div class="field">
                <div class="control">
                  <label class="checkbox">
                    <input
                      type="checkbox"
                      :value="2"
                      v-model="location_preferences"
                      :disabled="is_signup_loading"
                    />
                    <span> At Student's Home</span>
                  </label>
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <label class="checkbox">
                    <input
                      type="checkbox"
                      :value="1"
                      v-model="location_preferences"
                      :disabled="is_signup_loading"
                    />
                    <span> At Tutors Home</span>
                  </label>
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <label class="checkbox">
                    <input
                      type="checkbox"
                      :value="3"
                      v-model="location_preferences"
                      :disabled="is_signup_loading"
                    />
                    At Institute
                  </label>
                </div>
              </div>
              <p
                class="help is-danger"
                v-if="signup_location_preference_error != null"
              >
                {{ signup_location_preference_error }}
              </p>
            </div>
            <div class="column is-full">
              <div class="columns is-multiline">
                <div class="column is-4">
                  <div class="field">
                    <label class="label">Pincode/Zipcode</label>
                    <div class="control">
                      <input
                        v-model="signup_user_zipcode"
                        class="input"
                        type="number"
                        placeholder="eg: 110092"
                        :disabled="is_signup_loading"
                        required
                      />
                    </div>
                  </div>
                  <p
                    class="help is-danger"
                    v-if="signup_user_zipcode_error != null"
                  >
                    {{ signup_user_zipcode_error }}
                  </p>
                </div>
              </div>
            </div>
          </div>
          <button v-on:submit="signup" class="button is-success">
            Next
          </button>
        </div>

        <!-- Step 4 -->
        <div class="column is-full" v-if="signup_step == 4">
          <h1 class="title is-4 has-text-centered">Personal Information</h1>
          <div class="columns is-multiline">
            <div class="column is-full">
              <div class="columns is-multiline">
                <div class="column is-6">
                  <div class="field">
                    <label class="label">Name</label>
                    <p class="control">
                      <input
                        v-model="signup_user_name"
                        class="input"
                        type="text"
                        placeholder="eg: Alex Williams"
                        :disabled="is_signup_loading"
                        required
                      />
                    </p>
                    <p
                      class="help is-danger"
                      v-if="signup_user_name_error != null"
                    >
                      {{ signup_user_name_error }}
                    </p>
                  </div>
                </div>
                <div class="column is-6">
                  <div class="field">
                    <label class="label">Preferred Timings</label>
                    <div class="control">
                      <div class="select is-fullwidth">
                        <select
                          v-model="signup_user_timing"
                          :disabled="is_signup_loading"
                          required
                        >
                          <option value="2">Morning</option>
                          <option value="3">Afternoon</option>
                          <option value="4">Evening</option>
                          <option value="1">Anytime (7 AM - 7 PM)</option>
                        </select>
                      </div>
                    </div>
                    <p
                      class="help is-danger"
                      v-if="signup_user_timing_error != null"
                    >
                      {{ signup_user_timing_error }}
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <div class="column is-full">
              <div class="columns is-multiline">
                <div class="column is-6">
                  <div class="field">
                    <label class="label">Gender</label>
                    <div class="control">
                      <div class="select is-fullwidth">
                        <select
                          v-model="signup_user_gender"
                          :disabled="is_signup_loading"
                          required
                        >
                          <option value="1">Male</option>
                          <option value="2">Female</option>
                          <option value="3">Other</option>
                        </select>
                      </div>
                    </div>
                    <p
                      class="help is-danger"
                      v-if="signup_user_gender_error != null"
                    >
                      {{ signup_user_gender_error }}
                    </p>
                  </div>
                </div>
                <div class="column is-6">
                  <div class="field">
                    <label class="label">Date Of Birth</label>
                    <div class="control">
                      <input
                        type="date"
                        class="input"
                        v-model="signup_user_dob"
                        :disabled="is_signup_loading"
                        required
                      />
                    </div>
                    <p
                      class="help is-danger"
                      v-if="signup_user_dob_error != null"
                    >
                      {{ signup_user_dob_error }}
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <div class="column is-full" v-if="signup_user_type == 4">
              <div class="columns is-multiline">
                <div class="column is-6">
                  <div class="field">
                    <label class="label">Experience (Years)</label>
                    <div class="control">
                      <input
                        type="number"
                        class="input"
                        v-model="experience"
                        :disabled="is_signup_loading"
                        required
                      />
                    </div>
                    <p class="help is-danger" v-if="experience_error != null">
                      {{ experience_error }}
                    </p>
                  </div>
                </div>
                <div class="column is-6">
                  <div class="field">
                    <label class="label">Hourly Price</label>
                    <div class="control">
                      <input
                        type="number"
                        class="input"
                        v-model="price"
                        :disabled="is_signup_loading"
                        required
                      />
                    </div>
                    <p class="help is-danger" v-if="price_error != null">
                      {{ price_error }}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <button v-on:submit="signup" class="button is-success">
            Next
          </button>
        </div>

        <!-- Step 4 -->
        <div class="column is-full" v-if="signup_step == 5">
          <h1 class="title is-5 has-text-centered">Final Step</h1>
          <div class="columns is-multiline">
            <div class="column is-full">
              <div class="columns is-multiline">
                <div class="column is-6">
                  <div class="field">
                    <label class="label">Phone</label>
                    <p class="control has-icons-left has-icons-right">
                      <input
                        v-model="signup_user_phone"
                        class="input"
                        type="number"
                        placeholder="eg: 92*** (Without +91)"
                        :disabled="is_signup_loading"
                        required
                      />
                      <span class="icon is-small is-left">
                        <i class="fas fa-envelope"></i>
                      </span>
                      <span class="icon is-small is-right">
                        <i class="fas fa-check"></i>
                      </span>
                    </p>
                    <p
                      class="help is-danger"
                      v-if="signup_user_phone_error != null"
                    >
                      {{ signup_user_phone_error }}
                    </p>
                  </div>
                </div>

                <div class="column is-6">
                  <div class="field">
                    <label class="label">Email</label>
                    <p class="control has-icons-left has-icons-right">
                      <input
                        v-model="signup_email"
                        class="input"
                        type="email"
                        placeholder="eg: hello@gmail.com"
                        :disabled="is_signup_loading"
                        required
                      />
                      <span class="icon is-small is-left">
                        <i class="fas fa-envelope"></i>
                      </span>
                      <span class="icon is-small is-right">
                        <i class="fas fa-check"></i>
                      </span>
                    </p>
                    <p class="help is-danger" v-if="signup_email_error != null">
                      {{ signup_email_error }}
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <div class="column is-full">
              <div class="columns is-multiline">
                <div class="column is-6">
                  <div class="field">
                    <label class="label">Password</label>
                    <p class="control has-icons-left">
                      <input
                        v-model="signup_password"
                        class="input"
                        type="password"
                        placeholder="Password"
                        :disabled="is_signup_loading"
                        required
                      />
                      <span class="icon is-small is-left">
                        <i class="fas fa-lock"></i>
                      </span>
                    </p>
                    <p
                      class="help is-danger"
                      v-if="signup_password_error != null"
                    >
                      {{ signup_password_error }}
                    </p>
                  </div>
                </div>
                <div class="column is-6">
                  <div class="field">
                    <label class="label">Confirm Password</label>
                    <p class="control has-icons-left">
                      <input
                        v-model="signup_confirm_password"
                        class="input"
                        type="password"
                        placeholder="Confirm Password"
                        :disabled="is_signup_loading"
                        required
                      />
                      <span class="icon is-small is-left">
                        <i class="fas fa-lock"></i>
                      </span>
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <div class="column is-full">
              <div class="field">
                <div class="control">
                  <label class="checkbox">
                    <input
                      type="checkbox"
                      :disabled="is_signup_loading"
                      required
                    />
                    I agree to the
                    <a href="#">terms and conditions</a>
                  </label>
                </div>
              </div>
            </div>
          </div>
          <button
            v-on:submit="signup"
            class="button is-success"
            v-bind:class="{ 'is-loading': is_signup_loading }"
          >
            Submit
          </button>
        </div>
      </div>
    </form>

    <!-- Modal for subjects dialog -->
    <div class="modal" v-bind:class="{ 'is-active': isActiveSubjectDialog }">
      <div class="modal-background"></div>
      <div class="modal-content">
        <div class="card box">
          <div>
            <ul v-for="t in subject_based_topics" :key="t.child.code">
              <li>
                <label class="checkbox">
                  <input
                    type="checkbox"
                    :id="t.child.code"
                    :value="t.child.code"
                    v-model="selected_subjects"
                    :disabled="is_signup_loading"
                  />
                  {{ t.child.name }}
                </label>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <button
        class="modal-close is-large"
        aria-label="close"
        v-on:click="hide_subject_dialog"
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
  name: 'SignupForm',
  data: function() {
    return {
      signup_step: 1,
      signup_btn_text: 'Next',
      signup_user_type: null,
      signup_user_zipcode: null,
      location_preferences: [],
      signup_user_name: null,
      signup_user_dob: null,
      signup_user_gender: null,
      signup_user_phone: null,
      signup_email: null,
      signup_password: null,
      signup_confirm_password: null,
      is_signup_loading: false,
      signup_user_zipcode_error: null,
      signup_location_preference_error: null,
      signup_user_type_error: null,
      signup_user_name_error: null,
      signup_user_dob_error: null,
      signup_user_gender_error: null,
      signup_user_phone_error: null,
      signup_email_error: null,
      signup_password_error: null,
      errors: null,
      verification_email: null,
      subjects: null,
      selected_subjects: [],
      isActiveSubjectDialog: false,
      subject_based_topics: null,
      signup_user_subjects_error: null,
      signup_user_timing: null,
      experience: null,
      experience_error: null,
      price: null,
      price_error: null
    }
  },
  methods: {
    set_user_mode: function(user_type) {
      this.signup_user_type = user_type
      this.signup_step = 2
    },
    get_subjects: function() {
      axios
        .get(this.get_endpoint(this.endpoints.subjects), this.guest_headers())
        .then(
          response => {
            this.subjects = response.data.data
          },
          err => {
            console.log('err', err.response)
          }
        )
    },
    show_subject_dialog: function(subject) {
      this.subject_based_topics = subject.categories
      this.isActiveSubjectDialog = true
      this.signup_user_subjects_error = null
    },
    hide_subject_dialog: function() {
      this.isActiveSubjectDialog = false
      this.signup_user_subjects_error = null
    },
    remove_selected_code: function(code) {
      this.selected_subjects = this.selected_subjects.filter(elem => {
        return elem !== code
      })
    },
    signup: function() {
      this.signup_user_type_error = null
      this.signup_user_name_error = null
      this.signup_user_dob_error = null
      this.signup_user_gender_error = null
      this.signup_user_phone_error = null
      this.signup_email_error = null
      this.signup_password_error = null
      this.errors = null
      this.verification_email = null
      this.signup_user_subjects_error = null
      this.signup_user_zipcode_error = null
      this.signup_location_preference_error = null
      this.signup_user_timing_error = null
      this.price_error = null
      this.experience_error = null

      if (this.signup_step == 2) {
        if (this.selected_subjects.length < 1) {
          this.signup_user_subjects_error =
            'Please select atleast one subject topic'
        } else {
          this.signup_step = 3
        }
      } else if (this.signup_step == 3) {
        if (this.location_preferences.length < 1) {
          this.signup_location_preference_error = 'Select atleast one choice'
        } else if (
          this.signup_user_zipcode == null ||
          this.signup_user_zipcode == ''
        ) {
          this.signup_user_zipcode_error = 'Please enter a valid zipcode'
        } else {
            let data = {
                zipcode: this.signup_user_zipcode
            }
            axios.post(
                this.get_endpoint(this.endpoints.zipcode_check),
                data,
                this.guest_headers()
             ).then(response => {
             console.log(response.data)
             this.signup_step = 4
            }, err => {console.log(err)})
        }
      } else if (this.signup_step == 4) {
        if (this.signup_user_name == null || this.signup_user_name == '') {
          this.signup_user_name_error = 'This field is required'
        } else if (this.signup_user_timing == null) {
          this.signup_user_timing_error = 'Please select a valid timing'
        } else if (
          this.signup_user_gender == null ||
          this.signup_user_gender == ''
        ) {
          this.signup_user_gender_error = 'This field is required'
        } else if (this.signup_user_dob == null || this.signup_user_dob == '') {
          this.signup_user_dob_error = 'This field is required'
        } else if (
          (this.experience == null || this.experience == '') &&
          this.user_type == 4
        ) {
          this.experience_error = 'Please enter a valid experience'
        } else if (
          (this.price == null || this.price == '') &&
          this.user_type == 3
        ) {
          this.price_error = 'Please enter a valid price'
        } else {
          this.signup_step = 5
        }
      } else if (this.signup_step == 5) {
        if (this.signup_user_phone == null) {
          this.signup_user_phone_error = 'This field is required'
        } else if (this.signup_user_phone.toString().length != 10) {
          this.signup_user_phone_error = 'Phone number should be of 10 digits'
        } else if (this.validEmail(this.signup_email) == false) {
          this.signup_email_error = 'Please enter a valid email'
        } else if (
          this.signup_password == null ||
          this.signup_confirm_password == null
        ) {
          this.signup_password_error =
            'Please fill in the password and confirm_password both'
        } else {
          this.is_signup_loading = true
          let data = {
            name: this.signup_user_name,
            email: this.signup_email,
            password: this.signup_password,
            confirm_password: this.signup_confirm_password,
            phone: this.signup_user_phone,
            user_type: this.signup_user_type,
            subjects: this.selected_subjects,
            gender: this.signup_user_gender,
            timing: this.signup_user_timing,
            location_preferences: this.location_preferences,
            zipcode: this.signup_user_zipcode,
            dob: this.signup_user_dob,
            experience: this.experience,
            price_per_hour: this.price
          }
          axios
            .post(
              this.get_endpoint(this.endpoints.signup),
              data,
              this.guest_headers()
            )
            .then(
              response => {
                this.signup_step = 6
                this.is_signup_loading = false
                this.verification_email = response.data.email
              },
              error => {
                this.errors = error.response.data.errors
                this.is_signup_loading = false

                if (this.errors.name) {
                  this.signup_user_name_error = this.errors.name[0]
                }

                if (this.errors.email) {
                  this.signup_email_error = this.errors.email[0]
                }

                if (this.errors.phone) {
                  this.signup_user_phone_error = this.errors.phone[0]
                }

                if (this.errors.password) {
                  this.signup_password_error = this.errors.password[0]
                }

                if (this.errors.user_type) {
                  this.signup_user_type_error = this.errors.user_type[0]
                }
              }
            )
        }
      }
    }
  },
  mounted: function() {
    this.get_subjects()
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>

<style>
@-webkit-keyframes spinAround {
  from {
    -webkit-transform: rotate(0);
    transform: rotate(0);
  }
  to {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes spinAround {
  from {
    -webkit-transform: rotate(0);
    transform: rotate(0);
  }
  to {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.steps:not(:last-child) {
  margin-bottom: 1.5rem;
}
.steps {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  font-size: 1rem;
  min-height: 2rem;
}
.steps .step-item {
  margin-top: 0;
  position: relative;
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  -ms-flex-preferred-size: 0;
  flex-basis: 0;
}
.steps .step-item:not(:first-child) {
  -ms-flex-preferred-size: 1em;
  flex-basis: 1em;
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  -ms-flex-negative: 1;
  flex-shrink: 1;
}
.steps .step-item:not(:first-child)::before {
  content: ' ';
  display: block;
  position: absolute;
}
.steps .step-item::before {
  background: -webkit-gradient(
    linear,
    right top,
    left top,
    color-stop(50%, #dbdbdb),
    color-stop(50%, #00d1b2)
  );
  background: linear-gradient(to left, #dbdbdb 50%, #00d1b2 50%);
  background-size: 200% 100%;
  background-position: right bottom;
}
.steps .step-item::before .step-marker {
  color: #fff;
}
.steps .step-item.is-active::before {
  background-position: left bottom;
}
.steps .step-item.is-active .step-marker {
  background-color: #fff;
  border-color: #00d1b2;
  color: #00d1b2;
}
.steps .step-item.is-completed::before {
  background-position: left bottom;
}
.steps .step-item.is-completed .step-marker {
  color: #fff;
  background-color: #00d1b2;
}
.steps .step-item .step-marker {
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  border-radius: 50%;
  font-weight: 700;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  background: #b5b5b5;
  color: #fff;
  border: 0.2em solid #fff;
  z-index: 1;
}
.steps .step-item .step-details {
  text-align: center;
}
.steps .step-item.is-white::before {
  background: -webkit-gradient(
    linear,
    right top,
    left top,
    color-stop(50%, #dbdbdb),
    color-stop(50%, #fff)
  );
  background: linear-gradient(to left, #dbdbdb 50%, #fff 50%);
  background-size: 200% 100%;
  background-position: right bottom;
}
.steps .step-item.is-white.is-active::before {
  background-position: left bottom;
}
.steps .step-item.is-white.is-active .step-marker {
  background-color: #fff;
  border-color: #fff;
  color: #fff;
}
.steps .step-item.is-white.is-completed::before {
  background-position: left bottom;
}
.steps .step-item.is-white.is-completed .step-marker {
  color: #0a0a0a;
  background-color: #fff;
}
.steps .step-item.is-black::before {
  background: -webkit-gradient(
    linear,
    right top,
    left top,
    color-stop(50%, #dbdbdb),
    color-stop(50%, #0a0a0a)
  );
  background: linear-gradient(to left, #dbdbdb 50%, #0a0a0a 50%);
  background-size: 200% 100%;
  background-position: right bottom;
}
.steps .step-item.is-black.is-active::before {
  background-position: left bottom;
}
.steps .step-item.is-black.is-active .step-marker {
  background-color: #fff;
  border-color: #0a0a0a;
  color: #0a0a0a;
}
.steps .step-item.is-black.is-completed::before {
  background-position: left bottom;
}
.steps .step-item.is-black.is-completed .step-marker {
  color: #fff;
  background-color: #0a0a0a;
}
.steps .step-item.is-light::before {
  background: -webkit-gradient(
    linear,
    right top,
    left top,
    color-stop(50%, #dbdbdb),
    color-stop(50%, #f5f5f5)
  );
  background: linear-gradient(to left, #dbdbdb 50%, #f5f5f5 50%);
  background-size: 200% 100%;
  background-position: right bottom;
}
.steps .step-item.is-light.is-active::before {
  background-position: left bottom;
}
.steps .step-item.is-light.is-active .step-marker {
  background-color: #fff;
  border-color: #f5f5f5;
  color: #f5f5f5;
}
.steps .step-item.is-light.is-completed::before {
  background-position: left bottom;
}
.steps .step-item.is-light.is-completed .step-marker {
  color: #363636;
  background-color: #f5f5f5;
}
.steps .step-item.is-dark::before {
  background: -webkit-gradient(
    linear,
    right top,
    left top,
    color-stop(50%, #dbdbdb),
    color-stop(50%, #363636)
  );
  background: linear-gradient(to left, #dbdbdb 50%, #363636 50%);
  background-size: 200% 100%;
  background-position: right bottom;
}
.steps .step-item.is-dark.is-active::before {
  background-position: left bottom;
}
.steps .step-item.is-dark.is-active .step-marker {
  background-color: #fff;
  border-color: #363636;
  color: #363636;
}
.steps .step-item.is-dark.is-completed::before {
  background-position: left bottom;
}
.steps .step-item.is-dark.is-completed .step-marker {
  color: #f5f5f5;
  background-color: #363636;
}
.steps .step-item.is-primary::before {
  background: -webkit-gradient(
    linear,
    right top,
    left top,
    color-stop(50%, #dbdbdb),
    color-stop(50%, #00d1b2)
  );
  background: linear-gradient(to left, #dbdbdb 50%, #00d1b2 50%);
  background-size: 200% 100%;
  background-position: right bottom;
}
.steps .step-item.is-primary.is-active::before {
  background-position: left bottom;
}
.steps .step-item.is-primary.is-active .step-marker {
  background-color: #fff;
  border-color: #00d1b2;
  color: #00d1b2;
}
.steps .step-item.is-primary.is-completed::before {
  background-position: left bottom;
}
.steps .step-item.is-primary.is-completed .step-marker {
  color: #fff;
  background-color: #00d1b2;
}
.steps .step-item.is-link::before {
  background: -webkit-gradient(
    linear,
    right top,
    left top,
    color-stop(50%, #dbdbdb),
    color-stop(50%, #3273dc)
  );
  background: linear-gradient(to left, #dbdbdb 50%, #3273dc 50%);
  background-size: 200% 100%;
  background-position: right bottom;
}
.steps .step-item.is-link.is-active::before {
  background-position: left bottom;
}
.steps .step-item.is-link.is-active .step-marker {
  background-color: #fff;
  border-color: #3273dc;
  color: #3273dc;
}
.steps .step-item.is-link.is-completed::before {
  background-position: left bottom;
}
.steps .step-item.is-link.is-completed .step-marker {
  color: #fff;
  background-color: #3273dc;
}
.steps .step-item.is-info::before {
  background: -webkit-gradient(
    linear,
    right top,
    left top,
    color-stop(50%, #dbdbdb),
    color-stop(50%, #209cee)
  );
  background: linear-gradient(to left, #dbdbdb 50%, #209cee 50%);
  background-size: 200% 100%;
  background-position: right bottom;
}
.steps .step-item.is-info.is-active::before {
  background-position: left bottom;
}
.steps .step-item.is-info.is-active .step-marker {
  background-color: #fff;
  border-color: #209cee;
  color: #209cee;
}
.steps .step-item.is-info.is-completed::before {
  background-position: left bottom;
}
.steps .step-item.is-info.is-completed .step-marker {
  color: #fff;
  background-color: #209cee;
}
.steps .step-item.is-success::before {
  background: -webkit-gradient(
    linear,
    right top,
    left top,
    color-stop(50%, #dbdbdb),
    color-stop(50%, #23d160)
  );
  background: linear-gradient(to left, #dbdbdb 50%, #23d160 50%);
  background-size: 200% 100%;
  background-position: right bottom;
}
.steps .step-item.is-success.is-active::before {
  background-position: left bottom;
}
.steps .step-item.is-success.is-active .step-marker {
  background-color: #fff;
  border-color: #23d160;
  color: #23d160;
}
.steps .step-item.is-success.is-completed::before {
  background-position: left bottom;
}
.steps .step-item.is-success.is-completed .step-marker {
  color: #fff;
  background-color: #23d160;
}
.steps .step-item.is-warning::before {
  background: -webkit-gradient(
    linear,
    right top,
    left top,
    color-stop(50%, #dbdbdb),
    color-stop(50%, #ffdd57)
  );
  background: linear-gradient(to left, #dbdbdb 50%, #ffdd57 50%);
  background-size: 200% 100%;
  background-position: right bottom;
}
.steps .step-item.is-warning.is-active::before {
  background-position: left bottom;
}
.steps .step-item.is-warning.is-active .step-marker {
  background-color: #fff;
  border-color: #ffdd57;
  color: #ffdd57;
}
.steps .step-item.is-warning.is-completed::before {
  background-position: left bottom;
}
.steps .step-item.is-warning.is-completed .step-marker {
  color: rgba(0, 0, 0, 0.7);
  background-color: #ffdd57;
}
.steps .step-item.is-danger::before {
  background: -webkit-gradient(
    linear,
    right top,
    left top,
    color-stop(50%, #dbdbdb),
    color-stop(50%, #ff3860)
  );
  background: linear-gradient(to left, #dbdbdb 50%, #ff3860 50%);
  background-size: 200% 100%;
  background-position: right bottom;
}
.steps .step-item.is-danger.is-active::before {
  background-position: left bottom;
}
.steps .step-item.is-danger.is-active .step-marker {
  background-color: #fff;
  border-color: #ff3860;
  color: #ff3860;
}
.steps .step-item.is-danger.is-completed::before {
  background-position: left bottom;
}
.steps .step-item.is-danger.is-completed .step-marker {
  color: #fff;
  background-color: #ff3860;
}
.steps .steps-content {
  -webkit-box-align: stretch;
  -ms-flex-align: stretch;
  align-items: stretch;
  -ms-flex-preferred-size: 100%;
  flex-basis: 100%;
  margin: 2rem 0;
}
.steps .steps-content .step-content {
  display: none;
}
.steps .steps-content .step-content.is-active {
  display: block;
}
.steps .steps-actions {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: stretch;
  -ms-flex-align: stretch;
  align-items: stretch;
  -ms-flex-preferred-size: 100%;
  flex-basis: 100%;
}
.steps .steps-actions .steps-action {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-preferred-size: 0;
  flex-basis: 0;
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  margin: 0.5rem;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}
.steps.is-animated .step-item::before {
  -webkit-transition: all 2s ease;
  transition: all 2s ease;
}
.steps.is-animated .step-item .step-marker {
  -webkit-transition: all 0s ease;
  transition: all 0s ease;
  -webkit-transition-delay: 1.5s;
  transition-delay: 1.5s;
}
.steps .step-item:not(:first-child)::before {
  height: 0.2em;
  width: 100%;
  bottom: 0;
  left: -50%;
  top: 1rem;
}
.steps .step-item .step-marker {
  height: 2rem;
  width: 2rem;
  position: absolute;
  left: calc(50% - 1rem);
}
.steps .step-item .step-marker .icon * {
  font-size: 1rem;
}
.steps .step-item .step-details {
  margin-top: 2rem;
  margin-left: 0.5em;
  margin-right: 0.5em;
  padding-top: 0.2em;
}
.steps .step-item .step-details .step-title {
  font-size: 1.2rem;
  font-weight: 600;
}
.steps.is-small {
  font-size: 0.75rem;
  min-height: 1.5rem;
}
.steps.is-small .step-item:not(:first-child)::before {
  height: 0.2em;
  width: 100%;
  bottom: 0;
  left: -50%;
  top: 0.75rem;
}
.steps.is-small .step-item .step-marker {
  height: 1.5rem;
  width: 1.5rem;
  position: absolute;
  left: calc(50% - 0.75rem);
}
.steps.is-small .step-item .step-marker .icon * {
  font-size: 0.75rem;
}
.steps.is-small .step-item .step-details {
  margin-top: 1.5rem;
  margin-left: 0.5em;
  margin-right: 0.5em;
  padding-top: 0.2em;
}
.steps.is-small .step-item .step-details .step-title {
  font-size: 0.9rem;
  font-weight: 600;
}
.steps.is-medium {
  font-size: 1.25rem;
  min-height: 2.5rem;
}
.steps.is-medium .step-item:not(:first-child)::before {
  height: 0.2em;
  width: 100%;
  bottom: 0;
  left: -50%;
  top: 1.25rem;
}
.steps.is-medium .step-item .step-marker {
  height: 2.5rem;
  width: 2.5rem;
  position: absolute;
  left: calc(50% - 1.25rem);
}
.steps.is-medium .step-item .step-marker .icon * {
  font-size: 1.25rem;
}
.steps.is-medium .step-item .step-details {
  margin-top: 2.5rem;
  margin-left: 0.5em;
  margin-right: 0.5em;
  padding-top: 0.2em;
}
.steps.is-medium .step-item .step-details .step-title {
  font-size: 1.5rem;
  font-weight: 600;
}
.steps.is-large {
  font-size: 1.5rem;
  min-height: 3rem;
}
.steps.is-large .step-item:not(:first-child)::before {
  height: 0.2em;
  width: 100%;
  bottom: 0;
  left: -50%;
  top: 1.5rem;
}
.steps.is-large .step-item .step-marker {
  height: 3rem;
  width: 3rem;
  position: absolute;
  left: calc(50% - 1.5rem);
}
.steps.is-large .step-item .step-marker .icon * {
  font-size: 1.5rem;
}
.steps.is-large .step-item .step-details {
  margin-top: 3rem;
  margin-left: 0.5em;
  margin-right: 0.5em;
  padding-top: 0.2em;
}
.steps.is-large .step-item .step-details .step-title {
  font-size: 1.8rem;
  font-weight: 600;
}
</style>
