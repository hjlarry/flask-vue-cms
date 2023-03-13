<template>
  <div class="flex flex-col items-center">
    <m-svg-icon
      v-if="isMobileDevice"
      name="close"
      class="w-3 h-3 ml-auto p-0.5 m-1"
      @click="onCloseClick"
    />

    <img :src="blob" ref="imgTarget" />

    <m-button
      class="mt-4 mb-1 w-[80%] xl:w-1/2"
      :isActiveAnim="false"
      @click="onConfirmClick"
      >确定</m-button
    >
  </div>
</template>

<script lang="ts">
const pc_template = `
<cropper-canvas background style="min-height:500px;min-width:500px">
  <cropper-image></cropper-image>
  <cropper-shade hidden></cropper-shade>
  <cropper-handle action="select" plain></cropper-handle>
  <cropper-selection initial-coverage="0.5" movable resizable zoomable>
    <cropper-grid role="grid" bordered covered></cropper-grid>
    <cropper-crosshair theme-color="rgba(238, 238, 238, 0.5)" centered></cropper-crosshair>
    <cropper-handle action="move" theme-color="rgba(255, 255, 255, 0.35)"></cropper-handle>
    <cropper-handle action="n-resize"></cropper-handle>
    <cropper-handle action="e-resize"></cropper-handle>
    <cropper-handle action="s-resize"></cropper-handle>
    <cropper-handle action="w-resize"></cropper-handle>
    <cropper-handle action="ne-resize"></cropper-handle>
    <cropper-handle action="nw-resize"></cropper-handle>
    <cropper-handle action="se-resize"></cropper-handle>
    <cropper-handle action="sw-resize"></cropper-handle>
  </cropper-selection>
</cropper-canvas>
`
const mobile_template = `
<cropper-canvas background style="min-height:60vh;min-width:60vh">
  <cropper-image></cropper-image>
  <cropper-shade hidden></cropper-shade>
  <cropper-handle action="select" plain></cropper-handle>
  <cropper-selection initial-coverage="0.5" movable resizable zoomable>
    <cropper-handle action="move" theme-color="rgba(255, 255, 255, 0.35)"></cropper-handle>
  </cropper-selection>
</cropper-canvas>
`
</script>

<script setup lang="ts">
import { userStore } from '@/stores/user'
import { isMobileDevice } from '@/utils/flexiable'
import Cropper from 'cropperjs'
import { ref, onMounted } from 'vue'

defineProps<{
  blob: string
}>()
const emits = defineEmits(['close'])

const onCloseClick = () => {
  emits('close')
}
const imgTarget = ref<HTMLImageElement | null>(null)

const uStore = userStore()

let cropper: Cropper
onMounted(() => {
  cropper = new Cropper(imgTarget.value!, {
    template: isMobileDevice.value ? mobile_template : pc_template
  })
})

const onConfirmClick = () => {
  cropper
    .getCropperSelection()
    ?.$toCanvas()
    .then((canvas) => {
      uStore.setUserInfo({
        ...uStore.userInfo,
        avatar: canvas.toDataURL('image/jpeg', 0.5)
      })
    })
  location.reload()
}
</script>

<style scoped></style>
