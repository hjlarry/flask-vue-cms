<template>
  <div class="flex flex-col items-center">
    <m-svg-icon
      name="close"
      class="w-3 h-3 ml-auto p-0.5 m-1"
      @click="onCloseClick"
    />
    <img :src="blob" />
    <m-button class="mt-4 mb-1 w-[80%] xl:w-1/2">确定</m-button>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  blob: string
}>()
const emits = defineEmits(['close'])

const onCloseClick = () => {
  emits('close')
}
</script>

<style scoped></style>
