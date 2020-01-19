var app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#login-app',
  data: {
    auth_token_endpoint:"/auth/token/",
    login_email: null,
    login_password: null,
    invalid_login: false,
    login_error_message: null,
    is_login_loading: false,
    errors:[],
  },
  methods: {
    login: function(event) {
      let login_btn = $('#login_btn');
      if (validateEmail(this.login_email) == false) {
        this.login_error_message = "Please enter a valid email"
      } else if (this.login_password == "") {
        this.login_error_message = "Please fill in the password"
      } else {
        this.invalid_login = null;
        this.login_error_message = null;
        this.is_login_loading = true;
        axios.post(`http://jsonplaceholder.typicode.com/posts`, {
          body: this.data
        })
        .then(response => {})
        .catch(e => {
          this.errors.push(e)
        })
      }
    },
  }
});
