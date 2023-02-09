<template>
  <div class="h-main">
    Main Content

    <p>
      <m-button type="primary">Primary</m-button>
      <m-button type="main">Main</m-button>
      <m-button type="info">Info</m-button>
      <m-button type="primary" size="small">Primary</m-button>
      <m-button type="main" size="small">Main</m-button>
      <m-button type="info" size="small" :isActiveAnim="false">Info</m-button>
      <m-button type="primary" size="small" icon="close"></m-button>
      <m-button type="main" icon="close"></m-button>
      <m-button type="info" size="small" icon="close"></m-button>
      <m-button type="info" size="small" :loading="true"></m-button>
      <m-button type="notexist">Primary</m-button>
    </p>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped></style>
