import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user: {},
    isAuthenticated: false,
    search_filters: {
      location_keyword: '',
      category: '',
      experience: null,
      price_per_hour: null,
      qualification: null,
      timing: null,
      gender: null,
      location_preferences: []
    },
    filtered_users: []
  },
  getters: {
    is_loggedin: function(state) {
      return state.isAuthenticated
    }
  },
  mutations: {},
  actions: {},
  modules: {}
})
