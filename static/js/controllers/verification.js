var main_app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#verification_app',
  data: {
    account_activation_endpoint: "/account/auth/account-activation-link/",
    verification_email: null,
    verification_email_error: false,
    is_loading: false,
    error_msg:null,
    verification_msg:null,
    app_state:"login",
    source:"",
  },
  methods: {
    resend_verification_email: function(event){
      this.error_msg = null;
      this.verification_msg=null;
      this.verification_email_error=false;

      if (validateEmail(this.verification_email) == false) {
        this.verification_email_error = true;
      }else{
        this.is_loading = true;
        axios.post(this.account_activation_endpoint, {
          email: this.verification_email
        })
        .then((response) => {
          this.is_loading = false;
          this.verification_msg = "Verification mail has been sent. If not received try again after 60 seconds."
        }, (error) => {
          console.log(error.response);
          this.is_loading = false;
          this.error_msg = error.response.data.detail[0];
        });
      }

    },
  }
});
