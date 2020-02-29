<script>
export default {
  methods: {
    validEmail: function(email) {
      var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      var re = new RegExp(pattern)
      return re.test(email)
    }
  }
}
</script>
