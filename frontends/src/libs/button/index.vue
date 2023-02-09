<template>
  <button
    class="text-sm text-center flex items-center justify-center rounded"
    :class="[typeEnum[type], sizeEnum[sizeKey as sizeType].button, {'active:scale-105':isActiveAnim}]"
    @click.stop="onBtnClick"
  >
    <!-- loading -->
    <m-svg-icon
      v-if="loading"
      name="loading"
      class="w-2 h-2 animate-spin mr-1"
    />
    <!-- 有图标展示图标，没图标展示文字 -->
    <m-svg-icon
      v-if="icon"
      :name="icon"
      :class="sizeEnum[sizeKey as sizeType].icon"
      :color="iconColor"
      :fillClass="iconClass"
    />
    <slot v-else />
  </button>
</template>

<script lang="ts">
const typeEnum = {
  primary:
    'text-white bg-zinc-800 dark:bg-zinc-900 hover:bg-zinc-900 dark:hover:bg-zinc-700 active:bg-zinc-800 dark:active:bg-zinc-700',
  main: 'text-white bg-main dark:bg-zinc-900 hover:bg-hover-main dark:hover:bg-zinc-700 active:bg-main dark:active:bg-zinc-700',
  info: 'text-zinc-800 dark:text-zinc-300 bg-zinc-200 dark:bg-zinc-700 hover:bg-zinc-300 dark:hover:bg-zinc-600 active:bg-zinc-200 dark:active:bg-zinc-700 '
}

const sizeEnum = {
  default: {
    button: 'w-8 h-4 text-base',
    icon: ''
  },
  'icon-default': {
    button: 'w-4 h-4',
    icon: 'w-1.5 h-1.5'
  },
  small: {
    button: 'w-7 h-3 text-base',
    icon: ''
  },
  'icon-small': {
    button: 'w-3 h-3',
    icon: 'w-1.5 h-1.5'
  }
}

type sizeType = keyof typeof sizeEnum
</script>

<script setup lang="ts">
import { computed } from 'vue'

interface Prop {
  type?: 'primary' | 'main' | 'info'
  size?: 'default' | 'small'
  // 关联了一个点击后放大的动画
  isActiveAnim?: boolean
  loading?: boolean
  icon?: string
  iconColor?: string
  iconClass?: string
}

const props = withDefaults(defineProps<Prop>(), {
  type: 'main',
  size: 'default',
  isActiveAnim: true,
  loading: false
})

// 用于获取sizeEnum中对应的class
const sizeKey = computed(() => {
  return props.icon ? 'icon-' + props.size : props.size
})

const emits = defineEmits(['click'])
const onBtnClick = () => {
  if (props.loading) return
  emits('click')
}
</script>

<style scoped></style>
