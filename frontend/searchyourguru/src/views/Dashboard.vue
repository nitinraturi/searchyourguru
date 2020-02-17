<template>
  <div id="dashboard_app">
    <section class="section has-background-white">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-10">
            <div class="columns is-centered">
              <div class="column is-4">
                <aside class="menu">
                  <p class="menu-label">Account</p>
                  <ul class="menu-list">
                    <li>
                      <a
                        v-on:click.prevent.stop="
                          set_app_state('general_settings')
                        "
                        >General</a
                      >
                    </li>
                    <li>
                      <a
                        v-on:click.prevent.stop="
                          set_app_state('change_password')
                        "
                        >Change Password</a
                      >
                    </li>
                  </ul>
                  <p class="menu-label">Tution</p>
                  <ul class="menu-list">
                    <li>
                      <a
                        v-on:click.prevent.stop="set_app_state('create_tution')"
                        class="button is-link has-text-left is-outlined"
                        >Create Tution +</a
                      >
                    </li>
                    <li>
                      <a
                        v-on:click.prevent.stop="
                          set_app_state('tution_request')
                        "
                        >Tution Request</a
                      >
                    </li>
                  </ul>
                </aside>
              </div>
              <div class="column is-8">
                <div class="box" v-if="app_state == 'general_settings'">
                  <h1 class="title is-6">General Settings</h1>
                  <UpdateProfileForm />
                </div>
                <div class="box" v-if="app_state == 'change_password'">
                  <h1 class="title is-6">Change Password</h1>
                  <ChangePasswordForm />
                </div>
                <div class="box" v-if="app_state == 'create_tution'">
                  <h1 class="title is-6 has-text-centered has-text-link">
                    Create a Tution
                  </h1>
                  <CreateTutionForm />
                </div>
                <div class="box" v-if="app_state == 'tution_request'">
                  <h1 class="title is-6">Tution Request</h1>
                  <TutionRequestForm />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import UpdateProfileForm from '@/components/forms/UpdateProfileForm.vue'
import ChangePasswordForm from '@/components/forms/ChangePasswordForm.vue'
import TutionRequestForm from '@/components/forms/TutionRequestForm.vue'
import CreateTutionForm from '@/components/forms/CreateTutionForm.vue'

export default {
  name: 'Dashboard',
  data: function() {
    return {
      app_state: 'general_settings'
    }
  },
  methods: {
    set_app_state: function(state) {
      this.app_state = state
    }
  },
  components: {
    UpdateProfileForm,
    ChangePasswordForm,
    TutionRequestForm,
    CreateTutionForm
  }
}
</script>

<style></style>
