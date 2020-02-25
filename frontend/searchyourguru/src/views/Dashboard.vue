<template>
  <div id="dashboard_app">
    <section class="section has-background-white">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-8">
            <h1 class="title is-5 has-text-centered">Manage</h1>
            <hr />
            <div class="columns is-multiline">
              <div class="column is-3">
                <a v-on:click.prevent.stop="set_app_state('general_settings')">
                  <figure class="image is-48x48">
                    <img src="@/assets/general_settings1.svg" alt="" />
                  </figure>
                  <p class="subtitle has-text-link">General</p>
                </a>
              </div>
              <div class="column is-3">
                <a v-on:click.prevent.stop="set_app_state('change_password')">
                  <figure class="image is-48x48">
                    <img src="@/assets/change_password.svg" alt="" />
                  </figure>
                  <p class="subtitle has-text-link">Change Password</p>
                </a>
              </div>
              <div class="column is-3" v-if="isUserTutor == true">
                <a v-on:click.prevent.stop="set_app_state('create_tution')">
                  <figure class="image is-48x48">
                    <img src="@/assets/create_tution.svg" alt="" />
                  </figure>
                  <p class="subtitle has-text-link">
                    New Tution <span class="has-text-danger">+</span>
                  </p>
                </a>
              </div>
              <div class="column is-3">
                <a v-on:click.prevent.stop="set_app_state('notification')">
                  <figure class="image is-48x48">
                    <img src="@/assets/notification1.svg" alt="" />
                  </figure>
                  <p class="subtitle has-text-link">Notifications</p>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section has-background-white">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-8">
            <h1 class="title is-5 has-text-centered">Your Tutions</h1>
            <TutionManageForm v-if="user_type == 'tutor'" />
            <TutionAppliedForm v-if="user_type == 'student'" />
          </div>
        </div>
      </div>
    </section>

    <div class="modal" v-bind:class="{ 'is-active': quickview != null }">
      <div class="modal-background"></div>
      <div class="modal-content">
        <div class="card box is-paddingless is-small">
          <div class="card-content">
            <UpdateProfileForm v-if="app_state == 'general_settings'" />
            <ChangePasswordForm v-if="app_state == 'change_password'" />
            <CreateTutionForm v-if="app_state == 'create_tution'" />
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
import UpdateProfileForm from '@/components/forms/UpdateProfileForm.vue'
import ChangePasswordForm from '@/components/forms/ChangePasswordForm.vue'
import CreateTutionForm from '@/components/forms/CreateTutionForm.vue'
import TutionManageForm from '@/components/forms/TutionManageForm.vue'
import TutionAppliedForm from '@/components/forms/TutionAppliedForm.vue'

export default {
  name: 'Dashboard',
  data: function() {
    return {
      app_state: 'general_settings',
      quickview: null
    }
  },
  methods: {
    set_app_state: function(state) {
      this.app_state = state
      this.quickview = state
    },
    HideQuickView: function() {
      this.app_state = null
      this.quickview = null
    }
  },
  computed: {
    isUserTutor() {
      return this.$store.getters.is_user_tutor
    },
    user_type() {
      return this.$store.getters.user_type
    }
  },
  components: {
    UpdateProfileForm,
    ChangePasswordForm,
    CreateTutionForm,
    TutionManageForm,
    TutionAppliedForm
  }
}
</script>

<style></style>
