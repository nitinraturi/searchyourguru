Vue.prototype.$appName = 'SearchYourGuru'
var main_app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#main_app',
  data: {
    // login_endpoint: "/account/auth/login/",
    logout_endpoint: "/account/auth/logout/",
    // login_email: null,
    // login_password: null,
    // invalid_login: false,
    // login_error_message: null,
    // is_login_loading: false,
    // errors: [],
  },
  methods: {
    // login: function(event) {
    //   if (validateEmail(this.login_email) == false) {
    //     this.login_error_message = "Please enter a valid email"
    //   } else if (this.login_password == "") {
    //     this.login_error_message = "Please fill in the password"
    //   } else {
    //     this.invalid_login = null;
    //     this.login_error_message = null;
    //     this.is_login_loading = true;
    //     axios.post(this.login_endpoint, {
    //         email: this.login_email,
    //         password: this.login_password
    //       })
    //       .then((response) => {
    //         // localStorage.setItem('user-token', response.data.access);
    //         // localStorage.setItem('user-token-refresh', response.data.refresh);
    //         // localStorage.setItem('user-is-authenticated', true);
    //         this.is_login_loading = false;
    //         window.location = "/";
    //       }, (error) => {
    //         console.log(error.response);
    //         this.login_error_message=error.response.data.detail[0];
    //         this.is_login_loading = false;
    //       });
    //   }
    // },
    logout: function(event) {
      axios.post(this.logout_endpoint, {})
      .then((response) => {
        window.location = "/";
      }, (error) => {
        console.log(error.response);
      });
    },
  }
});
