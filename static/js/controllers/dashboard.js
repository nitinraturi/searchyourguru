var main_app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#dashboard_app',
  data: {
    app_state:"account",
    is_login_loading: false,
    general_settings:{
      user_name:"",
      user_name_error:null,
      user_phone:"",
      user_phone_error:null,
      user_email:"",
      user_email_error:null,
      edit_mode:true,
    },
  },
  methods: {
    set_app_state: function(state) {
      this.app_state = state;
    },
    update_general_profile:function(){
      // axios.post(this.login_endpoint, {
      // })
      // .then((response) => {
      //   this.is_login_loading = false;
      // }, (error) => {
      //
      //   this.is_login_loading = false;
      // });
    }
  }
});
