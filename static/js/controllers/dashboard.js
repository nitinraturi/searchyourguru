var main_app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#dashboard_app',
  data: {
    endpoints: {
      user_profile: "/account/user/",
      update_user_profile: "/account/user/update-profile/",
      update_password: "/account/user/update-password/"
    },
    app_state: "change_password",
    is_loading: false,
    general_settings: {
      user_name: "",
      user_name_error: null,
      user_phone: "",
      user_phone_error: null,
      user_email: "",
      user_email_error: null,
      edit_mode: false,
      mode_text: "Edit",
      is_loading: false,
    },
    change_password: {
      old_password: "",
      new_password: "",
      confirm_new_password: "",
      error_msg: null,
      mode_text: "Update",
      is_loading: false,

    }
  },
  mounted: function() {
    this.get_user_profile();
  },
  methods: {
    set_app_state: function(state) {
      this.app_state = state;
    },
    save_formdata: function(source) {
      // general_settings form toggle
      if (source == "general_settings") {
        this.general_settings.edit_mode = !this.general_settings.edit_mode
        if (this.general_settings.edit_mode == true) {
          this.general_settings.mode_text = "Save";
        } else {
          this.general_settings.mode_text = "Edit";
          this.update_general_profile();
        }
      }

      // change_password form toggle
      if (source == "change_password") {
        this.update_password();
      }
    },
    get_request_config: function() {
      let token = localStorage.getItem('user-token');
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`
        }
      }
      return config;
    },
    update_general_profile: function() {
      this.general_settings.is_loading = true;
      axios.post(this.endpoints.update_user_profile, {
          'name': this.general_settings.user_name
        }, this.get_request_config())
        .then((response) => {
          this.general_settings.is_loading = false;
        }, (error) => {
          this.general_settings.is_loading = false;
        });
    },
    update_password: function() {
      this.change_password.is_loading = true;
      this.change_password.error_msg = null;
      axios.post(this.endpoints.update_password, {
          'old_password': this.change_password.old_password,
          'new_password': this.change_password.new_password,
          'confirm_new_password': this.change_password.confirm_new_password
        }, this.get_request_config())
        .then((response) => {
          this.change_password.is_loading = false;
          this.change_password.error_msg = null;
          this.change_password.old_password = "";
          this.change_password.new_password = "";
          this.change_password.confirm_new_password = "";
        }, (error) => {
          this.change_password.error_msg = error.response.data.detail[0];
          this.change_password.is_loading = false;
        });
    },
    get_user_profile: function() {
      let config = this.get_request_config()
      axios.get(this.endpoints.user_profile, config)
        .then((response) => {
          let res = response.data;
          this.is_loading = false;
          this.general_settings.user_name = res.first_name;
          this.general_settings.user_email = res.email;
          this.general_settings.user_phone = res.phone;
        }, (error) => {
          this.is_loading = false;
        });
    }
  }
});
