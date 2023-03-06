<template>
  <div class="relative">
    <input
      v-if="type === 'text'"
      v-model="inputValue"
      :maxlength="maxlength"
      class="border-gray-200 border-[1px] text-sm rounded-sm w-full p-1 outline-none focus:border-blue-400"
      type="text"
    />

    <textarea
      v-if="type === 'textarea'"
      v-model="inputValue"
      :maxlength="maxlength"
      class="border-gray-200 border-[1px] text-sm rounded-sm w-full p-1 -my-1 outline-none focus:border-blue-400"
      rows="6"
      type="text"
    ></textarea>

    <span
      v-if="maxlength"
      class="absolute text-xs right-1 bottom-1 text-zinc-400"
      :class="currentLength === maxlength ? 'text-red-400' : ''"
      >{{ currentLength }} / {{ maxlength }}</span
    >
  </div>
</template>

<script setup lang="ts">
import { useVModel } from '@vueuse/core'
import { computed } from 'vue'

interface Prop {
  modelValue: string
  type?: 'text' | 'textarea'
  maxlength?: number
}

const props = withDefaults(defineProps<Prop>(), {
  type: 'text'
})
defineEmits(['update:modelValue'])

const inputValue = useVModel(props)
const currentLength = computed(() => {
  return (inputValue.value as string).length
})
</script>

<style scoped></style>
