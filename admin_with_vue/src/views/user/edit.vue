<template>
  <user-detail :is-edit='true'></user-detail>
</template>

<script>
  import UserDetail from './UserDetail'
  export default {
    name: 'editForm',
    components: { UserDetail }
  }
</script>
