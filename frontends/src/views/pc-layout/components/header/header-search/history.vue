<template>
  <div>
    <div class="flex items-center">
      <span class="text-zinc-400 text-xs">最近搜索</span>
      <m-svg-icon
        name="delete"
        class="w-2.5 h-2.5 ml-1 p-0.5 cursor-pointer rounded-sm hover:bg-zinc-100"
        fillClass="fill-zinc-400"
        @click="onClearClick"
      ></m-svg-icon>
    </div>
    <ul class="flex flex-wrap font-bold text-sm space-x-1">
      <li
        v-for="(item, index) in sStore.$state.searchHistory"
        :key="index"
        class="flex items-center px-1.5 py-0.5 my-0.5 rounded-sm cursor-pointer duration-500 bg-zinc-100 hover:bg-zinc-200"
        @click="onItemClick(item)"
      >
        {{ item }}
        <m-svg-icon
          name="input-delete"
          class="h-2.5 w-2.5 ml-1 p-0.5 rounded-sm hover:bg-zinc-100"
          @click.stop="onItemDeleteClick(index)"
        ></m-svg-icon>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { confirm } from '@/libs/confirm'
import { searchStore } from '@/stores/search'

const sStore = searchStore()
const emits = defineEmits(['click'])
const onItemClick = (item: string) => {
  emits('click', item)
}

const onItemDeleteClick = (index: number) => {
  sStore.removeHistory(index)
}

const onClearClick = () => {
  confirm('确定清空搜索历史吗？')
    .then(() => {
      sStore.clearHistory()
    })
    .catch(() => {})
}
</script>

<style scoped></style>
