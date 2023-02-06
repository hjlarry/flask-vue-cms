import { computed } from 'vue'
import { useWindowSize } from '@vueuse/core'

const { width } = useWindowSize()

export const isMoibleDevice = computed(() => {
  return width.value < 1280
})
