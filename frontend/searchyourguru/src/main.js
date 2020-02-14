import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bulma/css/bulma.css'

Vue.config.productionTip = false

const token = localStorage.getItem('guru-user-token')
var search_filters = localStorage.getItem('search_filters')
if (token) {
  // Vue.prototype.$http.defaults.headers.common['Authorization'] = token
  store.state.isAuthenticated = true
}

if (search_filters) {
  store.state.search_filters = JSON.parse(search_filters)
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
