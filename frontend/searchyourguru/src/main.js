import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bulma/css/bulma.css'

Vue.config.productionTip = false

const token = localStorage.getItem('guru-user-token')
if (token) {
  // Vue.prototype.$http.defaults.headers.common['Authorization'] = token
  store.state.isAuthenticated = true
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
