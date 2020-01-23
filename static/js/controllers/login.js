var main_app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#login_app',
  data: {
    login_endpoint: "/account/auth/login/",
    account_activation_endpoint: "/account/auth/account-activation-link/",
    login_email: null,
    login_password: null,
    invalid_login: false,
    login_error_message: null,
    is_login_loading: false,
    account_activation_required:false,
    account_activation_required_message:null,
  },
  methods: {
    login: function(event) {
      if (validateEmail(this.login_email) == false) {
        this.login_error_message = "Please enter a valid email"
      } else if (this.login_password == "") {
        this.login_error_message = "Please fill in the password"
      } else {
        this.invalid_login = null;
        this.login_error_message = null;
        this.is_login_loading = true;
        axios.post(this.login_endpoint, {
            email: this.login_email,
            password: this.login_password
          })
          .then((response) => {
            // localStorage.setItem('user-token', response.data.access);
            // localStorage.setItem('user-token-refresh', response.data.refresh);
            // localStorage.setItem('user-is-authenticated', true);
            this.is_login_loading = false;
            window.location = "/";
          }, (error) => {
            console.log(error.response);
            this.login_error_message=error.response.data.status[0];
            if(this.login_error_message == 'inactive'){
              this.account_activation_required=true;
              this.account_activation_required_message="Hii "+this.login_email+", your account has not been activated yet. Click on button below to get an verification email. After that open your inbox and click on the verification link or open it by copying or pasting in your browser to activate the account";
            }
            if(this.login_error_message=="doesnotexist"){
              this.login_error_message="No active account found with the given credentials";
            }
            this.is_login_loading = false;
          });
      }
    },
    resend_verification_email: function(event){
      this.is_login_loading = true;
      axios.post(this.account_activation_endpoint, {
          email: this.login_email
        })
        .then((response) => {
          this.is_login_loading = false;
          this.account_activation_required_message = "Verification mail has been sent. If not received try again after 60 seconds."
        }, (error) => {
          console.log(error.response);
          this.is_login_loading = false;
        });
    },
  }
});
