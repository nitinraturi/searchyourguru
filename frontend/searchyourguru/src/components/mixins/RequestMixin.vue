<script>
export default {
  methods: {
    guest_headers: function() {
      let config = {
        headers: {
          'Content-Type': 'application/json'
        }
      }
      return config
    },
    get_headers: function(auth = true) {
      let token = localStorage.getItem('guru-user-token')
      let headers = {}
      if (auth == true) {
        headers['Authorization'] = `Bearer ${token}`
      }
      headers['Content-Type'] = 'application/json'

      let config = {
        headers
      }
      return config
    }
  }
}
</script>
