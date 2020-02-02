var main_app = new Vue({
  delimiters: ["[[", "]]"],
  el: "#password_reset_app",
  data: {
    password_reset_endpoint: "/account/auth/account-password-reset-link/",
    change_password_endpoint: "/account/auth/change-password/",
    reset_email: null,
    reset_email_error: false,
    new_password: null,
    new_password_error: null,
    confirm_new_password: null,
    confirm_new_password_error: null,
    is_loading: false,
    error_msg: null,
    verification_msg: null
  },
  methods: {
    change_password: function(event) {
      this.error_msg = null;
      this.new_password_error = null;
      this.confirm_new_password_error = null;

      if (this.new_password == "") {
        this.new_password_error = true;
      } else if (this.confirm_new_password == "") {
        this.confirm_new_password_error = true;
      } else {
        this.is_loading = true;
        axios
          .post(this.change_password_endpoint, {
            email: document.querySelector("#user_email").value,
            password: this.new_password,
            confirm_password: this.confirm_new_password
          })
          .then(
            response => {
              this.is_loading = false;
              this.verification_msg = "Password has been successfully changed.";
            },
            error => {
              console.log(error.response);
              this.is_loading = false;
              this.error_msg = error.response.data.detail[0];
            }
          );
      }
    }
  }
});
