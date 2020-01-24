var main_app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#password_reset_app',
  data: {
    password_reset_endpoint: "/account/auth/account-password-reset-link/",
    change_password_endpoint: "/account/auth/change-password/",
    reset_email: null,
    reset_email_error: false,
    new_password:null,
    new_password_error:null,
    confirm_new_password:null,
    confirm_new_password_error:null,
    is_loading: false,
    error_msg:null,
    verification_msg:null,
  },
  methods: {
    resend_reset_email: function(event){
      this.error_msg = null;
      this.verification_msg=null;
      this.reset_email_error=false;

      if (validateEmail(this.reset_email) == false) {
        this.reset_email_error = true;
      }else{
        this.is_loading = true;
        axios.post(this.password_reset_endpoint, {
          email: this.reset_email
        })
        .then((response) => {
          this.is_loading = false;
          this.verification_msg = "Password Reset mail has been sent. If not received try again after 60 seconds."
        }, (error) => {
          this.is_loading = false;
          this.error_msg = error.response.data.detail[0];
        });
      }
    },
    change_password: function(event){
      this.error_msg = null;
      this.new_password_error=null;
      this.confirm_new_password_error=null;

      if (this.new_password == "") {
        this.new_password_error = true;
      }else if (this.confirm_new_password == "") {
        this.confirm_new_password_error = true;
      }else{
        this.is_loading = true;
        axios.post(this.change_password_endpoint, {
          email:document.querySelector('#user_email').value,
          password: this.new_password,
          confirm_password: this.confirm_new_password
        })
        .then((response) => {
          this.is_loading = false;
          this.verification_msg = "Password has been successfully changed.";
          setTimeout(function () {
            window.location = '/login/';
          }, 5000);
        }, (error) => {
          console.log(error.response);
          this.is_loading = false;
          this.error_msg = error.response.data.detail[0];
        });
      }
    },
  }
});
