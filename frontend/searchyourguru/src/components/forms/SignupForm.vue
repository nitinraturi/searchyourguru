<template>
  <div>
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

    <form
      action="#"
      v-on:submit.prevent="signup"
      method="POST"
      v-if="verification_email == null"
    >
      <div class="columns is-multiline">
        <div class="column is-full">
          <!-- User Type -->
          <div class="field is-horizontal">
            <div class="field-label">
              <label class="label">I am a ?</label>
            </div>
            <div class="field-body">
              <div class="field is-narrow">
                <div class="control">
                  <label class="radio">
                    <input
                      type="radio"
                      name="user_type"
                      v-model="signup_user_type"
                      value="3"
                      :disabled="is_signup_loading"
                      required
                    />
                    Student or Parent
                  </label>
                  <label class="radio">
                    <input
                      type="radio"
                      name="user_type"
                      v-model="signup_user_type"
                      value="4"
                      required
                    />
                    Tutor
                  </label>
                </div>
                <p class="help is-danger" v-if="signup_user_type_error != null">
                  {{ signup_user_type_error }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <div class="column is-full">
          <!-- Name -->
          <div class="field">
            <label class="label">Name</label>
            <p class="control has-icons-left has-icons-right">
              <input
                v-model="signup_user_name"
                class="input"
                type="text"
                placeholder="eg: Alex Williams"
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
            <p class="help is-danger" v-if="signup_user_name_error != null">
              {{ signup_user_name_error }}
            </p>
          </div>
        </div>

        <div class="column is-full">
          <div class="columns is-multiline">
            <div class="column is-6">
              <!-- Phone -->
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
              <!-- Email -->
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
            <div class="column is-4">
              <div class="field">
                <label class="label">Country</label>
                <div class="control">
                  <div class="select">
                    <select>
                      <option>India (+91)</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
            <div class="column is-4">
              <div class="field">
                <label class="label">State</label>
                <div class="control">
                  <div class="select">
                    <select>
                      <option>India (+91)</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
            <div class="column is-4">
              <div class="field">
                <label class="label">Pincode/Zipcode</label>
                <div class="control">
                  <input
                    class="input"
                    type="number"
                    placeholder="eg: 110092"
                    :disabled="is_signup_loading"
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
              <!-- Password -->
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
                <p class="help is-danger" v-if="signup_password_error != null">
                  {{ signup_password_error }}
                </p>
              </div>
            </div>
            <div class="column is-6">
              <!-- Confirm Password -->
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
                <input type="checkbox" :disabled="is_signup_loading" required />
                I agree to the
                <a href="#">terms and conditions</a>
              </label>
            </div>
          </div>
        </div>
      </div>

      <div class="column is-full">
        <div class="field">
          <p class="control">
            <button
              type="submit"
              v-on:submit="signup"
              class="button is-success"
              v-bind:class="{ 'is-loading': is_signup_loading }"
            >
              Create Account
            </button>
          </p>
        </div>
      </div>
    </form>
    <hr />
    <p>
      Already have an account,
      <router-link to="/login/">Login here</router-link>
    </p>
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
      signup_user_type: null,
      signup_user_name: null,
      signup_user_phone: null,
      signup_email: null,
      signup_password: null,
      signup_confirm_password: null,
      is_signup_loading: false,
      signup_user_type_error: null,
      signup_user_name_error: null,
      signup_user_phone_error: null,
      signup_email_error: null,
      signup_password_error: null,
      errors: null,
      verification_email: null
    }
  },
  methods: {
    signup: function() {
      this.signup_user_type_error = null
      this.signup_user_name_error = null
      this.signup_user_phone_error = null
      this.signup_email_error = null
      this.signup_password_error = null
      this.errors = null
      this.verification_email = null

      if (this.signup_user_type == null) {
        this.signup_user_type_error = 'This field is required'
      } else if (this.signup_user_name == null) {
        this.signup_user_name_error = 'This field is required'
      } else if (this.signup_user_phone == null) {
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
          user_type: this.signup_user_type
        }
        axios
          .post(
            this.get_endpoint(this.endpoints.signup),
            data,
            this.guest_headers()
          )
          .then(
            response => {
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
  },
  mixins: [ValidatorsMixin, EndpointsMixin, RequestMixin]
}
</script>

<style></style>
