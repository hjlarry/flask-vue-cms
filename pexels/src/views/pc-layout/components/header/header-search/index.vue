<template>
  <div
    class="group rounded-xl relative p-0.5 border-white hover:bg-red-100/40 duration-500"
    ref="containerTarget"
  >
    <m-svg-icon
      class="h-1.5 w-1.5 absolute left-2 top-[50%] translate-y-[-50%]"
      color="#707070"
      name="search"
    ></m-svg-icon>
    <input
      class="block duration-500 w-full h-[44px] pl-4 rounded-xl outline-0 text-sm font-semibold text-zinc-900 dark:text-zinc-200 tracking-wide caret-zinc-400 border border-zinc-100 dark:border-zinc-700 group-hover:border-zinc-200 dark:group-hover:border-zinc-700 focus:border-red-300 bg-zinc-100 dark:bg-zinc-800 group-hover:bg-white dark:group-hover:bg-zinc-900"
      placeholder="搜索"
      v-model="searchValue"
      @focus="isFocus = true"
      @keyup.enter="onSearchHandler"
    />
    <m-svg-icon
      v-show="searchValue"
      class="h-1.5 w-1.5 absolute right-9 top-[50%] translate-y-[-50%] cursor-pointer duration-500"
      color="#707070"
      name="input-delete"
      @click="searchValue = ''"
    ></m-svg-icon>
    <div
      class="h-1.5 w-[1px] absolute right-[62px] bg-zinc-200 top-[50%] translate-y-[-50%] opacity-0 group-hover:opacity-100 duration-500"
    ></div>
    <m-button
      class="absolute right-1 top-[50%] translate-y-[-50%] duration-500 rounded-xl opacity-0 group-hover:opacity-100"
      type="main"
      icon="search"
      iconColor="#ffffff"
      @click="onSearchHandler"
    ></m-button>

    <Transition name="slide">
      <div
        v-show="isFocus"
        class="absolute duration-200 w-[96%] z-20 left-0 top-[56px] max-h-[368px] ml-1 p-2 overflow-auto bg-white dark:bg-zinc-800 text-base border border-zinc-200 dark:border-zinc-600 rounded hover:shadow-2xl scrollbar-thin scrollbar-thumb-rounded-md scrollbar-thumb-zinc-200 dark:scrollbar-thumb-zinc-500 scrollbar-track-transparent"
      >
        <hintVue
          v-show="searchValue"
          :userInput="searchValue"
          @click="onSearchHandler"
        ></hintVue>
        <historyVue v-show="!searchValue" @click="onSearchHandler"></historyVue>
        <hotVue v-show="!searchValue"></hotVue>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { onClickOutside } from '@vueuse/core'

import { searchStore } from '@/stores/search'

import hintVue from './hint.vue'
import historyVue from './history.vue'
import hotVue from './hot.vue'

const sStore = searchStore()

const searchValue = ref('')
const isFocus = ref(false)
// 点击外部区域关闭下拉框
const containerTarget = ref(null)
onClickOutside(containerTarget, () => {
  isFocus.value = false
})
const onSearchHandler = (item: any) => {
  if (typeof item === 'string') {
    searchValue.value = item
  }
  sStore.addHistory(searchValue.value)
  sStore.changeCurrentSearch(searchValue.value)
  isFocus.value = false
}
</script>

<style scoped>
.slide-enter-active {
  transition: all 0.5s;
}

.slide-leave-active {
  transition: all 0.5s;
}

.slide-enter-from,
.slide-leave-to {
  transform: translateY(40px);
  opacity: 0;
}
</style>
