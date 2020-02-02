Vue.prototype.$appName = 'SearchYourGuru'
var main_app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#nav_app',
  data: {
    login_endpoint: "/account/auth/login/",
    logout_endpoint: "/account/auth/logout/",
    login_email: null,
    login_password: null,
    invalid_login: false,
    login_error_message: null,
    is_login_loading: false,
    errors: [],
  },
  methods: {
    logout: function(event) {
      axios.post(this.logout_endpoint, {})
      .then((response) => {
        localStorage.removeItem('user-token');
        localStorage.removeItem('user-token-refresh');
        localStorage.setItem('user-is-authenticated', false);
        window.location = "/";
      }, (error) => {
        console.log(error.response);
      });
    },
  }
});
