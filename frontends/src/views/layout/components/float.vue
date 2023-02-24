<template>
  <div class="fixed bottom-5 right-5">
    <m-popover placement="left">
      <template #target>
        <div
          class="flex items-center justify-center w-4 h-4 rounded-full cursor-pointer border border-zinc-200 dark:border-0 dark:bg-zinc-900 hover:shadow-lg"
        >
          <m-svg-icon
            name="feedback"
            class="w-2 h-2"
            fillClass="fill-zinc-900 dark:fill-zinc-200 "
          />
        </div>
      </template>
      <template #dropdown>
        <div class="w-[140px]">
          <div
            class="flex items-center space-x-1 p-1 rounded-sm cursor-pointer hover:bg-zinc-100/60 dark:hover:bg-zinc-700"
            @click="onFeedClick"
          >
            <m-svg-icon
              name="feedback"
              class="w-1.5 h-1.5"
              fillClass="fill-zinc-900 dark:fill-zinc-300"
            />
            <span class="text-sm text-zinc-800 dark:text-zinc-300"
              >提点建议</span
            >
          </div>
        </div>
      </template>
    </m-popover>
  </div>
</template>

<script setup lang="ts">
const onFeedClick = () => {
  window.open('http://www.baidu.com', '_blank')
}
</script>

<style scoped></style>
