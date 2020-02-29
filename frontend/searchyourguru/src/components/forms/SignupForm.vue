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
          class="step-item is-link"
          v-bind:class="{
            'is-active': signup_step == 3,
            'is-completed': signup_step >= 4
          }"
        >
          <div class="step-marker">3</div>
        </li>
      </ul>
    </div>
    <hr />
    <article class="message is-link" v-if="verification_email != null">
      <div class="message-body">
        <p>
          Hii <b>{{ verification_email }}</b
          >,
        </p>
        <p>
          We have sent an email verification link to your inbox, kindly open it
          to activate your account.
        </p>
        <p>If not received within 60 seconds, click on button below</p>
        <hr />
        <router-link class="button is-link is-outlined" to="/verification/"
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
      <h1 class="title is-4 has-text-centered">Signup</h1>
      <div class="columns is-multiline">
        <div class="column is-full" v-if="signup_step == 1">
          <div class="columns is-multiline">
            <div class="column is-6">
              <h1 class="title is-6">I want to grow my business</h1>
              <p class="subtitle is-6">
                Respond to student requests and get hired
              </p>
              <button
                type="button"
                v-on:click="set_user_mode(4)"
                class="button is-link is-outlined"
              >
                Register as tutor
              </button>
            </div>
            <div class="column is-6">
              <h1 class="title is-6">I need tutoring</h1>
              <p class="subtitle is-6">
                Get introduced to affordable tutors & reserve a class
              </p>
              <button
                type="button"
                v-on:click="set_user_mode(3)"
                class="button is-link is-outlined"
              >
                Register as student
              </button>
            </div>
          </div>
        </div>

        <div class="column is-full" v-if="signup_step == 2">
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
                    <label class="label">Email</label>
                    <p class="control">
                      <input
                        v-model="signup_email"
                        class="input"
                        type="email"
                        placeholder="eg: hello@gmail.com"
                        :disabled="is_signup_loading"
                        required
                      />
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
                    <p class="control">
                      <input
                        v-model="signup_password"
                        class="input"
                        type="password"
                        placeholder="Password"
                        :disabled="is_signup_loading"
                        required
                      />
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
                    <p class="control">
                      <input
                        v-model="signup_confirm_password"
                        class="input"
                        type="password"
                        placeholder="Confirm Password"
                        :disabled="is_signup_loading"
                        required
                      />
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
      signup_user_name: null,
      signup_email: null,
      signup_password: null,
      signup_confirm_password: null,
      is_signup_loading: false,
      signup_user_name_error: null,
      signup_email_error: null,
      signup_password_error: null,
      errors: null,
      verification_email: null
    }
  },
  methods: {
    set_user_mode: function(user_type) {
      this.signup_user_type = user_type
      this.signup_step = 2
    },
    signup: function() {
      this.signup_user_name_error = null
      this.signup_email_error = null
      this.signup_password_error = null
      this.errors = null
      this.verification_email = null

      if (this.signup_step == 2) {
        if (this.signup_user_name == null || this.signup_user_name == '') {
          this.signup_user_name_error = 'This field is required'
        } else if (this.validEmail(this.signup_email) == false) {
          this.signup_email_error = 'Please enter a valid email'
        } else if (
          this.signup_password == null ||
          this.signup_confirm_password == null
        ) {
          this.signup_password_error =
            'Please fill in the password and confirm_password both'
        } else if (this.signup_password !== this.signup_confirm_password) {
          this.signup_password_error = 'Passwords didnot match'
        } else {
          this.is_signup_loading = true
          let data = {
            name: this.signup_user_name,
            email: this.signup_email,
            password: this.signup_password,
            confirm_password: this.signup_confirm_password,
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
                this.signup_step = 3
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
