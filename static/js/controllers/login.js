var main_app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#login_app',
  data: {
    login_endpoint: "/account/auth/login/",
    login_email: "",
    login_password: "",
    login_error_message: null,
    login_email_error: false,
    login_password_error: false,
    is_login_loading: false,
  },
  methods: {
    login: function(event) {
      this.login_email_error = false;
      this.login_password_error = false;
      if (validateEmail(this.login_email) == false) {
        this.login_email_error = true;
      } else if (this.login_password == "") {
        this.login_password_error = true;
      } else {
        this.login_error_message = null;
        this.is_login_loading = true;
        axios.post(this.login_endpoint, {
            email: this.login_email,
            password: this.login_password
          })
          .then((response) => {
            this.is_login_loading = false;
            window.location = "/";
          }, (error) => {
            let response =error.response.data.status[0];
            if(response == "doesnotexist"){
              this.login_error_message="No active account found with the given credentials";
            }
            if(response == 'inactive'){
              window.location = '/verification/?source=login&verification_email='+this.login_email
            }
            this.is_login_loading = false;
          });
      }
    },
  }
});
