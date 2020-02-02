import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user: {},
    isAuthenticated: false
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
