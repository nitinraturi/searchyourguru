import axios from 'axios'

const state = {
    get_user_profile: function() {
        let config = this.get_headers()
        axios.get(this.get_endpoint(this.endpoints.user_profile), config).then(
          response => {
            let res = response.data
            this.is_loading = false
            this.general_settings.user_name = res.name
            this.general_settings.user_email = res.email
            this.general_settings.user_phone = res.phone
          },
          () => {
            this.is_loading = false
          }
        )
      
}

const getters = {}

const actions = {}

const mutations = {}

export default {
  state,
  getters,
  actions,
  mutations
}
