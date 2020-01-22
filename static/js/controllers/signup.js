var main_app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#signup_app',
  data: {
    signup_endpoint: "/account/auth/register/",
    signup_user_type: null,
    signup_user_name: null,
    signup_email: null,
    signup_user_phone: null,
    signup_password: null,
    signup_confirm_password: null,
    invalid_signup: false,
    signup_error_message: null,
    is_signup_loading: false,
    success_signup_message:null,
    errors: [],
  },
  methods: {
    signup: function(event) {
      if (validateEmail(this.signup_email) == false) {
        this.signup_error_message = "Please enter a valid email"
      } else if (this.signup_password == "") {
        this.signup_error_message = "Please fill in the password"
      } else {
        this.invalid_signup = null;
        this.signup_error_message = null;
        this.is_signup_loading = true;
        let data = {
            "name": this.signup_user_name,
            "email": this.signup_email,
            "password": this.signup_password,
            "confirm_password": this.signup_confirm_password,
            "phone": this.signup_user_phone,
            "user_type": this.signup_user_type
          };
        axios.post(this.signup_endpoint,data)
          .then((response) => {
            // localStorage.setItem('user-token', response.data.access);
            // localStorage.setItem('user-token-refresh', response.data.refresh);
            // localStorage.setItem('user-is-authenticated', true);
            this.is_signup_loading = false;
            // window.location = "/";
            this.success_signup_message = true;
          }, (error) => {
            console.log(error.response);
            this.signup_error_message = error.response.data;
            this.is_signup_loading = false;
          });
      }
    },
  }
});
