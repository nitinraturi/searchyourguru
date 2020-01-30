<script>
export default {
  data: function() {
    return {
      base_api_url: 'http://localhost:8005',
      endpoints: {
        login: '/account/auth/login/',
        signup: '/account/auth/register/',
        account_activation: '/account/auth/account-activation-link/'
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
