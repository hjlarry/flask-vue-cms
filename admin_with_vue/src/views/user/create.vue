<template>
  <user-detail :is-edit='false'></user-detail>
</template>

<script>
  import UserDetail from './UserDetail'
  export default {
    name: 'createForm',
    components: { UserDetail }
  }
</script>
