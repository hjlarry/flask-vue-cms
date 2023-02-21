<template>
  <div>
    <ul>
      <li
        v-for="(item, index) in hintList"
        :key="index"
        class="cursor-pointer rounded p-1 text-base font-bold text-zinc-500 duration-500 hover:bg-zinc-300 dark:hover:bg-zinc-900"
        @click="onItemClick(item)"
        v-html="highlightText(item)"
      ></li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { watchDebounced } from '@vueuse/shared'

import { getHint } from '@/api/home'

const props = defineProps<{
  userInput: string
}>()
const emits = defineEmits(['click'])

const hintList = ref<Array<string>>([])
const fillHintList = async () => {
  if (!props.userInput) return
  const res = await getHint({ q: props.userInput })
  hintList.value = res.result
}

const highlightText = (text: string) => {
  const hightlightStr = `<span class="text-zinc-900 dark:text-zinc-200">${props.userInput}</span>`
  const reg = new RegExp(props.userInput, 'gi')
  return text.replace(reg, hightlightStr)
}

const onItemClick = (item: string) => {
  emits('click', item)
}

watchDebounced(() => props.userInput, fillHintList, {
  immediate: true,
  debounce: 500
})
</script>

<style scoped></style>
