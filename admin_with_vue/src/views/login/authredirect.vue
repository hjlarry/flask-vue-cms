<script>
  export default {
    name: 'authredirect',
    created() {
      console.log(1)
      console.log(window.location.origin)
      const hash = window.location.search.slice(1)
      window.opener.location.href = window.location.origin + '/login#' + hash
      window.close()
    }
  }
</script>
