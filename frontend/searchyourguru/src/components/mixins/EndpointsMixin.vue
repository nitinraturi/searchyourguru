<script>
export default {
  data: function() {
    return {
      base_api_url: 'http://localhost:8005',
      endpoints: {
        login: '/account/auth/login/',
        logout: '/account/auth/logout/',
        signup: '/account/auth/register/',
        account_activation: '/account/auth/account-activation-link/',
        password_reset: '/account/auth/account-password-reset-link/',
        change_password: '/account/auth/change-password/',
        user_profile: '/account/user/',
        update_user_profile: '/account/user/update-profile/',
        update_password: '/account/user/update-password/',
        subjects: '/tution/subjects/'
      }
    }
  },
  methods: {
    get_endpoint: function(endpoint) {
      return this.base_api_url + endpoint
    }
  }
}
</script>
