<script>
export default {
  data: function() {
    return {
      base_api_url: process.env.VUE_APP_API_ENDPOINT || 'http://localhost:8005',
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
        zipcode_check: '/account/user/zipcode-check/',
        subjects: '/tution/subjects/',
        tution_search: '/tution/search/',
        tution_create: '/tution/create/',
        tution_update: '/tution/update/',
        tution_delete: '/tution/delete/',
        contact: '/account/contact/',
        tution_list: '/tution/list/',
        tution_request_applied: '/tution/tution-applied/',
        tution_request_add: '/tution/tution-request/',
        suggested_cities: '/tution/suggested-cities/',
        suggested_subjects: '/tution/suggested-subjects/'
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
