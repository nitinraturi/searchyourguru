var main_app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#signup_app',
  data: {
    signup_endpoint: "/account/auth/register/",
    signup_user_type: null,
    signup_user_name: null,
    signup_user_phone: null,
    signup_email: null,
    signup_password: null,
    signup_confirm_password: null,
    invalid_signup: false,
    is_signup_loading: false,
    success_signup_message:null,
    signup_user_type_error: null,
    signup_user_name_error: null,
    signup_user_phone_error: null,
    signup_email_error: null,
    signup_password_error: null,
    errors: null,
  },
  methods: {
    signup: function(event) {
      this.signup_user_type_error = null;
      this.signup_user_name_error = null;
      this.signup_user_phone_error = null;
      this.signup_email_error = null;
      this.signup_password_error = null;
      this.errors = null;

      if (this.signup_user_type == null) {
        this.signup_user_type_error = "This field is required";
      }else if(this.signup_user_name == null){
        this.signup_user_name_error = "This field is required";
      }else if(this.signup_user_phone == null){
          this.signup_user_phone_error = "This field is required";
      }else if(this.signup_user_phone.toString().length != 10){
        this.signup_user_phone_error = "Phone number should be of 10 digits";
      }else if (validateEmail(this.signup_email) == false) {
        this.signup_email_error = "Please enter a valid email"
      }else if (this.signup_password == null || this.signup_confirm_password == null) {
        this.signup_password_error = "Please fill in the password and confirm_password both";
      }else {
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
            this.success_signup_message = true;
          }, (error) => {
            console.log(error.response);
            this.errors = error.response.data.errors;
            this.is_signup_loading = false;

            if(this.errors.first_name){
              this.signup_user_name_error=this.errors.first_name[0];
            }

            if(this.errors.email){
              this.signup_email_error=this.errors.email[0];
            }

            if(this.errors.phone){
              this.signup_user_phone_error=this.errors.phone[0];
            }

            if(this.errors.password){
              this.signup_password_error=this.errors.password[0];
            }

            if(this.errors.user_type){
              this.signup_user_type_error=this.errors.user_type[0];
            }
          });
      }
    },
  }
});
