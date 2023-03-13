<template>
  <div>{{ formatTime(duration) }}</div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps<{
  time: number
}>()

const emits = defineEmits(['finish'])

const formatTime = (timeSeconds: number) => {
  const hours = Math.floor(timeSeconds / 3600)
  const minutes = Math.floor((timeSeconds % 3600) / 60)
  const seconds = timeSeconds % 60
  const format = (n: number) => n.toString().padStart(2, '0')
  return `${format(hours)}:${format(minutes)}:${format(seconds)}`
}

const duration = ref(props.time)
let timer: any = null
const start = () => {
  timer = setInterval(() => {
    duration.value--
    if (duration.value <= 0) {
      emits('finish')
      clearInterval(timer)
    }
  }, 1000)
}
const close = () => {
  if (timer) {
    clearInterval(timer)
  }
}

onMounted(() => {
  start()
})
onUnmounted(() => {
  close()
})
</script>

<style scoped></style>
