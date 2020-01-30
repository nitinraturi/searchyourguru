<script>
export default {
  methods: {
    guest_headers: function() {
      // let token = localStorage.getItem('user-token')
      let config = {
        headers: {
          'Content-Type': 'application/json'
          // Authorization: `Bearer ${token}`
        }
      }
      return config
    }
  }
}
</script>
